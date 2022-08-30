from django import forms
from .models import *


class ReviewForm(forms.ModelForm):
    """Form of reviews"""
    class Meta:
        model = Reviews
        fields = ("name", "email", "text")
