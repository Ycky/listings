from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from .serializer import *
from rest_framework.response import Response
from .models import *


class AAMALLView(generics.GenericAPIView):
    queryset = AAMAll.objects.all()
    serializer_class = AAMALLSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        print(request.data)
        if serializer.is_valid(raise_exception=True):
            # image = request.FILES.get('images')
            object = serializer.save()
            # object.photo = image
            # object.save()
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

