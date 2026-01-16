from django.shortcuts import render

from .models import Topic  # import the Topic model from the current package.
# Create your views here.

# When the URL request matches what is defined
# Django will look for a function called index in this file.
def index(request):
    """The home page for Learning Log"""

def topics(request): # Topic function needs the request object Django received from the server.
    """Show all topics."""
    topics = Topic.objects.order_by("date_added") # We aask for the topic object sorted by the date_added attribute.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context) # pass it to render to complete the template.

# Render uses two argument, the original request object and the template it can use to build the page.