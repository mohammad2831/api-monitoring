from django.db import models
from django_celery_beat.models import PeriodicTask
class ApiTarget(models.Model):
    api = models.CharField(max_length=500)
    interval_minutes = models.IntegerField(default=1)
    start_test = models.DateTimeField(null=True, blank=True)
    finish_test = models.DateTimeField(null=True, blank=True)

    task = models.OneToOneField(PeriodicTask, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.api} - {self.interval_minutes} - {self.start_test}" 