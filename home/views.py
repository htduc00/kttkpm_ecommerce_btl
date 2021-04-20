from django.shortcuts import render
from .models import Product

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

    context={'products': products}
             #'category':category,
            #  'catdata':catdata }
    return render(request,'category_products.html',context)
