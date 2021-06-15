from django import forms
from django.db.models import fields
from django.forms import Form, ModelForm
from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    type = forms.CharField()

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'noidung', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Productcomment
        fields = ['noidung']


class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['soluong','variant_id']

class OrderForm(ModelForm):
    class Meta:
        model = OrderFormm
        fields = ['name','address','phone','city','dvvc']


STATUS = [
    ('WAITING', 'WAITING'),
    ('DELIVERING', 'DELIVERING'),
]
class ExportInvoiceForm(forms.Form):
    orderId = forms.CharField(max_length=10)
    status = forms.ChoiceField(choices=STATUS)

class AddProductForm(forms.Form):
    typeChoices = [
        ('Book', 'Book'),
        ('Electro', 'Electro'),
        ('Clothe', 'Clothe')
    ]
    ten = forms.CharField(label='Product Name', help_text='Insert product name')
    mota = forms.CharField(label='Description', help_text='Insert description')
    # gia = forms.CharField(label='Price', help_text='Insert price')
    chiTietSP = forms.CharField(label='Product Detail', help_text='Insert product detail')
    type = forms.ChoiceField(label='Type', help_text='Select type', choices=typeChoices)

