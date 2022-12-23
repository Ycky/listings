from django.contrib.auth.models import User
from django.db import models



class Category(models.Model):
    category = models.CharField(max_length=234, db_index=True)

    def __str__(self):
        return self.category


class AAMAll(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    city = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    phone = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Image(models.Model):
    adl = models.ForeignKey(AAMAll, on_delete=models.CASCADE, related_name='image')
    photo = models.ImageField(upload_to='image')
    image_url = models.URLField(blank=True, max_length=234, null=True)

    def __str__(self):
        return self.photo



