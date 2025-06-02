from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Agent, Task, Interaction
from .serializers import AgentSerializer, TaskSerializer, InteractionSerializer
from django.shortcuts import render
from .models import Agent
from django.shortcuts import redirect
from .form import AgentForm
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404
from .form import TaskForAgentForm


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class AgentViewSet(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
    permission_classes = [IsAdminOrReadOnly]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

class InteractionViewSet(viewsets.ModelViewSet):
    queryset = Interaction.objects.all()
    serializer_class = InteractionSerializer
    permission_classes = [permissions.IsAuthenticated]


class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'  # ou autre template si tu as


def agent_list(request):
    agents = Agent.objects.prefetch_related('interactions').all()
    return render(request, 'agents/agent_list.html', {'agents': agents})
def agent_create(request):
    if request.method == 'POST':
        form = AgentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agent_list')
    else:
        form = AgentForm()
    return render(request, 'agents/agent_form.html', {'form': form})


def ai_task_list(request):
    tasks = Task.objects.all().order_by('-created_at')  # suppose que tu as un champ created_at
    return render(request, 'agents/ai_task_list.html', {'tasks': tasks})

def ai_task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    interactions = task.interaction_set.all().order_by('timestamp')  # suppose champ timestamp
    return render(request, 'agents/ai_task_detail.html', {
        'task': task,
        'interactions': interactions
    })

def task_create_for_agent(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    
    if request.method == 'POST':
        form = TaskForAgentForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.assigned_agent = agent
            task.save()
            return redirect('agent_detail', agent_id=agent.id)  # change this as needed
    else:
        form = TaskForAgentForm()
    
    return render(request, 'agents/task_form_for_agent.html', {'form': form, 'agent': agent})

def agent_detail(request, agent_id):
    agent = get_object_or_404(Agent, id=agent_id)
    tasks = agent.tasks.all()
    return render(request, 'agents/agent_detail.html', {'agent': agent, 'tasks': tasks})
