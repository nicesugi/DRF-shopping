from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response



class ProductView(APIView):
    
    def get(self, request):
        return Response({"message": "get 성공"})
    def post(self, request):
        return Response({"message": "post 성공"})
    def put(self, request):
        return Response({"message": "put 성공"})
    def delete(self, request):
        return Response({"message": "delete 성공"})
    