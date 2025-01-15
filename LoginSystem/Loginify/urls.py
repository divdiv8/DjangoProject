from django.urls import path
from . import views

app_name = 'login'
# Define URL patterns for this app
urlpatterns = [
    path('hello/', views.hello_view),
    path('homepage/', views.home_page_view),
    path('userlogin/', views.user_login_view , name='userlogin'),
    path('signup/', views.signup_view, name='signup'),
]