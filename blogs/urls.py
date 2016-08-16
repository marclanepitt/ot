from django.conf.urls import url

from . import views

app_name = 'blogs'

urlpatterns = [
    url(r'^$', views.index, name = 'Articles'),

    url(r'^lists/', views.list_index, name='List'),

    url(r'^blogs/', views.blog_index, name='Blog'),

    url(r'^countdowns/', views.countdown_index, name='Countdown'),

    url(r'^submit/' ,views.submit, name= 'submit'),

    url(r'^submit_blog/', views.submit_blog, name= 'submit blog'),

    url(r'^submit/list/', views.submit_list, name= 'submit list'),

    url(r'^submit/countdown/', views.submit_countdown, name= 'submit countdown'),

    url(r'^search/', views.search, name = 'search'),

    url(r'^(?P<slug>[a-z-0-9-]+)/$',views.detail, name='detail'),


]
