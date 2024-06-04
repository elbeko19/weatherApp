from django.forms import ModelForm, TextInput
from .models import City


class CityForm(ModelForm):
    class Meta:
        max_length=254,
        widget = {'name': TextInput(attrs={'class': 'input', 'placeholder': 'Enter a city'})}
        model = City
        fields = ["name"]
