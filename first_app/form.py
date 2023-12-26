from django import forms
from .models import myModel
from django.forms.widgets import NumberInput
import datetime

FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class base_forms(forms.Form):
    name = forms.CharField(max_length=20,    required = False)
    email = forms.EmailField(label='email')
    comment = forms.CharField(widget=forms.Textarea, initial='comment ')
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}), initial=True)
    date = forms.DateField(initial=datetime.date.today)
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    value = forms.DecimalField()
    favorite_color = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)
    model_choice = forms.ModelChoiceField(
        queryset = myModel.objects.all(),
        initial = 0
        )