from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Perfume
from .serializers import PerfumeSerializer

from django.db.models import Sum,Avg,Count,Max,Q

# from django.core.exceptions import ObjectDoesNotExist

# 추천
import random

# import pandas as pd
# import numpy as np

# import pymysql
# from sqlalchemy import create_engine
# from sklearn.metrics.pairwise import cosine_similarity


# Create your views here.

@api_view(['GET'])
def recentList(request,page_num):
    perfumes = Perfume.objects.order_by('-year')
    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)
    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def listBy(request,gender,brand,line,page_num):
    if gender == '0':
        gender = ""
    if brand == '0':
        brand = ''
    if line == '0':
        line =''
    if gender != -1 and brand != -1 and line != -1:
        perfumes = Perfume.objects.filter(gender=gender,brand__icontains=brand,line__icontains=line)
    elif gender != -1 and brand == -1 and line == -1:
        perfumes = Perfume.objects.filter(gender=gender)
    elif gender == -1 and brand != -1 and line == -1:
        perfumes = Perfume.objects.filter(brand__icontains=brande)
    elif gender == -1 and brand == -1 and line != -1:
        perfumes = Perfume.objects.filter(line__icontains=lin)
    elif gender != -1 and brand != -1 and line == -1:
        perfumes = Perfume.objects.filter(gender=gender,brand__icontains=brand)
    elif gender != -1 and brand == -1 and line != -1:
        perfumes = Perfume.objects.filter(gender=gender,line__icontains=lin)
    elif gender == -1 and brand != -1 and line != -1:
        perfumes = Perfume.objects.filter(brand__icontains=brand,line__icontains=lin)

    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)

    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def perfumeDetail(request, perfume_id):
    select_perfume = Perfume.objects.filter(id=perfume_id)
    serializer = PerfumeSerializer(select_perfume,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def genderList(request,gender,page_num):
    perfumes = Perfume.objects.filter(gender=gender).order_by('-year')
    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)
    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def brandList(request,brand,page_num):
    perfumes = Perfume.objects.filter(brand=brand).order_by('-year')
    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)
    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def lineList(request,line,page_num):
    perfumes = Perfume.objects.filter(line=line).order_by('-year')
    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)
    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def perfumeSearch(request, word, page_num):
    word_upper = word.title()
    perfumes = Perfume.objects.filter(Q(brand__icontains=word_upper)|Q(name__icontains=word)|Q(line__icontains=word_upper))
    paginator = Paginator(perfumes,16)
    page_num=page_num
    page_obj = paginator.get_page(page_num)
    serializer = PerfumeSerializer(page_obj, many=True)
    return Response({
        'perfumeData':serializer.data,
        'pageNum':perfumes.count()
    })


@api_view(['GET'])
def byAgeRecommend(request): # 새내기
    newmen = Perfume.objects.filter(id__in=random.sample(['476','265','1904','77','253','252','59','575','966','968'],4))
    newwomen = Perfume.objects.filter(id__in=random.sample(['121', '137', '126', '265', '542', '928', '2681', '1862'],4))
    socialmen = Perfume.objects.filter(id__in=random.sample(['959', '253', '1812', '476', '1165', '64', '720', '1704', '69', '968', '778'],4))
    socialwomen = Perfume.objects.filter(id__in=random.sample(['1127', '497', '626', '959', '671', '497', '1391', '1803', '129', '1835'],4))
    tmen = Perfume.objects.filter(id__in=random.sample(['1704', '968', '474', '71', '1812','2002','1059', '1002', '1974', '778', '747', '2514', '2558', '2574'],4))
    twomen = Perfume.objects.filter(id__in=random.sample(['504', '2004', '542', '928', '2596', '2606', '131', '1704', '203', '148', '1835', '2606', '127', '128'],4))
    fmen = Perfume.objects.filter(id__in=random.sample(['313', '472', '2514', '747','720', '920', '710', '1072', '1867'],4))
    fwomen = Perfume.objects.filter(id__in=random.sample(['497', '671', '1127', '641', '1002', '1719', '130', '959', '928', '1812', '1765', '1744', '1056','1063', '1619', '1605', '1599', '523', '469', '2278', '2272', '2246', '2227', '198', '220'],4))
    men = Perfume.objects.filter(id__in=random.sample(['720', '199', '486', '71', '618'],4))
    women = Perfume.objects.filter(id__in=random.sample(['150', '89', '75', '546', '641'],4))
    serializer = PerfumeSerializer(newmen,many=True)
    serializer1 = PerfumeSerializer(newwomen,many=True)
    serializer2 = PerfumeSerializer(socialmen,many=True)
    serializer3 = PerfumeSerializer(socialwomen,many=True)
    serializer4 = PerfumeSerializer(tmen,many=True)
    serializer5 = PerfumeSerializer(twomen,many=True)
    serializer6 = PerfumeSerializer(fmen,many=True)
    serializer7 = PerfumeSerializer(fwomen,many=True)
    serializer8 = PerfumeSerializer(men,many=True)
    serializer9 = PerfumeSerializer(women,many=True)
    return Response({
        'newmen':serializer.data,
        'newwomen':serializer1.data,
        'socialmen':serializer2.data,
        'socialwomen':serializer3.data,
        'thirtymen':serializer4.data,
        'thirtywomen':serializer5.data,
        'fortymen':serializer6.data,
        'fortywomen':serializer7.data,
        'fiftymen':serializer8.data,
        'fiftywomen':serializer9.data,
    })

@api_view(['GET'])
def weatherRecommend(request): # 계절
    weathers = {
        0 : ["상쾌한","따뜻한","가벼운","달콤한","밝은","순수한","편안한","부드러운","사랑스러운"],
        1 : ["기운찬","맑은","매력적인","밝은","신선한","동적인","자연적인","젊은"],
        2 : ["깔끔한","도시적인","가벼운","시원한","우아한","은은한","점잖은","차분한"],
        3 : ["고급스러운","도시적인","무거운","시원한","어두운","우아한","정적인","차가운","성숙한"]
    }
    
    for k, weather in weathers.items():
        if k == 0:
            spring = recommend_adjective(weather)
            springlist = []
            for p_id in spring:
                serializer_spring = get_object_or_404(Perfume,id=p_id)
                springlist.append(PerfumeSerializer(serializer_spring).data)
        elif k == 1:
            summer = recommend_adjective(weather)
            summerlist = []
            for p_id in summer:
                serializer_summer = get_object_or_404(Perfume,id=p_id)
                summerlist.append(PerfumeSerializer(serializer_summer).data)
        elif k == 2:
            autumn = recommend_adjective(weather)
            autumnlist = []
            for p_id in autumn:
                serializer_autumn = get_object_or_404(Perfume,id=p_id)
                autumnlist.append(PerfumeSerializer(serializer_autumn).data)
        
        elif k == 3:
            winter = recommend_adjective(weather)
            winterlist = []
            for p_id in winter:
                serializer_winter = get_object_or_404(Perfume,id=p_id)
                winterlist.append(PerfumeSerializer(serializer_winter).data)
        
    return Response({
        'spring' : springlist,
        'summer' : summerlist,
        'autumn' : autumnlist,
        'winter' : winterlist,
    })

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
    # adjectives = adjectives.split(",")
    for i in range(len(adjectives)):
        for k, v in lines.items():
            if adjectives[i] in v:
                cnt[k] += 1
    # print(cnt)
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
        return [serializer.data[0]["id"]]
    elif se_cnt == 2:
        return [serializer.data[0]["id"], serializer.data[1]["id"]]
    elif se_cnt >= 3:
        tmp = random.sample(range(0, se_cnt), 4)
        c = []
        for i in tmp:
            c.append(serializer.data[i]["id"])
        return c