import psycopg2
from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from .serializer import *
from rest_framework.response import Response
from .models import *


class AAMALLView(generics.GenericAPIView):
    queryset = AAMAll.objects.all()
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # conn = psycopg2.connect(
        #     host="localhost",
        #     database="lalafo_db",
        #     user="lalafouser",
        #     password="postgres",
        #     port=5432
        # )
        # cursor = conn.cursor()
        title = request.data['title']
        description = request.data['description']
        price = request.data['price']
        city = request.data['city']
        cat_id_id = request.data['cat_id']
        phone = request.data['phone']
        author = request.data['author']

        photo = request.data['images']
        listing, created = AAMAll.objects.get_or_create(title=title, description=description, price=price,
                                               city=city, cat_id_id=cat_id_id, phone=phone,
                                               author=author)
        print(listing)
        for p in photo:
            Image.objects.create(photo=p, cats_id=listing.id)
        # print('vi' * 50, title, description, price, city, cat_id_id, phone, author, photo)

        # cursor.execute(
        #           "INSERT INTO listings_aamall (title, description, price, city, cat_id_id, phone, author)"+
        #                "VALUES (%s, %s, %s, %s, %s, %s, %s);",
        #                (title, description, price, city, cat_id_id, phone, author)
        # )
        #
        # cursor.execute("SELECT id FROM listings_aamall WHERE title=title;")
        #
        # ids = cursor.fetchall()
        # print(ids)

        # cursor.execute(
        #     """INSERT INTO listings_image(photo, cats_id)
        #         VALUES (%s, %s);""",
        #                (photo, f"{ids[0]}")
        # )
        #
        # cur = conn.cursor()
        # sql = """INSERT INTO listings_image (photo, cats_id) VALUES (%s, %s)"""
        # for row in ids: # 1343
        #     for j in photo: #5
        #         row_to_insert = (j, row[0])
        #         cur.execute(sql, row_to_insert)
        #
        # conn.commit()
        print('added!' * 80)

class ImageView(generics.GenericAPIView):
    queryset = Image.objects.all()


    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.errors)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

