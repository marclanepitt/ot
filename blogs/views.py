from django.shortcuts import render,get_object_or_404, HttpResponseRedirect
from .models import Article
from .forms import BlogForm

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'index.html',context)


def list_index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'list_index.html', context)


def blog_index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'blog_index.html', context)


def countdown_index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:20]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'countdown_index.html', context)

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
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BlogForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('submit_success.html')

            # if a GET (or any other method) we'll create a blank form
    else:
        form = BlogForm()

    return render(request, 'submit_blog.html', {'form': form})

def submit_list(request):
    return render(request, 'submit_list.html')

def submit_countdown(request):
    return render(request, 'submit_countdown.html')
