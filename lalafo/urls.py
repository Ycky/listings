from django.urls import path
from . import views

urlpatterns = [
    path('mvi/', views.AAMALLView.as_view()),
    path('cvi/', views.CategoryView.as_view()),
    path('ivi/', views.ImageView.as_view())
]

