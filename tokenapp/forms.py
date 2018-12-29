from django import forms

from .models import Worker


class WorkerForm(forms.ModelForm):
    # TODO: Define other fields here

    class Meta:
        model = Worker
        fields = '__all__'
