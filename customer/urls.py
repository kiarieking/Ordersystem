from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/registration', views.registration_form, name='registration_form'),
    path('home/registration/register', views.register, name='register'),
    path('home/login_form', views.login_form, name='login_form'),
    path('home/login_form/login', LoginView.as_view(template_name='customer/login.html'), name='login2'),
    path('home/logout', LogoutView.as_view(template_name='customer/logout.html'), name='logout')
]