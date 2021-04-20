from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, request

from home.models import Product
from home.forms import SearchForm

# Create your views here.
def category_products(request,type):
    # catdata = Category.objects.get(pk=id)
    products = Product.objects.filter(type=type) #default language
    # try:
    #     products = Product.objects.raw(
    #         'SELECT p.id,p.price,p.amount,p.image,p.variant,l.title, l.keywords, l.description,l.slug,l.detail '
    #         'FROM product_product as p '
    #         'LEFT JOIN product_productlang as l '
    #         'ON p.id = l.product_id '
    #         'WHERE p.category_id=%s and l.lang=%s', [id])
    # except:
    #     pass
    # catdata = CategoryLang.objects.get(category_id=id, lang=currentlang)

    context={'products': products,
            'productType': type }
             #'category':category,
            #  'catdata':catdata }
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
