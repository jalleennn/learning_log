"""Define URL patterns for learning_logs project."""
# Add a docstring describing the purpose of this file.

from sys import path
from django.urls import  path # import the url function needed when mapping URL to views.

from . import views # import views module from current package.
# the dot (.) indicates the same directory as this urls.py file.

# the variable urlpatterns  is a list of individual pages that can be requested from the learning_logs app.
urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),

    #Show all topics
    path('topics/', views.topics, name = 'topics'),
    path('learning_logs/', views.topics, name = 'learning_logs'),
] 
# Takes three arguments: a regular expression,view function to call, provides the name index for this URL pattern.
# when the regular expression is matched, Django calls view.index.

