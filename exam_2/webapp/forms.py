from django import forms
from django.forms import widgets
from webapp.models import Poll, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ('question',)


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ('choice_text',)

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')