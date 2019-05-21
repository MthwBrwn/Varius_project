from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class TimePost(models.Model):
    '''
    '''
    time_spent = models.FloatField()
    notes = models.TextField()
    date = models.DateField(default=timezone.now)
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.notes


class Client(models.Model):
    '''
    '''
    client = models.CharField(primary_key=True, max_length=255)
    project_name = models.CharField(max_length=255)
