from django.shortcuts import render,get_object_or_404
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def review_list(request,user_id):
    review_list = Review.objects.filter(user_id=user_id)
    serializer = ReviewSerializer(review_list,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def review_detail(request, review_id):
    review = get_object_or_404(Review,id=review_id)
    serializer = ReviewSerializer(review)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create_review(request):
    serializer=ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['POST'])
def update_review(request,review_id):
    review = get_object_or_404(Review,id=review_id)
    serializer = ReviewSerializer(data=request.data,instance=review)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response()

@api_view(['DELETE'])
def delete_review(request,review_id):
    review=get_object_or_404(Review,id=review_id)
    review.delete()
    return Response()
