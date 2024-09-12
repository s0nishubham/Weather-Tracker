import requests
from django.shortcuts import render
from django.conf import settings

def weather_app_dashboard(request):
    print("hi")
    api_key = settings.WEATHER_APP_API_KEY
    city = request.GET.get('city', 'London')
    url = f'https://api.tomorrow.io/v4/weather/realtime?location={city}&apikey=aPGMoqpqssS2TgrbRyjH5E08gUaS8TG4'

    response = requests.get(url)
    data = response.json()
    print("response",response)
    print("data",data)
    context = {
        'city': city,
        'temperature': data['data']['values']['temperature'] if response.status_code == 200 else 'N/A',
        # 'description': data['weather_app'][0]['description'] if response.status_code == 200 else 'N/A',
        # 'icon': data['weather_app'][0]['icon'] if response.status_code == 200 else '',
    }

    return render(request, 'dashboard.html', context)
