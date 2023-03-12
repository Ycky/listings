from django.contrib import admin
from .models import *


# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')
    ordering = ('id',)

@admin.register(Image)
class PostImageAdmin(admin.ModelAdmin):
    pass
# admin.site.register(Image)


admin.site.register(AAMAll)
