from django import forms
from .models import Article
from django.forms.formsets import BaseFormSet

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category","title","text","description","pic","author","author_pic"]