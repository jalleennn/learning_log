"""Define URL patterns for learning_logs project."""
# Add a docstring describing the purpose of this file.

from sys import path
from django.urls import  path # import the url function needed when mapping URL to views.

from . import views # import views module from current package.
# the dot (.) indicates the same directory as this urls.py file.

app_name = 'learning_logs' # set the application namespace for the learning_logs app.
# the variable urlpatterns  is a list of individual pages that can be requested from the learning_logs app.
urlpatterns = [
    # Home page
     
    path('', views.index, name='index'),
    #Show all topics
    path('topics/', views.topics, name = 'topics'),
    path('topics/<int:topic_id>/', views.topic, name= 'topic'),
    path('new_topics/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry') ,
    # Page for editing an entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'), # this function sends request to the view function to edit entry()
] 
# Takes three arguments: a regular expression,view function to call, provides the name index for this URL pattern.
# when the regular expression is matched, Django calls view.index.

