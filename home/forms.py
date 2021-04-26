from django import forms
from django.forms import ModelForm
from .models import *

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)
    catid = forms.IntegerField()
    

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'noidung', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Productcomment
        fields = ['noidung']
