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

def product_detail(request,id,name):
    #query = request.GET.get('q')
    #category = Category.objects.all()

    product = Product.objects.get(pk=id)

    images = Hinhanhsanpham.objects.filter(productid_id=id)
    comments = Productcomment.objects.filter(productid_id=id)
    commentReplys = Productcommentreply.objects.all()
    orderDetails = Orderdetail.objects.filter(productid=id)

    damua = False
    for detail in orderDetails:
        if detail.orderid.taikhoanid == request.user:
            damua = True
            break

    productAttribute = Attributevalue.objects.filter(productid=id)

    review_list = Review.objects.filter(productid = id)
    paginator = Paginator(review_list, 4)
    reviews = paginator.page(1)
    context = {
    			'product': product,
                'images': images,
                'comments': comments,
                'reviews' : reviews,
                'commentReplys': commentReplys,
                'damua': damua
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
    if request.method == 'GET' and request.is_ajax() == False :
        return render(request,'product_detail.html',context)
    else:
        page = request.GET.get('page')
        reviews = paginator.page(int(page))
        review_li = list(reviews.object_list.values('taikhoanid__first_name','taikhoanid__last_name','subject','noidung','rating','createdat'))
        result = {'review_li': review_li}
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