from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['hovaten', 'gioitinh', 'diachi', 'sodt', 'thethanhvien', 'role'
    , 'image_tag']

class DiscountAdmin(admin.ModelAdmin):
    list_display = ['value', 'hsd', 'requiree']

class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ['user_profile','productid','noidung','createdat']


class ProductCommentReplyAdmin(admin.ModelAdmin):
    list_display = ['productcommentid','user_profile','noidung','createdat']

admin.site.register(Product)
admin.site.register(Tacgia)
admin.site.register(Nhaxuatban)
admin.site.register(Theloaisach)
admin.site.register(Chitiettheloaisach)
admin.site.register(Sachtype)
admin.site.register(Review)
admin.site.register(Thethanhvien)
admin.site.register(Role)
admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Hinhanhsanpham)
admin.site.register(Productcomment,ProductCommentAdmin)
admin.site.register(Productcommentreply,ProductCommentReplyAdmin)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Paymentmethod)
admin.site.register(Donvivanchuyen)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(ProductDiscount)
admin.site.register(Attribute)
admin.site.register(Attributevalue)
