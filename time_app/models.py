from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


class Client(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class TimePost(models.Model):
    '''
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_spent = models.FloatField()
    notes = models.TextField()
    date = models.DateField(default=timezone.now)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE,
        null=True
        )

    def __str__(self):
        return self.notes

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



