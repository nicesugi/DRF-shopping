from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from django.contrib.auth import login, logout, authenticate

from user.serializers import UserSerializer
    
    
class UserView(APIView):
    
    def get(self, request):
        return Response({"message": "get 성공"})    
    
    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        
        return Response(user_serializer.data, status=status.HTTP_200_OK) 
    
    def put(self, request):
        return Response({"message": "put 성공"})    
    
    def delete(self, request):
        return Response({"message": "delete 성공"})  
    
    
class UserAPIView(APIView):
    
    def post(self, request):

        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "존재하지 않는 계정이거나 비밀번호가 일치하지 않습니다"},
                            status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({"message": "로그인 성공"})

    def delete(self, request):
        logout(request)
        return Response({"message": "로그아웃 성공"})
    
    
class UserCartView(APIView):
    
    def get(self, request):
        return Response({"message": "get 성공"})    
    
    def post(self, request):
        return Response({"message": "post 성공"})    
