from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Product)
admin.site.register(Hinhanhsanpham)
admin.site.register(Review)
admin.site.register(Productcomment)
admin.site.register(Productcommentreply)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Paymentmethod)
admin.site.register(Donvivanchuyen)