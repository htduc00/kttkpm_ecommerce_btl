from django.contrib import admin
from .models import *
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['hovaten', 'gioitinh', 'diachi', 'sodt', 'thethanhvien', 'role','image_tag']


admin.site.register(Product)
admin.site.register(Tacgia)
admin.site.register(Nhaxuatban)
admin.site.register(Theloaisach)
admin.site.register(Chitiettheloaisach)
admin.site.register(Sachtype)
admin.site.register(Review)
admin.site.register(Thethanhvien)
admin.site.register(Role)
admin.site.register(UserProfile,UserProfileAdmin)

admin.site.register(Hinhanhsanpham)
admin.site.register(Productcomment)
admin.site.register(Productcommentreply)
admin.site.register(Order)
admin.site.register(Orderdetail)
admin.site.register(Payment)
admin.site.register(Shipment)
admin.site.register(Paymentmethod)
admin.site.register(Donvivanchuyen)
