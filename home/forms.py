from django.forms import ModelForm
from .models import *

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['subject', 'noidung', 'rating']

class CommentForm(ModelForm):
    class Meta:
        model = Productcomment
        fields = ['noidung']