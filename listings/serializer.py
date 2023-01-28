from rest_framework import serializers
from listings.models import *

class AAMALLSerializer(serializers.ModelSerializer):
    class Meta:
        model = AAMAll
        fields = ['title', 'description', 'price', 'city', 'category', 'author', 'photo', 'phone']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image_url']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']


# class AAMALLSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AAMAll
#
#
# class AAMSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AAMAll
#         fields = ('user', 'title', 'description', 'price', 'city', 'category', 'phone', 'created')
#
#
#     def create(self, validated_data):
#         category = validated_data.pop('category')
#         aam = AAMAll.objects.create(category=category, **validated_data)
#         return aam
#
# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ('adl', 'photo', 'image_url')
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('category')
#
#
