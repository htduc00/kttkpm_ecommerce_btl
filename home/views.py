import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Avg, Count, Q, F
from django.db.models.functions import Concat
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request
from django.shortcuts import render
from .models import *
from django import template
from .forms import *
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from django.http import JsonResponse
from django.core.paginator import Paginator
import json
from json import JSONEncoder

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



def product_detail(request,id,name):
    #query = request.GET.get('q')
    #category = Category.objects.all()

    product = Product.objects.get(pk=id)
    images = Hinhanhsanpham.objects.filter(productid_id=id)
    orderDetails = Orderdetail.objects.filter(productid=id)

    damua = False
    for detail in orderDetails:
        if detail.orderid.taikhoanid == request.user:
            damua = True
            break

    productAttributes = Attributevalue.objects.filter(productid=id)
    review_list = Review.objects.filter(productid = id)
    paginator = Paginator(review_list, 4)
    reviews = paginator.page(1)
    comment_list = Productcomment.objects.filter(productid=id);
    commentPaginator = Paginator(comment_list,3)
    comments = commentPaginator.page(1)
    commentReplys = []
    for comment in comments:
        replys = Productcommentreply.objects.filter( productcommentid = comment)
        commentReplys.extend(list(replys))

    productDiscounts = ProductDiscount.objects.filter(productid=id)

    
    context = {
    			'product': product,
                'images': images,
                'comments': comments,
                'reviews' : reviews,
                'commentReplys': commentReplys,
                'damua': damua,
                'discounts': productDiscounts,
               }
    # if productAttribute != None:
    #     if request.method == 'POST': #if we select color
    #         variant_id = request.POST.get('variantid')
    #         variant = Variants.objects.get(id=variant_id) #selected product by click color radio
    #         colors = Variants.objects.filter(product_id=id,size_id=variant.size_id )
    #         sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
    #         query += variant.title+' Size:' +str(variant.size) +' Color:' +str(variant.color)
    #     else:
    #         variants = Variants.objects.filter(product_id=id)
    #         colors = Variants.objects.filter(product_id=id,size_id=variants[0].size_id )
    #         sizes = Variants.objects.raw('SELECT * FROM  product_variants  WHERE product_id=%s GROUP BY size_id',[id])
    #         variant =Variants.objects.get(id=variants[0].id)
    #     context.update({'sizes': sizes, 'colors': colors,
    #                     'variant': variant,'query': query
    #                     })

    if productAttributes != None:
        color_size = productAttributes.filter(attributeid__tenthuoctinh = "color-size")
        colors = []
        sizes = []
        for item in color_size:
            value = item.tenvalue.split("-")
            if value[0] not in colors:
                colors.append(value[0])
            if value[1] not in sizes:
                sizes.append(value[1])
        context.update({'color_size':color_size, 'colors':colors, 'sizes':sizes })
    if request.method == 'GET' and request.is_ajax() == False :
        return render(request,'product_detail.html',context)
    elif request.GET.get('type') == "rv":
        page = request.GET.get('page')
        reviews = paginator.page(int(page))
        review_li = list(reviews.object_list.values('taikhoanid__first_name','taikhoanid__last_name','subject','noidung','rating','createdat'))
        result = {'review_li': review_li}
        return JsonResponse(result)
    elif request.GET.get('type') == "cm":
        page = request.GET.get('page')
        comments = commentPaginator.page(int(page))
        comment_li = list(comments.object_list.values('id','taikhoanid__first_name','taikhoanid__last_name','noidung','createdat'))
        commentReplys = []
        for comment in comments:
            replys = Productcommentreply.objects.filter( productcommentid = comment).values('productcommentid_id','taikhoanid__last_name','taikhoanid__first_name','noidung','createdat')
            commentReplys.extend(list(replys))
        result = {'comment_li': comment_li,
                    'comment_rep': commentReplys}
        return JsonResponse(result)

def addreview(request,id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid() :
            data = Review()
            data.subject = form.cleaned_data['subject']
            data.noidung = form.cleaned_data['noidung']
            data.rating = form.cleaned_data['rating']
            data.productid_id = id
            data.taikhoanid_id = request.user.id
            data.createdat = date.today()
            data.save()
            messages.success(request, "Đánh giá của bạn đã được ghi nhận")
            return HttpResponseRedirect(url)
    return HttpResponseRedirect(url)

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            data = Productcomment()
            data.noidung = form.cleaned_data['noidung']
            data.productid_id = id
            data.taikhoanid_id = request.user.id
            data.createdat = date.today()
            data.save()
            messages.success(request, "Bình luận thành công")
            return HttpResponseRedirect(url)

def addcommentreply(request,id):
    url = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid() :
            data = Productcommentreply()
            data.noidung = form.cleaned_data['noidung']
            data.productcommentid_id = id
            data.taikhoanid_id = request.user.id
            data.createdat = date.today()
            data.save()
            messages.success(request, "Bình luận thành công")
            return HttpResponseRedirect(url)
