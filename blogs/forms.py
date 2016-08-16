from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["category","title","text","description","pic","author","author_pic"]

class BlogForm(forms.ModelForm):
    category = forms.CharField(widget=forms.HiddenInput(),initial="Blog")
    class Meta:
        model = Article
        fields = ["title", "text", "description", "pic", "author", "author_pic"]
