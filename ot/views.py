from django.shortcuts import render

def HomeView(request):
    return render(request , 'site_home.html')

def AboutView(request):
    return render(request, 'about.html')