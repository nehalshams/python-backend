
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.root, name='root'),
    path('dynamic-route/<str:name>/', views.dynamic_route, name='dynamic_route'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
]