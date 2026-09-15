from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    time_spent = models.IntegerField(default=0)  # Time spent in seconds
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title