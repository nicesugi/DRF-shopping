from dataclasses import field
from rest_framework import serializers

from user.models import User as UserModel
from user.models import Cart as CartModel



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password", "fullname", "phone",
                  "cart", "keep", ]
        
        read_only_fields = ["cart", "keep", ]
        extra_kwargs = {
            "password": {"write_only": True}
        }
        
    def create(self, validated_data):
        password = validated_data.pop("password", "")
        user = UserModel(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class UserCartSerializer(serializers.ModelSerializer):
    product_option_id = serializers.IntegerField(write_only=True)
    product_info = serializers.SerializerMethodField(read_only=True)
    
    def get_product_info(self, obj):
        return obj.product_option.product.title
    
    product_option_info = serializers.SerializerMethodField(read_only=True)
    def get_product_option_info(self, obj):
        return obj.product_option_name
    
    price = serializers.SerializerMethodField(read_only=True)
    sum_price = serializers.SerializerMethodField(read_only=True)
    def get_price(self, obj):
        return obj.product_option.price
    
    def get_sum_price(self, obj):
        return obj.product_option.price * obj.count
    
    
    class Meta:
        model = CartModel
        fields = ["user", "count", 
                  "product_option_id", "product_info", "product_option_info", 
                  "price", "sum_price", ]
        
        extra_kwargs = {
            "user": {"write_only": True},
        }