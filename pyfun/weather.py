import requests
from .models.weather_response import WeatherResponse
from .models import map_json_to_object


class Weather(object):
    def __init__(self):
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.appid = "3b77e39b4d8a6e4c0611ad4f59c78f74"
        self.country_code = "us"

    def get_by_zip_code(self, zip_code):
        params = {"APPID": self.appid, 'q': f"{zip_code},{self.country_code}"}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            wr = WeatherResponse()
            map_json_to_object(wr, response.text)
            return wr
        else:
            print(f"Response was not 200, was actually {response.status_code}")
            return None


if __name__ == "__main__":
    w = Weather()
    w.get_by_zip_code("Rogers")
