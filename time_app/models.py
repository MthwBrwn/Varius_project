from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import admin


class Client(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    '''
    '''
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    archived = models.BooleanField(default=False, )

    def __str__(self):
        return self.name


class TimePost(models.Model):
    '''
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_spent = models.FloatField("Time worked", null=True, blank=True)
    expenses = models.FloatField(null=True, blank=True)
    miles = models.FloatField(null=True, blank=True)
    notes = models.TextField("Time notes", null=True, blank=True)
    expense_notes = models.TextField("Expense notes", null=True, blank=True)
    miles_notes = models.TextField("Miles notes", null=True, blank=True)
    # added image to model in order to upload expenses
    # expense_image = models.ImageField(
    #     "Upload your expense sheet", null=True, blank=True
    #     )
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


# class TimePostAdmin(admin.ModelAdmin):
#     list_display = ('user', 'client', 'project')
