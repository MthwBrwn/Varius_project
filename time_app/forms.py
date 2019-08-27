from django import forms
from flatpickr import DatePickerInput
from .models import TimePost, Project


class TimePostForm(forms.ModelForm):
    class Meta:
        model = TimePost
        fields = ('date', 'client', 'project', 'time_spent', 'notes')
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 2}),
            'date': DatePickerInput()
        }
        help_texts = {
            'time_spent': '''This field is in hours.  
            Partial hours should only be entered as quarter-hours
            (.25, .5, .75, .0)'''
        }

    def clean_time_spent(self):
        time_try = self.cleaned_data.get("time_spent")
        if time_try % .25 > 0:
            raise forms.ValidationError(
                "The partial hours posted need to be in quarter hours only"
                )
        if time_try < 0:
            raise forms.ValidationError(
                "time posted cannot be negative"
                )
        if time_try >= 24.0:
            raise forms.ValidationError(
                "time posted cannot be greater than 24.0 hours"
                )
        return time_try

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


class TimeGetForm(forms.ModelForm):
    class Meta:
        model = TimePost
        fields = ('date', 'client', 'project',)
        
