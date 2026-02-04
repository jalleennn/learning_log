from django.shortcuts import render # import the render function to generate the registratin page.
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login,logout, authenticate # import the login and the authenticate functions to log in the user if and only if their registration information is correct.
# import the logout function from django.contrib.auth().
from django.contrib.auth.forms import UserCreationForm
#import the UserCreationForm class from django,contrib.auth.forms module to create a user registration from.

# Create your views here.

def logoutView(request):
    """Log the user out."""
    logout(request) #call logout in the function.
    return HttpResponseRedirect(reverse('learning_logs:index'))
# redirect to the homepage.

def register(request): # the register function checks if the we are responding to a post request or a get request. If it is a GET request we create a blank instance of the UserCreationForm class.
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST) # if POST request we make an instance based on the submitted data.
        if form.is_valid(): # checks the validity of the data.
            new_user = form.save() # calls the form save() method to add the new user to the database.
            # Log the user in and then redirect to the homepage.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'] # after the user is created we authenticate them using the username and password they just provided.
            ) # after the user is asked to enter two matching passwords.
            login(request, authenticated_user)
            
            return HttpResponseRedirect(reverse('learning_logs:index'))
        # Redirect the user to the homepage after logging them in.

    context = {'form': form}
    return render(request, 'users/register.html', context)