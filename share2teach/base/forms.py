# base/forms.py
from django import forms
from .models import Document

class ModerationForm(forms.Form):
    STATUS_CHOICES = [
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True)
    feedback = forms.CharField(widget=forms.Textarea, required=False)
