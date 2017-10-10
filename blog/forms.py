from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class DeliSearchForm(forms.Form):
    start_point = forms.CharField(label='출발지역구')
    end_point = forms.CharField(label='도착지역구')
