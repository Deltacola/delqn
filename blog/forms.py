from django import forms
from .choice import *


class DeliSearchForm(forms.Form):
    start_point = forms.ChoiceField(choices = AREA_CHOICES, label="From ",
                                    initial='', widget=forms.Select(), required=True)
    end_point = forms.ChoiceField(choices = AREA_CHOICES, label="To ",
                                  initial='', widget=forms.Select(), required=True)
    weight_form = forms.ChoiceField(choices = WEIGHT_CHOICES, label="무게 ",
                                    initial='', widget=forms.Select(), required=True)
    length_form = forms.ChoiceField(choices = LENGTH_CHOICES, label="총길이(가로+세로+높이) ",
                                    initial='', widget=forms.Select(), required=True)
    time_form = forms.ChoiceField(choices = TIME_CHOICES, label="최대 도착시간 ",
                                  initial='', widget=forms.Select(), required=False)

