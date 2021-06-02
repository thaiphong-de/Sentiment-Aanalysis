from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from .models import Review
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import os
from rest_framework import generics, permissions, mixins, status
from django.db.models import Count
from django.http import HttpResponse
from django.http import JsonResponse


# Định nghĩa model cần serialize và các trường. ở đây mình để là all.
# Có rất nhiều API class mà rest đã viết sẵn. ở đây mình chỉ dùng 2 class để thao tác CRUD với database. 
class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


# API get detail, update, delete
class ReviewDetailUpdateAPIView(viewsets.GenericViewSet,
                              RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewListSerializer
    lookup_field = 'ReviewId'
    # permission_classes = [IsAuthenticated]
class ReviewIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['ReviewId']


# API get detail, update, delete
@api_view(['GET', 'POST'])
def get_reviewId(request):
    if request.method == 'GET':
        settings = Review.objects.all()
        serializer = ReviewIDSerializer(settings, many=True)
        return Response(serializer.data)

class AspectView(generics.GenericAPIView):
    serializer_class = ReviewIDSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        result = {}
        reviewid = (request.data['ReviewId'])
        # user = Review.objects.get(ReviewId=email)
        with open("C:/Users/Thai Phong/Desktop/Sentiment Analysis/LARA_BootStrap/modelData/summary.json", 'r') as j: 
            json_data = json.load(j)
            for i in range(len(json_data)):
                if json_data[i]["ReviewID"]==reviewid:
                    result=json_data[i]["aspect"]   
                    # import pdb
                    # pdb.set_trace()
                    return Response(result)  

            return Response({"aspect":"None"}, status=status.HTTP_204_NO_CONTENT)


class ContentView(generics.GenericAPIView):
    serializer_class = ReviewIDSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        result = {}
        reviewid = (request.data['ReviewId'])
        # user = Review.objects.get(ReviewId=email)
        path_to_json = 'C:/Users/Thai Phong/Desktop/Sentiment Analysis/LARA_BootStrap/hotelReviews/'
        json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
        for index, js in enumerate(json_files):
            with open(os.path.join(path_to_json, js)) as json_file:
                json_text = json.load(json_file)
                for i in range(len(json_text["Reviews"])):
                    if json_text["Reviews"][i]["ReviewID"]==reviewid:
                        result=json_text["Reviews"][i]["Content"]
                        return Response(result)  

                return Response({"aspect":"None"}, status=status.HTTP_204_NO_CONTENT)


class CountSerializer(serializers.Serializer):
    class Meta:
        fields = ['Result', 'Count']

@api_view(['GET', 'POST'])
def count_result(request):
    if request.method == 'GET':
        result = Review.objects.values("Result").annotate(num_books=Count('Result'))
        # qs_json = serializers.serialize('json', result)
        return HttpResponse(result, content_type='application/json')

