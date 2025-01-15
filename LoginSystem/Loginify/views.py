from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello_view(request):
    return HttpResponse("Hello, Divya!")

def home_page_view(request):
    return render(request, 'Loginify/index.html')