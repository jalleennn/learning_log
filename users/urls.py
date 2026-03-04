"""Defines URL patterns for users."""


from django.urls import path # import the url function from the main url in the learninng_log project.
from django.contrib.auth import views as auth_views # import the LoginView class from django.contrib.auth.views module.

from . import views

urlpatterns = [
    # Login page
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'), # logout page
    # Registration page
    
    
]
# creates a url link for the login page using the LoginView class.
# Since we aren't writing our own views we pass a dictionary telling Django where to find the template for the login page.