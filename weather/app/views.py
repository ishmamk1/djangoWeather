from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Weather
import requests

def index(request):
    API_KEY = 'key'
    currentWeatherURL = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
    if request.method == 'POST':
        city = request.POST.get('city')
        data = requests.get(currentWeatherURL.format(city, API_KEY)).json()
        description = data['weather'][0]['description']
        temperature = round((float(data['main']['temp'])-273.15)*(9/5)+32,2)
        icon = data['weather'][0]['icon']
        favorite = request.POST.get('favorite')
        favorite = favorite == 'on'

        weatherData = Weather(city=city, description=description, temperature=temperature,icon=icon, favorite=favorite)
        weatherData.save()



        return redirect('index')

    else:
        weatherData = Weather.objects.order_by('-id')[:1]
        watchlist = Weather.objects.filter(favorite=True)
        return render(request, 'index.html', {'weatherData': weatherData, 'watchlist': watchlist})





