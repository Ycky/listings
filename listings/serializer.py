from rest_framework import serializers
from listings.models import *

class AAMALLSerializer(serializers.ModelSerializer):
    photos = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='photos'
    )

    class Meta:
        model = AAMAll
        fields = ['title', 'description', 'price', 'city', 'category', 'author', 'phone', 'photos']

    def create(self, validated_data):
        print('v' * 50, validated_data)
        photos_data = validated_data.pop('photos')
        ads = AAMAll.objects.create(**validated_data)
        for photo_data in photos_data:
            Image.objects.create(ads=ads, **photo_data)
        return ads


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

