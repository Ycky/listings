# import psycopg2
# from rest_framework import generics, status
# from rest_framework.permissions import AllowAny
#
# from .serializer import *
# from rest_framework.response import Response
# from .models import *
#
#
# class AAMALLView(generics.GenericAPIView):
#     queryset = AAMAll.objects.all()
#     permission_classes = [AllowAny]
#     # serializer_class = AAMALLSerializer
#
#     def post(self, request, *args, **kwargs):
#         connect = psycopg2.connect(
#             host="localhost",
#             database="lalafo_db",
#             user="lalafouser",
#             password="postgres",
#             port=5432
#         )
#         cursor = connect.cursor()
#
#         title = request.data['title']
#         description = request.data['description']
#         price = request.data['price']
#         city = request.data['city']
#         cat_id_id = request.data['cat_id']
#         phone = request.data['phone']
#         author = request.data['author']
#
#         # images = request.data['images']
#         data = {
#             'title': title, 'description': description, 'price': price, 'city': city,
#             'cat_id_id': cat_id_id, 'phone': phone, 'author': author
#         }
#
#         # def snow():
#         #     vi = cursor.execute('select * from listings_aamall').fetchall()
#         #     for v in vi:
#         #         print('vi' * 80, v)
#
#         print('vi'* 80, title, description, price, city, cat_id_id, phone, author, )
#
#         cursor.execute(
#                   f"""INSERT INTO listings_aamall (title, description, price, city, cat_id_id, phone, author)
#                        VALUES (%s, %s, %s, %s, %s, %s, %s);""",(title, description,
#                                                                 price, city, cat_id_id,
#                                                                 phone, author)
#         )
#
#         connect.commit()
#         print('added!' * 80)
#
#         cursor.execute(
#             f"""
#             SELECT * FROM listings_aamall WHERE title == {title};
#             """
#         )
#
#         print(cursor.fetchall())
#         cursor.close()
#         connect.close()
#
# class ImageView(generics.GenericAPIView):
#     queryset = Image.objects.all()
#     serializer_class = ImageSerializer
#
#     def post(self,request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print(serializer.errors)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class CategoryView(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#



# while - пока

# i = 0
# while i < 10:
#     print('hi!')
#     i += 2

from array import *
a = array('i', [1, 2])
print(a)