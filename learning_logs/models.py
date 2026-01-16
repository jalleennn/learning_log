from django.db import models

# Create your models here.

class Topic(models.Model): # creates a class called Topic that inherits from parent class Model
    """A topic the user is learning about."""
    text = models.CharField(max_length= 200) #CharField is a piece of data that made up of text or characters.
    date_added = models.DateTimeField(auto_now_add = True) #DateTimeField, a piece of data that records a date and Time.
# Using the CharField attribute, tells Django how much space reserve in the database, 
# we gave it 200 characters.
# auto_add_now sets the attributes telling Django to set time and date to the current moment.

    def __str__(self): # Displays information about a topic. __str__() methods that performs that.
        """Return a string repesentation of the model."""
        return self.text
    
class Entry(models.Model): # a child class Entry inherits from the Model parent class.
    """ Something specific learned about a topic"""
    topic = models.ForeignKey(Topic, on_delete =models.CASCADE) # the attribute has foreign key that will connect each entry to a topic saved.
    text = models.TextField() #we don't have a limit for the text because we don't know length of info the user needs to save.
    # 'on_delete= CASCADE' means when the topic is deleted , all the entries also follow suit. Very important to add to the attribute because in real life users will like to delete a topic.
    date_added = models.DateTimeField(auto_now_add=True) # Timestamp are set to the current moment the user save that entry.

    class Meta: # nest Meta class into the class Entry, holds extra information for managing a model
        verbose_name_plural = 'entries' # this attributes tells django to use entries when the user wants to input more than one entry.
# set forward and quantifies more than one entry as 'entries' otherwise , Django would refer to it as 'Entrys'.

    def __str__(self): # __str__() method shows the inputs
        """Return a string representation of the model."""
        return self.text[:50] + "..."  # ellipsis added to clarify that we aren't the entire entry.
    # we don't want to have a disorganised interface so Django shows just the first 50 characters of the text.

