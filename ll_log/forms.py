from django import forms
from .models import Topic, Entry, Nest  # Adjust the import path based on your project structure

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}

class NestForm(forms.ModelForm):
    class Meta:
        model = Nest
        fields = ['text']
        labels = {'text': ''}
