from django import forms
from .models import TimePost, Project


class TimePostForm(forms.ModelForm):
    class Meta:
        model = TimePost
        fields = ('time_spent', 'client', 'project', 'notes')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.none()

        if 'client' in self.data:
                try:
                    client_id = int(self.data.get('client'))
                    self.fields['project'].queryset = Project.objects.filter(
                        client_id=client_id).order_by('name')
                except (ValueError, TypeError):
                    pass  
        elif self.instance.pk:
            self.fields['project'].queryset = self.instance.client.project_set.order_by('name')