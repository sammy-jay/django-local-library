from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.index),
    path('authors/', views.index),
    path('books/<int:id>/', views.index, name='book-detail'),
    path('authors/<int:id>/', views.index, name='author-detail'),
]
