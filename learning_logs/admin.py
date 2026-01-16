from django.contrib import admin

# Register your models here.

from learning_logs.models import Topic, Entry #import the Topic and Entry model from models.py

admin.site.register(Topic) #register the Topic model with the admin site so we can manage it through the admin interface
admin.site.register(Entry) # register the Entry model with the admin site so we can manage it through the admin interface