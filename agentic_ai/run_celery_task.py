import os



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "agentic_ai.settings")
import django
django.setup()

from agents.models import Agent
from agents.tasks import run_agent_task

agent = Agent.objects.create(name="Agent Test Celery", description="Test avec script")
result = run_agent_task.delay(agent.id)
print(f"Tâche lancée, id de résultat : {result.id}")
