from dataclasses import field
from rest_framework import serializers

from product.models import Category as CategoryModel
from product.models import Product as ProductModel
from product.models import Review as ReviewModel
from product.models import ProductOption as ProductOptionModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ["name", ]


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        print(f'obj: {obj}')
        print(f'obj.category {obj.category}')
        return obj.category.name
    class Meta:
        model = ProductModel
        fields = ["user", "thumbnail", "detail", "category",
                  "title", "description", "created", ]

        
        
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ["product", "user", "rating", "content", "created"]
        
        extra_kwargs = {
            "product": {"write_only": True},
        }
                
        
class ProductOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOptionModel
        fields = ["name", "price", ]
        
        
class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    def get_category(self, obj):
        return obj.category.name
    
    options = ProductOptionSerializer(many=True, source="productoption_set")
    reviews = ReviewSerializer(many=True, source="review_set")
    
    class Meta:
        model = ProductModel
        fields = ["name", "thumbnail", "detail", "categorty",
                  "title", "description", "created", "options", "reviews", ]