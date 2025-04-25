from django.db import models
from django.utils import timezone

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Update completed_date when task is marked as completed
        if self.completed and not self.completed_date:
            self.completed_date = timezone.now()
        elif not self.completed and self.completed_date:
            self.completed_date = None
        super().save(*args, **kwargs)