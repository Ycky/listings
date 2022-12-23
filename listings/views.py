# from django.shortcuts import render
# from rest_framework import generics,status
# from rest_framework.response import Response
#
# from .serializer import *
# from listings.models import *
#
# class AAMView(generics.ListCreateAPIView):
#     queryset = AAMAll.objects.all()
#     serializer_class = AAMALLSerializer
#
# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class AAMSView(generics.ListCreateAPIView):
#     queryset = AAMAll.objects.all()
#     serializer_class = AAMSerializer
#
#     def post(self, request, *args, **kwargs):
#         images = request.FILES.getlist('images')
#         print(images)
#         image_url = request.POST.getlist('image_url')
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             obj = serializer.save()
#             for img in images:
#                 Image.objects.create(ad_id=obj.id, image=img)
#             print(serializer.errors)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#
# class ImageView(generics.GenericAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         print(serializer.errors)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
