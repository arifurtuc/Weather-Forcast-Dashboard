import requests
import os
from dotenv import load_dotenv

# Load API key from environment variables
load_dotenv()
api_key = os.getenv("API_KEY")


def generate_weather_data(place, forecast_days, kind):
    """
    Fetches weather data based on the provided parameters.

    :param place: Location for weather data.
    :param forecast_days: Number of forecast days.
    :param kind: Type of weather data - 'Temperature' or 'Sky'.
    :return: Filtered weather data based on the kind specified.
    """
    url = ("http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&"
           f"appid={api_key}")
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    filtered_data = filtered_data[:8 * forecast_days]
    if kind == "Temperature":
        filtered_data = [dict["main"]["temp"] for dict in filtered_data]
    if kind == "Sky":
        filtered_data = [dict["weather"][0]["main"] for dict in filtered_data]
    return filtered_data
