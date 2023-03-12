from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=234, db_index=True)

    def __str__(self):
        return self.category


class AAMAll(models.Model):
    title = models.CharField(max_length=250, db_index=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    city = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_url = models.URLField(blank=True, max_length=234, null=True)
    phone = models.CharField(max_length=25)
    author = models.CharField(max_length=200)
    # post = models.ForeignKey('Image', default=None, on_delete=models.CASCADE)
    # photo = models.FileField(upload_to='photo_data')
    # photo = models.URLField(blank=True, max_length=234, null=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    photo = models.FileField(blank=True)


