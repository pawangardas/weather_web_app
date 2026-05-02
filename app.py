from flask import Flask, render_template, request
import requests

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            api_key = os.getenv("API_KEY")  # Replace with your OpenWeatherMap API key
            print("API KEY:", api_key, flush=True)
            
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)

            print(response.text)
            if response.status_code == 200:
                data = response.json()
                weather_data = {
                    'city': data['name'],
                    'temperature': data['main']['temp'],
                    'description': data['weather'][0]['description'],
                    'icon': data['weather'][0]['icon']
                }
            else:
                weather_data = {'error': 'City not found'}
    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)