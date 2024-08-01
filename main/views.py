from django.shortcuts import render
# import json to load json data to python dictionary
import json
# urllib.request to make a request to api
import urllib.request

from django.conf import settings


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        ''' api key might be expired use your own api_key 
			place api_key in place of appid ="your_api_key_here " '''

        # source contain JSON data from API

        source = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + settings.WEATHER_API_KEY).read()

        # converting JSON data to a dictionary
        list_of_data = json.loads(source)

        # Extract and convert temperature from Kelvin to Celsius
        temp_kelvin = list_of_data['main']['temp']
        temp_celsius = temp_kelvin - 273.15

        # data for variable list_of_data
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ' '
            + str(list_of_data['coord']['lat']),
            "temp": str(temp_celsius) + '°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request, "main/index.html", data)
