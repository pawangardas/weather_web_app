from flask import Flask, render_template, request
import requests

from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    weather_list = []
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')
            
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            response = requests.get(url)

                    if response.get("cod") == 200:
            weather_data = {
                "city": response["name"],
                "temp": response["main"]["temp"],
                "desc": response["weather"][0]["description"]
            }

            weather_list.append(weather_data)

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)