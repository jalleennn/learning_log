"""Defines URL patterns for users."""


from django.urls import path # import the url function from the main url in the learninng_log project.
from django.contrib.auth.views import LoginView , LogoutView # import the LoginView class from django.contrib.auth.views module.

from . import views

urlpatterns = [
    # Login page
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'), # logout page
    # Registration page
    path('register/', views.register, name='register'),
]
# creates a url link for the login page using the LoginView class.
# Since we aren't writing our own views we pass a dictionary telling Django where to find the template for the login page.