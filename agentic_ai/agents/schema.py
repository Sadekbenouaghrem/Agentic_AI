import graphene
from graphene_django.types import DjangoObjectType
from .models import Agent, Task

class AgentType(DjangoObjectType):
    class Meta:
        model = Agent
        fields = "__all__"

class TaskType(DjangoObjectType):
    class Meta:
        model = Task
        fields = "__all__"

class Query(graphene.ObjectType):
    all_agents = graphene.List(AgentType)
    all_tasks = graphene.List(TaskType)

    def resolve_all_agents(root, info):
        return Agent.objects.all()

    def resolve_all_tasks(root, info):
        return Task.objects.all()

schema = graphene.Schema(query=Query)

class CreateAgent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        description = graphene.String()

    agent = graphene.Field(AgentType)

    def mutate(self, info, name, description=None):
        agent = Agent(name=name, description=description)
        agent.save()
        return CreateAgent(agent=agent)

class Mutation(graphene.ObjectType):
    create_agent = CreateAgent.Field()

