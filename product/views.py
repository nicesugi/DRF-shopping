from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from product.models import Product as ProductModel
from product.serializers import ProductSerializer, ReviewSerializer



class ProductView(APIView):
    
    def get(self, request):
        return Response(ProductSerializer(ProductModel.objects.all(), many=True))
    
    def post(self, request):
        request.data["user"] = request.user.id
        
        product_serializer = ProductSerializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 상품입니다"},
                            status=status.HTTP_400_BAD_REQUEST)
            
        product_serializer = ProductSerializer(product, data=request.data, partial=True)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        
        return Response(product_serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request):
        return Response({"message": "delete 성공"})
    
    
class ProductDetailView(APIView):
    
    def get(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 상품입니다"},
                            status=status.HTTP_400_BAD_REQUEST)
    
    
class ReviewView(APIView):
    
    def post(self, request, product_id):
        try:
            product = ProductModel.objects.get(id=product_id)
        except ProductModel.DoesNotExist:
            return Response({"error": "존재하지 않는 상품입니다"},
                            status=status.HTTP_400_BAD_REQUEST)
        
        request.data["user"] = request.user.id
        request.data["product"] = product.id
        review_serializer = ReviewSerializer(data=request.data)
        review_serializer.is_valid(raise_exception=True)
        review_serializer.save()
        
        return Response(review_serializer.data, status=status.HTTP_200_OK)
        
    def put(self, request, review_id):
        return Response({})
    
    def delete(self, request, review_id):
        return Response({})
    