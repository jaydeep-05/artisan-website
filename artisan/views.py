import re
from unicodedata import name
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView,View
from .models import *

# Create your views here.
# def products(request):
#     context={
#         'items':Item.objects.all()
#     }
#     return render(request,'artisan/product.html',context)

class HomeView(ListView):
    model=Item
    template_name="artisan/home-page.html"

def home(request):
    product=Item.objects.all()
    return render(request,'artisan/home-page.html',{'product':product})

# class ItemDetailView(DetailView):
#     model=Item
#     template_name="artisan/product.html"
# class ProductDetailView(View):
#     def get(self,request,id):
#         product=Item.objects.get(id=id)
#         return render(request,'artisan/product.html',{'product':product})
def productDetail(request, id):
    product=Item.objects.get(id=id)
    return render(request,"artisan/product.html",{'product':product})