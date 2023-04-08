import psycopg2
from rest_framework import generics, status
from rest_framework.permissions import AllowAny

from .serializer import *
from rest_framework.response import Response
from .models import *


class AAMALLView(generics.GenericAPIView):
    queryset = AAMAll.objects.all()
    permission_classes = [AllowAny]
    # serializer_class = CatsSerializer

    def post(self, request, *args, **kwargs):
        connect = psycopg2.connect(
            host="localhost",
            database="lalafo_db",
            user="lalafouser",
            password="postgres",
            port=5432
        )
        cursor = connect.cursor()

        title = request.data['title']
        description = request.data['description']
        price = request.data['price']
        city = request.data['city']
        cat_id = request.data['cat_id']
        phone = request.data['phone']
        author = request.data['author']

        images = request.data['images']

        # print(title, description, price, city, cat_id, phone, author, images)

        cursor.execute(
                  f"""INSERT INTO listings_aamall ({title}, {description}, {price}, {city}, {cat_id}, {phone}, {author})
                      VALUES ("{title}", "{description}", "{price}", "{city}", "{cat_id}", "{phone}", "{author}");"""
        )

        connect.commit()

        cursor.execute(
            f"""
            SELECT * FROM listings_aamall WHERE title == {title};
            """
        )

        print(cursor.fetchall())



        try:
            cursor.execute(f"INSERT INTO listings_image(cats, photo) VALUES({'cats'}, {'photo'});")
            conne = cursor.fetchall()
            print(conne)
        except:
            pass

        # for k in images:
        #     cursor.execute(f"""INSERT INTO listings_image(cats, photo)
        #                         VALUES ({'cats'}, '{k}');""")

        print('v' * 80, request.data['title'])
        return "OK"
    # queryset = AAMAll.objects.all()
    # serializer_class = AAMALLSerializer
    # permission_classes = [AllowAny]
    #
    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     print(request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         # image = request.FILES.get('images')
    #         object = serializer.save()
    #         # object.photo = image
    #         # object.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)

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

