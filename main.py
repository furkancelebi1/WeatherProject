import requests

api_key = '2f03dfb14a43e4f600e60c04413d2cbb'

city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    desc = data['weather'][0]['description']
    print(f'Temperature: {temp_celsius:.2f}°C')
    print(f'Description: {desc}')
else:
    print('Error fetching weather data')
