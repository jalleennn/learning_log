from django import forms

from .models import Topic, Entry # import the module 'form' and the model 'Topic'
# update the import statement to include Entry as well.

class TopicForm(forms.ModelForm): # create a class with inherits from 'forms.ModelForm'
    class Meta: # Meta is a simple form nested in the class TopicForm
        model = Topic # we build a form from the Topic model that includes just text fields.
        fields = ['text']
        labels = {'text': ''} # there will be no label text next to the txet field in the form.

class EntryForm(forms.ModelForm): # Inherits from forms.ModelForm
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''} # Field text has a blank label.
        widgets = {'text': forms.Textarea(attrs={'cols': 80})} 
        # We included the widgets so we can have an area for the user to write his entries inside.
        # We wanted a column size of 80 so it overrides Django's default 40 wide text box