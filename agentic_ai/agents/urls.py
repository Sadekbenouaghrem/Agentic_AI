from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AgentViewSet, TaskViewSet, InteractionViewSet
from .views import TaskListView,agent_list,agent_create,ai_task_list,ai_task_detail
from . import views


router = DefaultRouter()
router.register(r'agents', AgentViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'interactions', InteractionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', agent_list, name='agent_list'),
     path('tasks/list/', TaskListView.as_view(), name='task_list'),
     path('create/', agent_create, name='agent_create'),
    path('ai-tasks/', ai_task_list, name='ai_task_list'),
    path('ai-tasks/<int:task_id>/', ai_task_detail, name='ai_task_detail'),
    path('agents/<int:agent_id>/', views.agent_detail, name='agent_detail'),
    path('agents/<int:agent_id>/add-task/', views.task_create_for_agent, name='task_create_for_agent'),
]

