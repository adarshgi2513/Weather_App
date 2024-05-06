import requests
from django.shortcuts import render
from .models import City


def get_weather(city):
    api_key = "69d8fc830299fdb152992a54900459e2"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def home(request):
    if request.method == 'POST':
        city_name = request.POST.get('city')
        city_weather = get_weather(city_name)
        context = {'city_weather': city_weather}
        return render(request, 'home.html', context)
    else:
        cities = City.objects.all()
        context = {'cities': cities}
        return render(request, 'home.html', context)