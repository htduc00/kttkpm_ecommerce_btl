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
from datetime import date
from django.core.paginator import Paginator
import json
from json import JSONEncoder

from django.urls import reverse
# Create your views here.

def index(request):
    products_picked = Product.objects.all().order_by('?')[:4]   #Random selected 4 products
    products_latest = Product.objects.all().order_by('-id')[:4]  # last 4 products
    products_slider = Product.objects.all().order_by('?')[:4]  #first 4 products
    context = {'products_slider': products_slider, 'products_latest': products_latest,'products_picked': products_picked}
    return render(request,'index.html', context)



def product_detail(request,id,slug):
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

    #Review Paging
    review_list = Review.objects.filter(productid = id)
    paginator = Paginator(review_list, 4)
    reviews = paginator.page(1)

    #Comment Paging
    comment_list = Productcomment.objects.filter(productid = id)
    commentPaginator = Paginator(comment_list, 3)
    comments = commentPaginator.page(1)
    commentReplys = []

    for comment in comments:
        replys = Productcommentreply.objects.filter(productcommentid = comment)
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
    productAttributes = Attributevalue.objects.filter(productid=id)
    if productAttributes != None:
        colors = []
        sizes = []
        color_size = productAttributes.filter(attributeid__tenthuoctinh = "color-size")
        colorAttribute = productAttributes.filter(attributeid__tenthuoctinh = "color")
        sizeAttribute = productAttributes.filter(attributeid__tenthuoctinh = "size")
        if(color_size):
            for item in color_size:
                value = item.tenvalue.split("-")
                if value[0] not in colors:
                    colors.append(value[0])
                if value[1] not in sizes:
                    sizes.append(value[1])
        else:
                for item in colorAttribute:
                    colors.append(item.tenvalue)
                for item in sizeAttribute:
                    sizes.append(item.tenvalue)
        print(colors)
        print(sizes)
        context.update({'color_size':list(color_size.values()),'colorAttribute':list(colorAttribute.values()),'sizeAttribute':list(sizeAttribute.values()), 'colors':colors, 'sizes':sizes })
    if request.method == 'GET' and request.is_ajax() == False :
        return render(request,'product_detail.html',context)
    elif request.GET.get('type') == "rv":
        page = request.GET.get('page')
        reviews = paginator.page(int(page))
        review_li = list(reviews.object_list.values('user_profile__first_name','user_profile__last_name','subject','noidung','rating','createdat'))
        result = {'review_li': review_li}
        return JsonResponse(result)
    elif request.GET.get('type') == "cm":
        page = request.GET.get('page')
        comments = commentPaginator.page(int(page))
        comment_li = list(comments.object_list.values('id','user_profile__hovaten','noidung','createdat','user_profile__image'))
        commentReplys = []
        for comment in comments:
            replys = Productcommentreply.objects.filter( productcommentid = comment).values('productcommentid_id','user_profile__hovaten','noidung','createdat','user_profile__image')
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
            data.user_profile= UserProfile.objects.get(user_id = request.user.id)
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
            data.user_profile = UserProfile.objects.get(user_id = request.user.id)
            data.createdat = date.today()
            data.save()
            messages.success(request, "Bình luận thành công")
            return HttpResponseRedirect(url)


def category_products(request, type, theloai):
    try:
        if type == 'book':
            products = Product.objects.raw(
                'SELECT * '
                'FROM product as p '
                'LEFT JOIN sachtype s on p.id = s.ProductID '
                'WHERE s.TheLoaiSachID = %s', [theloai])
        elif type == 'electro':
            products = Product.objects.raw(
                'SELECT * '
                'FROM product as p '
                'LEFT JOIN dientutype d on p.id = d.ProductID '
                'WHERE d.ChiTietTheLoaiDienTuID = %s', [theloai])
        elif type == 'aoquan':
            products = Product.objects.raw(
                'SELECT * '
                'FROM product as p '
                'LEFT JOIN aoquan a on p.id = a.ProductID '
                'WHERE a.TheLoaiQuanAoID = %s', [theloai])
        else:
            products = None
    except:
        pass
    # try:
    #     products = Product.objects.raw(
    #         'SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
    #         'FROM product_product as p '
    #         'LEFT JOIN product_productlang as l '
    #         'ON p.id = l.product_id '
    #         'WHERE p.category_id=%s and l.lang=%s', [id])
    # except:
    #     pass

    context={'products': products,
            'productType': type }

    return render(request,'category_products.html',context)


def search(request):
    if request.method == 'POST': # check post
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query'] # get form input data
            type = form.cleaned_data['type']
            if type=='0':
                products = Product.objects.filter(ten__icontains=query)  #SELECT * FROM product WHERE title LIKE '%query%'
            else:
                products = Product.objects.filter(ten__icontains=query,type=type)
            # category = Category.objects.all()
            context = {'products': products, 'query':query }
                      #  'category': category }
            
            return render(request, 'search_products.html', context)

    return HttpResponseRedirect('/')
