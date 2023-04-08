from django.contrib import admin
from lalafo .models import *


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    ordering = ('id',)

@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(AAMAll)
