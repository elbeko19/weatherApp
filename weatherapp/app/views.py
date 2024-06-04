from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


def index(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()
        
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=da258f1826f80f532aa6f19d6af34b05&units=metric'
        
    weather_data = []
    cities = City.objects.all()
        
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
            'humidity': r['main']['humidity'],
            'wind': r['wind']['speed'],
            'pressure': r['main']['pressure'],
            'country': r['sys']['country'],
        }
            
        weather_data.append(city_weather)
    context = {
            'weather_data': weather_data,
            'form': form,
    }
        
        
    return render(request, 'index.html', context)
