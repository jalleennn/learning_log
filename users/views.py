from django.shortcuts import render, redirect # import the render function to generate the registratin page.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate # import the login and the authenticate functions to log in the user if and only if their registration information is correct.
# import the logout function from django.contrib.auth().
from django.contrib.auth.forms import UserCreationForm
#import the UserCreationForm class from django,contrib.auth.forms module to create a user registration from.
from django.contrib import messages
from .models import Topic
from .models import TopicForm

# Create your views here.

def logoutView(request):
    """Log the user out."""
    logout(request) #call logout in the function.
    return HttpResponseRedirect(reverse('learning_logs:index'))
# redirect to the homepage.



def register(request): # the register function checks if the we are responding to a post request or a get request. If it is a GET request we create a blank instance of the UserCreationForm class.
    """Register a new user."""
    if request.method == 'POST':
        # Display blank registration form.
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Add your first topic below.')
            return redirect('new_topic')
    else:
        # Process completed form.
        form = UserCreationForm() # if POST request we make an instance based on the submitted data.
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

def new_topic(request):
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner = request.user  # associate topic with logged-in user
            topic.save()
            return redirect('topics')  # redirect to topic list
    else:
        form = TopicForm()
    return render(request, 'new_topic.html', {'form': form})

# List topics
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    return render(request, 'topics.html', {'topics': topics})
 






