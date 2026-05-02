# Weather Application

A Flask web application that fetches and displays weather information for a given city using the OpenWeatherMap API.

## Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment: `venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install flask requests`
4. Get an API key from [OpenWeatherMap](https://openweathermap.org/api)
5. Replace 'YOUR_API_KEY' in app.py with your actual API key
6. Run the app: `python app.py`

## Features

- Input city name to get current weather
- Display temperature, description, and weather icon
- Error handling for invalid cities