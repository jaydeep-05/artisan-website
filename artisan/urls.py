from django import views
from django.contrib import admin
from django.urls import path

from .views import (
    HomeView,
    # ProductDetailView,
    productDetail,
    home,
)
app_name="artisan"

urlpatterns=[
    path('',home,name='home'),
    path('product/<int:id>',productDetail,name='product'),
    
]