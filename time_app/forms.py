from django import forms
from flatpickr import DatePickerInput
from .models import TimePost, Project


class TimePostForm(forms.ModelForm):
    class Meta:
        model = TimePost
        fields = ('time_spent', 'date', 'client', 'project', 'notes')
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 4}),
            'date': DatePickerInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['project'].queryset = Project.objects.none()
        # self.fields['date'].widget = widgets.AdminDateWidget()

        if 'client' in self.data:
                try:
                    client_id = int(self.data.get('client'))
                    self.fields['project'].queryset = Project.objects.filter(
                        client_id=client_id).order_by('name')
                except (ValueError, TypeError):
                    pass  
        elif self.instance.pk:
            self.fields['project'].queryset = self.instance.client.project_set.order_by('name')