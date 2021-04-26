import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from home.forms import SearchForm
from .models import Product

def index(request):
    products_picked = Product.objects.all().order_by('?')[:4]   #Random selected 4 products
    products_latest = Product.objects.all().order_by('-id')[:4]  # last 4 products
    products_slider = Product.objects.all().order_by('?')[:4]  #first 4 products
    context = {'products_slider': products_slider, 'products_latest': products_latest,'products_picked': products_picked}
    return render(request,'index.html', context)