from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


class Client(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.client


class Project(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)
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
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        null=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.notes

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



