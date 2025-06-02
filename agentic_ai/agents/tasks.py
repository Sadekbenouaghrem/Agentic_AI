from celery import shared_task
from .models import Agent, Interaction
from django.conf import settings
from openai import OpenAI

client=OpenAI(api_key = settings.OPENAI_API_KEY)

@shared_task
def run_agent_task(agent_id):
    try:
        # Import des modèles à l'intérieur de la tâche (important !)
       

        agent = Agent.objects.get(id=agent_id)
        prompt = f"Quel est l'objectif de l'agent {agent.name} ?"

        response = OpenAI.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Tu es un agent autonome."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']

        Interaction.objects.create(
            agent=agent,
            prompt=prompt,
            response=reply
        )

        print(f"Agent {agent.name} is thinking...")
        return f"Interaction enregistrée pour l'agent {agent.name}."

    except Agent.DoesNotExist:
        return f"L'agent avec id {agent_id} n'existe pas."
    except Exception as e:
        return f"Erreur lors de l'exécution de l'agent : {str(e)}"

@shared_task
def add(x, y):
    return x + y





