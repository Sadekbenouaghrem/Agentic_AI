import graphene
from graphene_django import DjangoObjectType
from .models import Agent, Task, Interaction

class AgentType(DjangoObjectType):
    class Meta:
        model = Agent
        fields = "__all__"

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"

class InteractionType(DjangoObjectType):
    class Meta:
        model = Interaction
        fields = "__all__"
