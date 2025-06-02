from rest_framework import serializers
from .models import Agent, Task, Interaction
import bleach


def clean_input(text):
    return bleach.clean(text)

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'

    def validate_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Le nom de l'agent doit contenir au moins 3 caractères.")
        return value


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Le titre doit contenir au moins 3 caractères.")
        return value
    
    def validate_description(self, value):
        return clean_input(value)

class InteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaction
        fields = '__all__'

    def validate(self, data):
        if data['agent'] != data['task'].assigned_agent:
            raise serializers.ValidationError("L'agent doit être celui assigné à la tâche.")
        return data

