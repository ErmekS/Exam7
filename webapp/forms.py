from django import forms
# from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Poll


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question']
        widgets = {
            "question": widgets.Textarea(attrs={"placeholder": "Введите вопрос"})
        }
