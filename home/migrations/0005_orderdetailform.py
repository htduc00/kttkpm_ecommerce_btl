# Generated by Django 3.1.7 on 2021-06-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_browserorderform'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetailForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stt', models.CharField(blank=True, max_length=255, null=True)),
                ('maMatHang', models.CharField(blank=True, max_length=255, null=True)),
                ('thongTinMatHang', models.CharField(blank=True, max_length=255, null=True)),
                ('phanLoaiHang', models.CharField(blank=True, max_length=255, null=True)),
                ('donGia', models.CharField(blank=True, max_length=255, null=True)),
                ('soLuong', models.CharField(blank=True, max_length=255, null=True)),
                ('thanhTien', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
