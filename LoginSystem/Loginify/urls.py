from django.urls import path
from . import views

# Define URL patterns for this app
urlpatterns = [
    path('hello/', views.hello_view),
    path('homepage/', views.home_page_view),
]