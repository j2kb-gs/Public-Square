from django import forms
from apps.home.models import Review
from django.forms.widgets import Textarea, SelectDateWidget, DateTimeInput, DateInput


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rate', 'review']
        widgets = {
            'review': Textarea(attrs={'cols': 45, 'rows': 7})
        }
