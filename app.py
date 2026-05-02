from flask import Flask, render_template, request
import requests

from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    weather_list = []
    weather_data = None

    if request.method == 'POST':

        if request.form.get('remove'):
           city_to_remove = request.form.get("remove")
           weather_list = [w for w in weather_list if w["city"] != city_to_remove]
        
        else:
            city = request.form.get('city')

            if city:    
               url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
               response = requests.get(url).json()

               if response.get("cod") == 200:
                  weather_data = {
                      "city": response["name"],
                      "temp": response["main"]["temp"],
                      "desc": response["weather"][0]["description"]
                }
                  
    if not any(w["city"] == response["name"] for w in weather_list):
        weather_list.append(weather_data)    
         
    return render_template('index.html', weather=weather_data, weather_list=weather_list)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)