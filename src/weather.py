import config
from src import metoffer
from threading import Timer

class Data:

    def __init__(self,client):
        self.client = client

    def forecast(self):
        loc = self.client.nearest_loc_forecast(config.lat, config.lng, metoffer.THREE_HOURLY)
        return metoffer.Weather(loc)
