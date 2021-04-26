# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.db.models import Avg, Count
from django.contrib.auth.models import User
import json

class Aoquan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    thuonghieuquanaoid = models.ForeignKey('Thuonghieuquanao', models.DO_NOTHING, db_column='ThuongHieuQuanAoID')  # Field name made lowercase.
    theloaiquanaoid = models.ForeignKey('Theloaiquanao', models.DO_NOTHING, db_column='TheLoaiQuanAoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aoquan'


class AoquanChitiettheloaiquanao(models.Model):
    aoquanid = models.ForeignKey(Aoquan, models.DO_NOTHING, db_column='AoQuanID')  # Field name made lowercase.
    chitiettheloaiquanaoid = models.ForeignKey('Chitiettheloaiquanao', models.DO_NOTHING, db_column='ChiTietTheLoaiQuanAoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'aoquan_chitiettheloaiquanao'


class Attribute(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenthuoctinh = models.CharField(db_column='TenThuocTinh', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attribute'


class Attributevalue(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    attributeid = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='AttributeID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    tenvalue = models.CharField(db_column='TenValue', max_length=255, blank=True, null=True)  # Field name made lowercase.
    soluongsanphamconlai = models.IntegerField(db_column='SoLuongSanPhamConLai')  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'attributevalue'


class Cart(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong')  # Field name made lowercase.
    sotien = models.FloatField(db_column='SoTien')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cart'


class Chitietnhaphang(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    attributevalueid = models.ForeignKey(Attributevalue, models.DO_NOTHING, db_column='AttributeValueID')  # Field name made lowercase.
    nhaphangid = models.ForeignKey('Nhaphang', models.DO_NOTHING, db_column='NhapHangID')  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong')  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chitietnhaphang'


class Chitiettheloaidientu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theloaidientuid = models.ForeignKey('Theloaidientu', models.DO_NOTHING, db_column='TheLoaiDienTuID')  # Field name made lowercase.
    tenchitiettheloaidientu = models.CharField(db_column='TenChiTietTheLoaiDienTu', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chitiettheloaidientu'


class Chitiettheloaiquanao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenchitiet = models.CharField(db_column='TenChiTiet', max_length=255, blank=True, null=True)  # Field name made lowercase.
    theloaiquanaoid = models.ForeignKey('Theloaiquanao', models.DO_NOTHING, db_column='TheLoaiQuanAoID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chitiettheloaiquanao'


class Chitiettheloaisach(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    theloaisachid = models.ForeignKey('Theloaisach', models.DO_NOTHING, db_column='TheLoaiSachID')  # Field name made lowercase.
    tenchitiettheloaisach = models.CharField(db_column='TenChiTietTheLoaiSach', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'chitiettheloaisach'


class Color(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=255)  # Field name made lowercase.
    mamau = models.CharField(db_column='MaMau', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'color'


class Conversation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    taikhoankhachid = models.OneToOneField('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanKhachID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'conversation'


class Dientutype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    thuonghieuid = models.ForeignKey('Thuonghieu', models.DO_NOTHING, db_column='ThuongHieuID')  # Field name made lowercase.
    chitiettheloaidientuid = models.OneToOneField(Chitiettheloaidientu, models.DO_NOTHING, db_column='ChiTietTheLoaiDienTuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dientutype'


class Discount(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hsd = models.DateField(db_column='Hsd')  # Field name made lowercase.
    value = models.IntegerField(db_column='Value')  # Field name made lowercase.
    requiree = models.FloatField(db_column='Requiree')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'discount'


class Donvivanchuyen(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tendonvivanchuyen = models.CharField(db_column='TenDonViVanChuyen', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'donvivanchuyen'


class Hinhanhreview(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reviewid = models.ForeignKey('Review', models.DO_NOTHING, db_column='ReviewID')  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hinhanhreview'


class Hinhanhsanpham(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    urlimage = models.ImageField(db_column='UrlImage', blank=True, null=True)  # Field name made lowercase.
    tenanh = models.CharField(db_column='TenAnh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hinhanhsanpham'


class Khachhang(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hovaten = models.CharField(db_column='HoVaTen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.CharField(db_column='GioiTinh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sodt = models.CharField(db_column='SoDT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thethanhvienid = models.ForeignKey('Thethanhvien', models.DO_NOTHING, db_column='TheThanhVienID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'khachhang'


class Loaidiachi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    loai = models.CharField(db_column='Loai', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'loaidiachi'


class Message(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    conversationid = models.ForeignKey(Conversation, models.DO_NOTHING, db_column='ConversationID')  # Field name made lowercase.
    noidung = models.CharField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    isreadbykhach = models.TextField(db_column='IsReadByKhach', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    isreadbynhanvien = models.TextField(db_column='IsReadByNhanVien')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'message'


class Messageimage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    messageid = models.ForeignKey(Message, models.DO_NOTHING, db_column='MessageID')  # Field name made lowercase.
    url = models.CharField(db_column='Url', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'messageimage'


class Nhanvien(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    hovaten = models.CharField(db_column='HoVaTen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ngaysinh = models.DateField(db_column='NgaySinh', blank=True, null=True)  # Field name made lowercase.
    gioitinh = models.CharField(db_column='GioiTinh', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sodt = models.CharField(db_column='SoDT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isworking = models.TextField(db_column='IsWorking')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'nhanvien'


class Nhanxetreview(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nhanvienid = models.ForeignKey(Nhanvien, models.DO_NOTHING, db_column='NhanVienID')  # Field name made lowercase.
    noidung = models.CharField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    reviewid = models.ForeignKey('Review', models.DO_NOTHING, db_column='ReviewID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhanxetreview'


class Nhaphang(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nhanvienid = models.ForeignKey(Nhanvien, models.DO_NOTHING, db_column='NhanVienID')  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhaphang'


class Nhaxuatban(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tennhaxuatban = models.CharField(db_column='TenNhaXuatBan', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'nhaxuatban'


class Notification(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    noidung = models.CharField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    isopened = models.TextField(db_column='IsOpened')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'notification'


class Order(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey(User, models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    tongtien = models.FloatField(db_column='TongTien')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    shipmentid = models.OneToOneField('Shipment', models.DO_NOTHING, db_column='ShipmentID')  # Field name made lowercase.
    paymentid = models.OneToOneField('Payment', models.DO_NOTHING, db_column='PaymentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderdetail(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    orderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong')  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetail'


class Payment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sothe = models.CharField(db_column='SoThe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tenchuthe = models.CharField(db_column='TenChuThe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ngayphathanh = models.DateField(db_column='NgayPhatHanh', blank=True, null=True)  # Field name made lowercase.
    ngayhethan = models.DateField(db_column='NgayHetHan', blank=True, null=True)  # Field name made lowercase.
    paymentmethodid = models.ForeignKey('Paymentmethod', models.DO_NOTHING, db_column='PaymentMethodID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Paymentmethod(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenpthuc = models.CharField(db_column='TenPThuc', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentmethod'


class Phuong(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    quanid = models.ForeignKey('Quan', models.DO_NOTHING, db_column='QuanID')  # Field name made lowercase.
    tenphuong = models.CharField(db_column='TenPhuong', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'phuong'


class Product(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ten = models.CharField(db_column='Ten', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mota = models.TextField(db_column='MoTa', max_length=255, blank=True, null=True)  # Field name made lowercase.
    danhgia = models.IntegerField(db_column='DanhGia')  # Field name made lowercase.
    gia = models.FloatField(db_column='Gia')  # Field name made lowercase.
    chitietsp = models.CharField(db_column='ChiTietSP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    hinhanh = models.ImageField(db_column='HinhAnh', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product'
    @property
    def imageURL(self):
        try:
            url = self.hinhanh.url
        except:
            url = ''
        return url
    def avaregereview(self):
        review = Review.objects.filter(productid=self.id).aggregate(avarage=Avg('rating'))
        avg = 0
        if review["avarage"] is not None:
            avg=float(review["avarage"])
        return avg
    def countreview(self):
        review = Review.objects.filter(productid=self.id).aggregate(count=Count('id'))
        count = 0
        if review["count"] is not None:
            count = int(review["count"])
        return count

class ProductDiscount(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    discountid = models.ForeignKey(Discount, models.DO_NOTHING, db_column='DiscountID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'product_discount'


class Productcomment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey(User, models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    noidung = models.CharField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcomment'


class Productcommentreply(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey(User, models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productcommentid = models.ForeignKey(Productcomment, models.DO_NOTHING, db_column='ProductCommentID')  # Field name made lowercase.
    noidung = models.CharField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcommentreply'

class Productcommentreplyreaction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey(User, models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productcommentreplyid = models.ForeignKey(Productcommentreply, models.DO_NOTHING, db_column ='ProductCommentReplyID')  # Field name made lowercase.
    reaction = models.CharField(db_column='Reaction', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcommentreplyreaction'


class Productview(models.Model):
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productview'


class Quan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    thanhphoid = models.ForeignKey('Thanhpho', models.DO_NOTHING, db_column='ThanhPhoID')  # Field name made lowercase.
    tenquan = models.CharField(db_column='TenQuan', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quan'


class Review(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey(User, models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    subject = models.TextField(db_column="Subject", max_length=255, blank=True, null  =True)
    noidung = models.TextField(db_column='NoiDung', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.
    createdat = models.DateField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'


class Role(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.TextField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'role'


class Sachtype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    nhaxuatbanid = models.ForeignKey(Nhaxuatban, models.DO_NOTHING, db_column='NhaXuatBanID')  # Field name made lowercase.
    tacgiaid = models.ForeignKey('Tacgia', models.DO_NOTHING, db_column='TacGiaID')  # Field name made lowercase.
    theloaisachid = models.ForeignKey('Theloaisach', models.DO_NOTHING, db_column='TheLoaiSachID')  # Field name made lowercase.
    namxb = models.IntegerField(db_column='NamXB')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sachtype'


class SachtypeChitiettheloaisach(models.Model):
    sachtypeid = models.ForeignKey(Sachtype, models.DO_NOTHING, db_column='SachTypeID')  # Field name made lowercase.
    chitiettheloaisachid = models.ForeignKey(Chitiettheloaisach, models.DO_NOTHING, db_column='ChiTietTheLoaiSachID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sachtype_chitiettheloaisach'


class Sanphamdaxem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sanphamdaxem'


class Sanphammuasau(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sanphammuasau'


class Sanphamyeuthich(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID')  # Field name made lowercase.
    taikhoanid = models.ForeignKey('Taikhoan', models.DO_NOTHING, db_column='TaiKhoanID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sanphamyeuthich'


class Shipment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    donvivanchuyenid = models.ForeignKey(Donvivanchuyen, models.DO_NOTHING, db_column='DonViVanChuyenID')  # Field name made lowercase.
    giaship = models.FloatField(db_column='GiaShip')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'shipment'


class Tacgia(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tentacgia = models.CharField(db_column='TenTacGia', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tacgia'


class Taikhoan(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255, blank=True, null=True)  # Field name made lowercase.
    role = models.IntegerField(db_column='Role', blank=True, null=True)  # Field name made lowercase.
    createdtime = models.DateField(db_column='CreatedTime', blank=True, null=True)  # Field name made lowercase.
    isdeleted = models.TextField(db_column='IsDeleted')  # Field name made lowercase. This field type is a guess.
    nhanvienid = models.OneToOneField(Nhanvien, models.DO_NOTHING, db_column='NhanVienID')  # Field name made lowercase.
    khachhangid = models.OneToOneField(Khachhang, models.DO_NOTHING, db_column='KhachHangID')  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='RoleID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taikhoan'


class Thanhpho(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenthanhpho = models.CharField(db_column='TenThanhPho', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thanhpho'


class Theloaidientu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tentheloai = models.CharField(db_column='TenTheLoai', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theloaidientu'


class Theloaiquanao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tentheloai = models.CharField(db_column='TenTheLoai', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theloaiquanao'


class Theloaisach(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tentheloai = models.CharField(db_column='TenTheLoai', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'theloaisach'


class Thethanhvien(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sothe = models.CharField(db_column='SoThe', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diemtichluy = models.IntegerField(db_column='DiemTichLuy', blank=True, null=True)  # Field name made lowercase.
    loaithe = models.CharField(db_column='LoaiThe', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thethanhvien'


class Thongtingiaohang(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    khachhangid = models.ForeignKey(Khachhang, models.DO_NOTHING, db_column='KhachHangID')  # Field name made lowercase.
    hoten = models.CharField(db_column='HoTen', max_length=255, blank=True, null=True)  # Field name made lowercase.
    diachi = models.CharField(db_column='DiaChi', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sodt = models.CharField(db_column='SoDT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    macdinh = models.TextField(db_column='MacDinh')  # Field name made lowercase. This field type is a guess.
    thanhphoid = models.ForeignKey(Thanhpho, models.DO_NOTHING, db_column='ThanhPhoID')  # Field name made lowercase.
    quanid = models.ForeignKey(Quan, models.DO_NOTHING, db_column='QuanID')  # Field name made lowercase.
    phuongid = models.ForeignKey(Phuong, models.DO_NOTHING, db_column='PhuongID')  # Field name made lowercase.
    loaidiachiid = models.ForeignKey(Loaidiachi, models.DO_NOTHING, db_column='LoaiDiaChiID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thongtingiaohang'


class Thuonghieu(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenthuonghieu = models.CharField(db_column='TenThuongHieu', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thuonghieu'


class Thuonghieuquanao(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    tenthuonghieu = models.CharField(db_column='TenThuongHieu', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'thuonghieuquanao'
