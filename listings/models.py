from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=234, db_index=True)

    def __str__(self):
        return self.category

class Image(models.Model):
    # adl = models.ForeignKey(AAMAll, on_delete=models.CASCADE, related_name='image')
    # photo = models.ImageField(upload_to='image')
    image_url = models.URLField(blank=True, max_length=234, null=True)

    def __str__(self):
        return self.image_url


class AAMAll(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    city = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    thumbnail_url = models.URLField(blank=True, max_length=234, null=True)
    phone = models.CharField(max_length=25)
    author = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



