from .models import Brand
from django.shortcuts import render

# from .forms import PostForm

def brand_list(request):
    items = Brand.objects.all()
    return render(request, 'blog/cafe_brandlist.html',{'items': items})

def menu_list(request):
    items = Brand.objects.all()
    return render(request, 'blog/cafe_menulist.html',{'items': items})