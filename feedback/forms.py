from django import forms
from .models import feedback

class feedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'placeholder': 'Your feedback...'}),
        }
