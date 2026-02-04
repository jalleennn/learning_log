from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404 # import Http404 so if the topic owner doesn't much the requested user it calls an page not found.And so the users can be redirected back to the topics page after they have submitted their topics
# reverse function with Django will generate a URL when the page is requested.
from django.urls import reverse

from .models import Entry, Topic  # import the Topic model from the current package.
from .forms import TopicForm, EntryForm # we also import the form TopicForm.
# Create your views here.
# Update the import statement to include the EntryForm.
from django.contrib.auth.decorators import login_required
#import the login function from the auth module.

# When the URL request matches what is defined
# Django will look for a function called index in this file.
def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

# apply login required as a decorator to the topics view function.
# if the user is not logged in they will be redirected to the to login page.
@login_required
def topics(request): # Topic function needs the request object Django received from the server.
    """Show all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added') # the code fragment retrives from the database the topics the logged in user owns.
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context) # pass it to render to complete the template.

@login_required
def topic(request, topic_id): #view functions can accept additional parameters.
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id) # retrieve the topic with the given id.
    # Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    entries = Entry.objects.filter(topic=topic).order_by('-date_added') # retrieve all entries associated with this topic.
    context = {'topic': topic, 'entries': entries} # store the topics and entries in the dictionary context.
    return render(request, 'learning_logs/topic.html', context)
# Render uses two argument, the original request object and the template it can use to build the page.

# the minus sign in the date added (-date_added) sorts the entries in the reverse order, with the most currrent ones first or on top.

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method == 'POST': # determines whether the request is get or post and the request is probably get it retruns a blank form.
        #No data submitted; create a blank form.
        form =TopicForm() # an instance TopicForm and send it to template in the context dictionary. There was no argument so it creates a blank form that the user can fill out.
    else:
        # POST data submitted; process data.
        form = TopicForm(request.POST) # make an instnace and return the info submitted by the user.
        if form.is_valid(): # check the validity of the submitted data. 'is_valid() checks that all the required fields have been filled in.
            new_topic = form.save(commit=False) # save the form to the database.
            new_topic.owner = request.user # set the owner attribute of the new topic to the current user.
            new_topic.save() # if valid, can be saved by writing data from the database.
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        # Redirects the users to the topics page so the user can see the topic they just entered in the list of topics.

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id): # function new_entry has an topic_id it receives from the url.
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id) # we need the topic to render the page and process the form.

    if request.method == 'POST': # check if the request is POST or GET, if GET we create an empty balnk instance.
        # No data submitted; create a blank form.
        form = EntryForm() 
    else:
        # POST data submitted ; process data.
        form = EntryForm(data= request.POST) # if POST we create POST data from the request object.
        if form.is_valid(): # we then check the validity of the form. if it is valid, set the entry object's topic attribute before saving the database.
            new_entry = form.save(commit=False) # Tells Django to create a new entry object and store in new-entry
            new_entry.topic = topic # set the new entry topic attribute to topic and  pulls the topic from database
            new_entry.save() # saves the entry to the database
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) # redirects the user to the topic page
        
    context = {'topic': topic, 'form':form}
    return render(request, 'learning_logs/new_entry.html', context)
# user should to able to see the new entry in the list of entries.

@login_required
def edit_entry(request, entry_id): # entry object the user wants to edit.
    """Edit an existing entry."""
    entry = Entry.objects.get(id=entry_id)
    topic= entry.topic # the topic associated with the entry must align.
    if topic.owner != request.user:
        raise Http404

    if request.method == 'POST':
        # Initial request; pre-fill from with the current entry.
        form = EntryForm(instance=entry) # display a form prefilled with what the user has entered because of the GET request and the user is able to edit.
    else:
        # POST data submitted; process data.
        form= EntryForm(instance= entry, data=request.POST) # if POST, a form is created based on information linked with entry objects.
        if form.is_valid(): # check the validity of the form.
            form.save() # saves it to the database.
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) # redirect to th etopic page where the user should see the updated version of the entry edited.
        
    
    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'learning_logs/edit_entry.html', context)