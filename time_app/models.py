from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Client(models.Model):
    '''
    '''
    client = models.CharField(max_length=255)

    def __str__(self):
        return self.client


class ProjectName(models.Model):
    '''
    '''
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.project_name


class TimePost(models.Model):
    '''
    '''
    time_spent = models.FloatField()
    notes = models.TextField()
    date = models.DateField(default=timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project_name = models.ForeignKey(
        ProjectName, on_delete=models.CASCADE,
        null=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.notes


