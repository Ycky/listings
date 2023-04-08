from rest_framework import serializers
from lalafo.models import *


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

class AAMALLSerializer(serializers.ModelSerializer):
    photo = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='photo'
    )

    class Meta:
        model = AAMAll
        fields = '__all__'

    def create(self, validated_data):
        print('sss' * 50, validated_data)
        photos_data = validated_data.pop('photo')
        ads = AAMAll.objects.create(**validated_data)
        for photo_data in photos_data:
            Image.objects.create(ads=ads, **photo_data)
        return ads

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

