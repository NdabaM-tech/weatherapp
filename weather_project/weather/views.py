from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render
from django.conf import settings

def get_weather(request):
    if 'city' in request.GET:
        city = request.GET['city']
    else:
        city = 'London'  # Default city

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric'

    response = requests.get(url)
    weather_data = response.json()

    if weather_data.get('cod') != 200:
        weather = None
    else:
        weather = {
            'city': weather_data['name'],
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
        }

    return render(request, 'weather/weather.html', {'weather': weather})
