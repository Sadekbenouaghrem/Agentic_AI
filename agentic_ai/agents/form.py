from django import forms
from .models import Agent
from .models import Task

class AgentForm(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['name', 'description']


class TaskForAgentForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status']
