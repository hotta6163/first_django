from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('author/', views.post_author, name='post_author'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
