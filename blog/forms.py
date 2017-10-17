from django import forms

from .choice import *
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class DeliSearchForm(forms.Form):
    start_point = forms.CharField(label='출발지역구')
    end_point = forms.CharField(label='도착지역구')
    length_form = forms.ChoiceField(choices = LENGTH_CHOICES, label="총길이(가로+세로+높이)", initial='', widget=forms.Select(), required=True)
