from django.shortcuts import render ,HttpResponse
import requests
import datetime

# Create your views here.
def home(request):
    if request.method == 'POST' and 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Indore'  # Default city

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=51274294c9db126f55981cc9dcaaf04f'
    PARAMS = {'units': 'metric'}
    data = requests.get(url, params=PARAMS).json()

    # Safeguard for incorrect city name or API issues
    if data.get('cod') != 200:
        description = "City not found"
        icon = ""
        temp = ""
    else:
        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

    day = datetime.date.today()
    
    context = {
        'description': description,
        'icon': icon,
        'temp': temp,
        'day': day,
        'city': city,
    }

    return render(request, 'index.html', context)