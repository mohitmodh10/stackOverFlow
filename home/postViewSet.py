from django.shortcuts import render
from home.commonResponse import generateCommonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import response
from rest_framework.serializers import Serializer
from .serializers import PostSerializer
from .models import MyPost,UserModel
from rest_framework import viewsets


class postViewSet(viewsets.ModelViewSet):
    @api_view(['POST'])
    def addPost(request):
        s = PostSerializer(data = request.data)
        print(request.data['author'])
        if s.is_valid():
            s.save()
            data = generateCommonResponse(1,"post added successfully",s.data)
            return response.JsonResponse(data)
        else:
            data = generateCommonResponse(0,"all fileds are required",s.data)
            return response.JsonResponse(data)
    
    @api_view(['POST'])
    def addVote(request):
        post = MyPost.objects.get(id=str(request.data['id']))
        user = UserModel.objects.get(id=str(request.data["userId"]))
        if user in post.vote.all():
            vote = False
            post.vote.remove(user)
        else:
            vote = True
            post.vote.add(user)
        customData = {
            "Vote":vote
        }
        data = generateCommonResponse(1,"Vote updated successfully",customData)
        return response.JsonResponse(data)



