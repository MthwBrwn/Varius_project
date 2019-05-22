from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.FloatField(max_length=12, null=True)

    def __str__(self):
        return f'{self.user.username} rate'
        
    