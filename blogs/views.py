from django.shortcuts import render,get_object_or_404
from .models import Article

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'index.html',context)

def detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    return render(request, 'blog.html', {'article': article})

def search(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'search.html',context)

def submit(request):
    return render(request, 'submit.html')

def submit_blog(request):
    return render(request, 'submit_blog.html')

def submit_list(request):
    return render(request, 'submit_list.html')

def submit_countdown(request):
    return render(request, 'submit_countdown.html')
