# Generated by Django 3.1.7 on 2021-04-19 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aoquan',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'aoquan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AoquanChitiettheloaiquanao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'aoquan_chitiettheloaiquanao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenthuoctinh', models.CharField(blank=True, db_column='TenThuocTinh', max_length=255, null=True)),
            ],
            options={
                'db_table': 'attribute',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Attributevalue',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=255, primary_key=True, serialize=False)),
                ('tenvalue', models.CharField(blank=True, db_column='TenValue', max_length=255, null=True)),
                ('soluongsanphamconlai', models.IntegerField(db_column='SoLuongSanPhamConLai')),
                ('gia', models.FloatField(db_column='Gia')),
            ],
            options={
                'db_table': 'attributevalue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('soluong', models.IntegerField(db_column='SoLuong')),
                ('sotien', models.FloatField(db_column='SoTien')),
            ],
            options={
                'db_table': 'cart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitietnhaphang',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('soluong', models.IntegerField(db_column='SoLuong')),
                ('gia', models.FloatField(db_column='Gia')),
            ],
            options={
                'db_table': 'chitietnhaphang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitiettheloaidientu',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenchitiettheloaidientu', models.CharField(blank=True, db_column='TenChiTietTheLoaiDienTu', max_length=255, null=True)),
            ],
            options={
                'db_table': 'chitiettheloaidientu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitiettheloaiquanao',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenchitiet', models.CharField(blank=True, db_column='TenChiTiet', max_length=255, null=True)),
            ],
            options={
                'db_table': 'chitiettheloaiquanao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chitiettheloaisach',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenchitiettheloaisach', models.CharField(blank=True, db_column='TenChiTietTheLoaiSach', max_length=255, null=True)),
            ],
            options={
                'db_table': 'chitiettheloaisach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.CharField(db_column='ID', max_length=255, primary_key=True, serialize=False)),
                ('mamau', models.CharField(blank=True, db_column='MaMau', max_length=255, null=True)),
            ],
            options={
                'db_table': 'color',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'conversation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dientutype',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'dientutype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hsd', models.DateField(db_column='Hsd')),
                ('value', models.FloatField(db_column='Value')),
                ('requiree', models.FloatField(db_column='Requiree')),
            ],
            options={
                'db_table': 'discount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Donvivanchuyen',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tendonvivanchuyen', models.CharField(blank=True, db_column='TenDonViVanChuyen', max_length=255, null=True)),
            ],
            options={
                'db_table': 'donvivanchuyen',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hinhanhreview',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, db_column='Url', max_length=255, null=True)),
            ],
            options={
                'db_table': 'hinhanhreview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Hinhanhsanpham',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('urlimage', models.CharField(blank=True, db_column='UrlImage', max_length=255, null=True)),
                ('tenanh', models.CharField(blank=True, db_column='TenAnh', max_length=255, null=True)),
            ],
            options={
                'db_table': 'hinhanhsanpham',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Khachhang',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hovaten', models.CharField(blank=True, db_column='HoVaTen', max_length=255, null=True)),
                ('ngaysinh', models.DateField(blank=True, db_column='NgaySinh', null=True)),
                ('gioitinh', models.CharField(blank=True, db_column='GioiTinh', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('diachi', models.CharField(blank=True, db_column='DiaChi', max_length=255, null=True)),
                ('sodt', models.CharField(blank=True, db_column='SoDT', max_length=255, null=True)),
            ],
            options={
                'db_table': 'khachhang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Loaidiachi',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('loai', models.CharField(blank=True, db_column='Loai', max_length=255, null=True)),
            ],
            options={
                'db_table': 'loaidiachi',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
                ('isreadbykhach', models.TextField(blank=True, db_column='IsReadByKhach', null=True)),
                ('isreadbynhanvien', models.TextField(db_column='IsReadByNhanVien')),
            ],
            options={
                'db_table': 'message',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Messageimage',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('url', models.CharField(blank=True, db_column='Url', max_length=255, null=True)),
            ],
            options={
                'db_table': 'messageimage',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nhanvien',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hovaten', models.CharField(blank=True, db_column='HoVaTen', max_length=255, null=True)),
                ('ngaysinh', models.DateField(blank=True, db_column='NgaySinh', null=True)),
                ('gioitinh', models.CharField(blank=True, db_column='GioiTinh', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='Email', max_length=255, null=True)),
                ('sodt', models.CharField(blank=True, db_column='SoDT', max_length=255, null=True)),
                ('diachi', models.CharField(blank=True, db_column='DiaChi', max_length=255, null=True)),
                ('isworking', models.TextField(db_column='IsWorking')),
            ],
            options={
                'db_table': 'nhanvien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nhanxetreview',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'nhanxetreview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nhaphang',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'nhaphang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nhaxuatban',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tennhaxuatban', models.CharField(blank=True, db_column='TenNhaXuatBan', max_length=255, null=True)),
            ],
            options={
                'db_table': 'nhaxuatban',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
                ('isopened', models.TextField(db_column='IsOpened')),
            ],
            options={
                'db_table': 'notification',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tongtien', models.FloatField(db_column='TongTien')),
                ('status', models.CharField(blank=True, db_column='Status', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'order',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Orderdetail',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('soluong', models.IntegerField(db_column='SoLuong')),
                ('gia', models.FloatField(db_column='Gia')),
            ],
            options={
                'db_table': 'orderdetail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sothe', models.CharField(blank=True, db_column='SoThe', max_length=255, null=True)),
                ('tenchuthe', models.CharField(blank=True, db_column='TenChuThe', max_length=255, null=True)),
                ('ngayphathanh', models.DateField(blank=True, db_column='NgayPhatHanh', null=True)),
                ('ngayhethan', models.DateField(blank=True, db_column='NgayHetHan', null=True)),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paymentmethod',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenpthuc', models.CharField(blank=True, db_column='TenPThuc', max_length=255, null=True)),
            ],
            options={
                'db_table': 'paymentmethod',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Phuong',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenphuong', models.CharField(blank=True, db_column='TenPhuong', max_length=255, null=True)),
            ],
            options={
                'db_table': 'phuong',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('ten', models.CharField(blank=True, db_column='Ten', max_length=255, null=True)),
                ('mota', models.CharField(blank=True, db_column='MoTa', max_length=255, null=True)),
                ('danhgia', models.IntegerField(db_column='DanhGia')),
                ('gia', models.FloatField(db_column='Gia')),
                ('chitietsp', models.CharField(blank=True, db_column='ChiTietSP', max_length=255, null=True)),
                ('hinhanh', models.CharField(blank=True, db_column='HinhAnh', max_length=255, null=True)),
                ('type', models.CharField(blank=True, db_column='Type', max_length=255, null=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productcomment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'productcomment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productcommentreply',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'productcommentreply',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productcommentreplyreaction',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('reaction', models.CharField(blank=True, db_column='Reaction', max_length=255, null=True)),
            ],
            options={
                'db_table': 'productcommentreplyreaction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'product_discount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Productview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'productview',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quan',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenquan', models.CharField(blank=True, db_column='TenQuan', max_length=255, null=True)),
            ],
            options={
                'db_table': 'quan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('noidung', models.CharField(blank=True, db_column='NoiDung', max_length=255, null=True)),
                ('rating', models.IntegerField(db_column='Rating')),
                ('createdat', models.DateField(blank=True, db_column='CreatedAt', null=True)),
            ],
            options={
                'db_table': 'review',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('rolename', models.CharField(blank=True, db_column='RoleName', max_length=255, null=True)),
                ('isdeleted', models.TextField(db_column='IsDeleted')),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sachtype',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('namxb', models.IntegerField(db_column='NamXB')),
            ],
            options={
                'db_table': 'sachtype',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SachtypeChitiettheloaisach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'sachtype_chitiettheloaisach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanphamdaxem',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sanphamdaxem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanphammuasau',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sanphammuasau',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sanphamyeuthich',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'sanphamyeuthich',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('giaship', models.FloatField(db_column='GiaShip')),
            ],
            options={
                'db_table': 'shipment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tacgia',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tentacgia', models.CharField(blank=True, db_column='TenTacGia', max_length=255, null=True)),
            ],
            options={
                'db_table': 'tacgia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Taikhoan',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, db_column='UserName', max_length=255, null=True)),
                ('password', models.CharField(blank=True, db_column='Password', max_length=255, null=True)),
                ('role', models.IntegerField(blank=True, db_column='Role', null=True)),
                ('createdtime', models.DateField(blank=True, db_column='CreatedTime', null=True)),
                ('isdeleted', models.TextField(db_column='IsDeleted')),
            ],
            options={
                'db_table': 'taikhoan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thanhpho',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenthanhpho', models.CharField(blank=True, db_column='TenThanhPho', max_length=255, null=True)),
            ],
            options={
                'db_table': 'thanhpho',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theloaidientu',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tentheloai', models.CharField(blank=True, db_column='TenTheLoai', max_length=255, null=True)),
            ],
            options={
                'db_table': 'theloaidientu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theloaiquanao',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tentheloai', models.CharField(blank=True, db_column='TenTheLoai', max_length=255, null=True)),
            ],
            options={
                'db_table': 'theloaiquanao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Theloaisach',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tentheloai', models.CharField(blank=True, db_column='TenTheLoai', max_length=255, null=True)),
            ],
            options={
                'db_table': 'theloaisach',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thethanhvien',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('sothe', models.CharField(blank=True, db_column='SoThe', max_length=255, null=True)),
                ('diemtichluy', models.IntegerField(blank=True, db_column='DiemTichLuy', null=True)),
                ('loaithe', models.CharField(blank=True, db_column='LoaiThe', max_length=255, null=True)),
            ],
            options={
                'db_table': 'thethanhvien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thongtingiaohang',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('hoten', models.CharField(blank=True, db_column='HoTen', max_length=255, null=True)),
                ('diachi', models.CharField(blank=True, db_column='DiaChi', max_length=255, null=True)),
                ('sodt', models.CharField(blank=True, db_column='SoDT', max_length=255, null=True)),
                ('macdinh', models.TextField(db_column='MacDinh')),
            ],
            options={
                'db_table': 'thongtingiaohang',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thuonghieu',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenthuonghieu', models.CharField(blank=True, db_column='TenThuongHieu', max_length=255, null=True)),
            ],
            options={
                'db_table': 'thuonghieu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Thuonghieuquanao',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('tenthuonghieu', models.CharField(blank=True, db_column='TenThuongHieu', max_length=255, null=True)),
            ],
            options={
                'db_table': 'thuonghieuquanao',
                'managed': False,
            },
        ),
    ]
