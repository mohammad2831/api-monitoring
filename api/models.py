from django.db import models

class ApiTarget(models.Model):
    api = models.CharField(max_length=500)
    interval_minutes = models.IntegerField(default=1)
    def __str__(self):
        return self.api