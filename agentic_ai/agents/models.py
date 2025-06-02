from django.db import models
from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

class Agent(models.Model):
    name = models.CharField(max_length=100, unique=True, validators=[MinLengthValidator(3)])
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('FAILED', 'Failed')
    ]

    title = models.CharField(max_length=150, validators=[MinLengthValidator(3)])
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    assigned_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'assigned_agent')

    def __str__(self):
        return f"{self.title} ({self.status})"

class Interaction(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='interactions')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='interactions')
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"Interaction by {self.agent.name} on {self.task.title}"

# Create your models here.
