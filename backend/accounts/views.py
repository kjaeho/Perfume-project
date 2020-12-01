# from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


from .models import User, Clothes
from .serializers import UserSerializer, ClothesSerializer

# from django.conf import settings
from perfumes.models import Perfume
from perfumes.serializers import PerfumeSerializer

from itertools import combinations
from django.db.models import Q

import numpy as np
from keras.models import load_model
import glob
from PIL import Image
import matplotlib.pyplot as plt
import cv2
import random

User = get_user_model()


@api_view(["GET"])
def userdetail(request, email):
    selected_user = get_object_or_404(User, email=email)
    serializer = UserSerializer(selected_user)
    return Response(serializer.data)


@api_view(["POST"])
def joinplus(request, email):
    selected_user = get_object_or_404(User, email=email)
    serializer = UserSerializer(selected_user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(gender=request.data["gender"], age=request.data["age"])
        return Response(serializer.validated_data)
@api_view(["GET"])
def clothes_get_main(request):
    api_data = []
    clothes = Clothes.objects.order_by("-id")[:18]
    serializer = ClothesSerializer((clothes),many=True)
    for cloth in serializer.data:
            perfume_data = []
            for perfume_id in cloth["perfume"]:
                perfume = get_object_or_404(Perfume, id=perfume_id)
                perfume_data.append(PerfumeSerializer(perfume).data)
            api_data.append({**cloth, "perfumedata": perfume_data})
    return Response({"status": 200, "data": api_data})

@api_view(["GET", "POST"])
# @permission_classes([IsAuthenticated])
def clothes_get_create(request):
    if request.method == "GET":
        """
        # 페이지 쓸거면
        page = request.GET.get('page', 1)
        PER_PAGE = 6
        clothes = Paginator(Clothes.objects.all().order_by('-pk'), PER_PAGE)
        serializer = ClothesSerializer(clothes.page(page), many=True)
        """
        api_data = []
        clothes = Clothes.objects.all().order_by("-id")
        serializer = ClothesSerializer((clothes), many=True)
        for cloth in serializer.data:
            perfume_data = []
            for perfume_id in cloth["perfume"]:
                perfume = get_object_or_404(Perfume, id=perfume_id)
                perfume_data.append(PerfumeSerializer(perfume).data)
            api_data.append({**cloth, "perfumedata": perfume_data})
        return Response({"status": 200, "data": api_data})

    elif request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponse("Unauthorized", status=401)

        serializer = ClothesSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            clothes = serializer.save()
            image_dir = serializer.data["image"][1:]

            # new_image_dir = human_segmentation(image_dir)
            # extract_adjective(image_dir, new_image_dir)

            adjetive_3 = extract_adjective(image_dir)
            clothes.adjectives = (
                adjetive_3[0] + "," + adjetive_3[1] + "," + adjetive_3[2]
            )
            clothes.user = request.user
            perfumeData, lines = recommend_adjective(clothes.adjectives)

            line_cloth = ""
            for line in lines:
                line_cloth += "," + line
            line_cloth = line_cloth[1:]
            clothes.lines = line_cloth
            # 향수 추천 데이터 저장
            if perfumeData == None:
                clothes.save()
                return Response(
                    {"data": ClothesSerializer(clothes).data, "perfumedata": ""}
                )
            else:
                perfumes = []
                for perfume_id in perfumeData:
                    perfume = get_object_or_404(Perfume, id=perfume_id)
                    clothes.perfume.add(perfume)
                    perfumes.append(PerfumeSerializer(perfume).data)
                clothes.save()
                return Response(
                    {
                        "data": ClothesSerializer(clothes).data,
                        "perfumedata": perfumes,
                    }
                )


@api_view(["PUT", "DELETE"])
@permission_classes([IsAuthenticated])
def clothes_update_delete(request, clothes_id):
    clothes = get_object_or_404(Clothes, id=clothes_id)
    if not clothes.user == request.user:
        return HttpResponse("Forbidden", status=403)
    if request.method == "PUT":
        serializer = ClothesSerializer(clothes, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"data": serializer.data})
    else:
        clothes.delete()
        return Response({"status": 200})


def human_segmentation(image_dir):
    model = load_model("AI-model/unet_no_drop.h5")

    def preprocess(img):
        im = np.zeros((IMG_WIDTH, IMG_HEIGHT, 3), dtype=np.uint8)

        if img.shape[0] >= img.shape[1]:
            scale = img.shape[0] / IMG_HEIGHT
            new_width = int(img.shape[1] / scale)
            diff = (IMG_WIDTH - new_width) // 2
            img = cv2.resize(img, (new_width, IMG_HEIGHT))

            im[:, diff : diff + new_width, :] = img
        else:
            scale = img.shape[1] / IMG_WIDTH
            new_height = int(img.shape[0] / scale)
            diff = (IMG_HEIGHT - new_height) // 2
            img = cv2.resize(img, (IMG_WIDTH, new_height))

            im[diff : diff + new_height, :, :] = img

        return im

    def postprocess(img_ori, pred):
        h, w = img_ori.shape[:2]

        mask_ori = (pred.squeeze()[:, :, 1] > THRESHOLD).astype(np.uint8)
        max_size = max(h, w)
        result_mask = cv2.resize(mask_ori, dsize=(max_size, max_size))

        if h >= w:
            diff = (max_size - w) // 2
            if diff > 0:
                result_mask = result_mask[:, diff:-diff]
        else:
            diff = (max_size - h) // 2
            if diff > 0:
                result_mask = result_mask[diff:-diff, :]

        result_mask = cv2.resize(result_mask, dsize=(w, h))

        result_mask *= 255

        # smoothen edges
        result_mask = cv2.GaussianBlur(result_mask, ksize=(9, 9), sigmaX=5, sigmaY=5)

        return result_mask

    IMG_PATH = image_dir

    img = cv2.imread(IMG_PATH, cv2.IMREAD_COLOR)
    # print("-------------이미지 경로-----------")
    img_ori = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2RGB)

    IMG_WIDTH, IMG_HEIGHT = 256, 256

    img = preprocess(img)
    # print("----------reshape 전------------")
    input_img = img.reshape((1, IMG_WIDTH, IMG_HEIGHT, 3)).astype(np.float32) / 255.0
    # print("----------reshape 후------------")

    pred = model.predict(input_img)

    THRESHOLD = 0.5
    EROSION = 1

    mask = postprocess(img_ori, pred)

    converted_mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    result_img = cv2.subtract(converted_mask, img_ori)
    result_img = cv2.subtract(converted_mask, result_img)

    result_img = cv2.cvtColor(result_img, cv2.COLOR_RGB2RGBA)
    mask = cv2.medianBlur(mask, 5)

    h, w, _ = result_img.shape
    image_cut = cv2.bitwise_and(result_img, result_img, mask=mask)

    # 이상해짐
    # image_cut.resize((128, 128))

    # plt.figure(figsize=(16, 16))
    # plt.imshow(image_cut)
    # plt.show()
    # print("================image-cut===============")
    # print(type(image_cut), image_cut.shape)
    # new_img = Image.fromarray(image_cut)
    new_image_dir = "media/clothes/" + image_dir[14:-4] + "-cut.jpg"

    # new_img.save("media/clothes/test.jpeg")
    # cv2.imwrite(new_image_dir, image_cut)
    cv2.imwrite(new_image_dir, cv2.cvtColor(image_cut, cv2.COLOR_RGBA2BGRA))
    # cv2.imwrite(new_image_dir, dst)

    # return image_cut
    return new_image_dir


# def extract_adjective(image_dir, image_cut_dir):
def extract_adjective(image_dir):
    CNN_model = load_model("AI-model/형용사_45_model.h5")
    labels = [
        "가벼운",
        "개성적인",
        "거친",
        "고급스러운",
        "관능적인",
        "귀여운",
        "기운찬",
        "깔끔한",
        "남성적인",
        "달콤한",
        "도시적인",
        "동양적인",
        "동적인",
        "따뜻한",
        "맑은",
        "매력적인",
        "무거운",
        "밝은",
        "부드러운",
        "사랑스러운",
        "상쾌한",
        "서양적인",
        "성숙한",
        "소박한",
        "수수한",
        "순수한",
        "시원한",
        "신선한",
        "어두운",
        "여성적인",
        "우아한",
        "은은한",
        "인공적인",
        "자연적인",
        "전원적인",
        "전통적인",
        "젊은",
        "점잖은",
        "정적인",
        "중후한",
        "차가운",
        "차분한",
        "편안한",
        "현대적인",
        "화려한",
    ]
    # cut = []
    # img_cut = Image.open(image_cut_dir)
    # img_cut = img_cut.convert("RGB")
    # img_cut = img_cut.resize((128, 128))
    # data_cut = np.asarray(img_cut)
    # cut.append(data_cut)
    # cut = np.array(cut)
    # cut = cut.astype("float32") / 255

    origin = []
    img_origin = Image.open(image_dir)
    img_origin = img_origin.convert("RGB")
    img_origin = img_origin.resize((128, 128))
    data_origin = np.asarray(img_origin)
    origin.append(data_origin)
    origin = np.array(origin)
    origin = origin.astype("float32") / 255

    # r_cut = CNN_model.predict(cut, batch_size=32)
    r_origin = CNN_model.predict(origin, batch_size=32)

    # res_cut = r_cut[0]
    res_origin = r_origin[0]
    res = dict()
    # print("여기는 오리진")
    for i, acc in enumerate(res_origin):
        # print(labels[i], "=", np.round(acc * 100, 3))
        res[labels[i]] = np.round(acc * 100, 3)

    # print("----------------------------------")
    # print("여기는 cut")
    # for i, acc in enumerate(res_cut):
    #     # res[labels[i]] = np.round(acc*100, 3)
    #     print(labels[i], "=", np.round(acc * 100, 3))

    # print("예측결과 : ", labels[res_cut.argmax()])
    # print("")
    # res_cut = res_cut.reshape((1, -1))
    # print(res)
    adjectives = sorted(res, key=lambda x: res[x])[::-1][:3]
    return adjectives


def recommend_adjective(adjectives):
    line = {
        0: "floral",
        1: "citrus",
        2: "chypre",
        3: "oriental",
        4: "fruity",
        5: "woody",
        6: "green",
        7: "aldehyde",
        8: "spicy",
        9: "fougere",
        10: "gourmand",
        11: "musk",
        12: "vanilla",
        13: "leather",
        14: "aromatic",
        15: "aquatic",
    }
    lines = {
        0: [
            "도시적인",
            "성숙한",
            "화려한",
            "관능적인",
            "은은한",
            "따뜻한",
            "우아한",
            "사랑스러운",
            "여성적인",
            "고급스러운",
        ],
        1: ["무거운", "도시적인", "성숙한", "중후한", "남성적", "점잖은", "매력적인", "깔끔한", "고급스러움", "현대적인"],
        2: ["맑은", "자연적인", "성숙한", "수수한", "부드러운", "차분한", "은은한", "따뜻한", "편안한", "여성적인"],
        3: ["전통적인", "성숙한", "화려한", "거친", "관능적인", "동양적인", "달콤한", "우아한", "고급스러운", "개성적인"],
        4: [
            "맑은",
            "귀여운",
            "가벼운",
            "상쾌한",
            "밝은",
            "기운찬",
            "젊은",
            "순수한",
            "신선한",
            "깔끔함",
            "자연적인",
            "사랑스러운",
        ],
        5: ["무거운", "성숙한", "중후한", "부드러운", "점잖은", "차분한", "수수한", "자연적인", "편안한", "전원적인"],
        6: [
            "맑은",
            "상쾌한",
            "밝은",
            "소박한",
            "부드러운",
            "차분한",
            "순수한",
            "신선한",
            "은은한",
            "따뜻한",
            "깔끔한",
            "자연적인",
            "편안한",
        ],
        7: ["맑은", "귀여운", "상쾌한", "부드러운", "차분한", "매력적인", "신선한", "깔끔한", "편안한", "사랑스러운"],
        8: ["무거운", "어두운", "성숙한", "도시적인", "중후한", "남성적인", "거친", "관능적인", "인공적인", "현대적인"],
        9: ["화려한", "부드러운", "차분한", "점잖은", "매력적인", "순수한", "서양적인", "은은한", "따뜻한", "달콤한"],
        10: ["무거운", "성숙한", "도시적인", "관능적인", "인공적인", "우아한", "개성적인", "현대적인", "인공적인"],
        11: ["맑은", "소박한", "부드러운", "차분한", "매력적인", "순수한", "은은한", "깔끔한", "달콤한", "편안한"],
        12: ["밝은", "화려한", "부드러운", "무거운", "차분한", "관능적인", "여성적인", "따뜻한", "달콤한", "우아한"],
        13: [
            "무거운",
            "중후한",
            "성숙한",
            "관능적인",
            "어두운",
            "동적인",
            "서양적인",
            "인공적인",
            "고급스러운",
            "현대적인",
        ],
        14: ["상쾌한", "화려한", "기운찬", "매력적인", "젊은", "동양적인", "따뜻한", "자연적인", "깔끔한", "시원한"],
        15: ["맑은", "상쾌한", "시원한", "차가운", "신선한", "은은한", "자연적인", "편안한", "개성적인", "동적인"],
    }
    cnt = [0] * 16
    adjectives = adjectives.split(",")
    for i in range(len(adjectives)):
        for k, v in lines.items():
            if adjectives[i] in v:
                cnt[k] += 1
    Max_line_num = max(cnt)
    Max_line = []
    for i in range(16):
        if cnt[i] == Max_line_num:
            Max_line.append(line[i])
    if len(Max_line) == 1:
        perfume_tmp = Perfume.objects.filter(line__icontains=Max_line[0])
        serializer = PerfumeSerializer(perfume_tmp, many=True)

    elif len(Max_line) == 2:
        perfume_tmp = Perfume.objects.filter(
            Q(line__icontains=Max_line[0]) & Q(line__icontains=Max_line[1])
        )
        if len(perfume_tmp) == 0:
            perfume_tmp = Perfume.objects.filter(
                Q(line__icontains=Max_line[0]) | Q(line__icontains=Max_line[1])
            )
        serializer = PerfumeSerializer(perfume_tmp, many=True)

    else:
        Max_line = random.sample(Max_line, 2)
        perfume_tmp = Perfume.objects.filter(
            Q(line__icontains=Max_line[0]) & Q(line__icontains=Max_line[1])
        )
        if len(perfume_tmp) == 0:
            perfume_tmp = Perfume.objects.filter(
                Q(line__icontains=Max_line[0]) | Q(line__icontains=Max_line[1])
            )
        serializer = PerfumeSerializer(perfume_tmp, many=True)
    se_cnt = len(serializer.data)
    if se_cnt == 1:
        return [serializer.data[0]["id"]], Max_line
    elif se_cnt == 2:
        return [serializer.data[0]["id"], serializer.data[1]["id"]], Max_line
    elif se_cnt >= 3:
        tmp = random.sample(range(0, se_cnt), 3)
        c = []
        for i in tmp:
            c.append(serializer.data[i]["id"])
        return c, Max_line

    # for i in serializer.data:
    #     print(i)
    # print(serializer.data)
    # return Response(serializer.data)
