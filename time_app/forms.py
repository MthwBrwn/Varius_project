from django import forms
from .models import TimePost, Project


class TimePostForm(forms.ModelForm):
    class Meta:
        model = TimePost
        fields = ('time_spent', 'client', 'project', 'notes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.none()