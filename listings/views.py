from django.shortcuts import render
from rest_framework import generics,status
from .serializer import *
from rest_framework.response import Response
from .models import *


class AAMALLView(generics.ListAPIView):
    queryset = AAMAll.objects.all()
    serializer_class = AAMALLSerializer
    def post(self, request, *args, **kwargs):
        images = request.FILES.getlist('images')
        print(images)
        image_url = request.POST.getlist('image_url')
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            object = serializer.save()
            for image_url in images:
                Image.objects.create(ad_id=object.id, image=image_url)
                print(serializer.errors)
                return Response(serializer.data, status=status.HTTP_200_OK)

class ImageView(generics.GenericAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

