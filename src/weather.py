import config
from src import metoffer
from threading import Timer

class Data:
    client = None
    siteId = None

    def __init__(self,client):
        self.client = client
        self.siteId = self.client.find_site(config.lat,config.lng,metoffer.DAILY)

    def daySummary(self):
        today = self.client.loc_forecast(self.siteId, metoffer.DAILY)
        return((today["SiteRep"]["DV"]["Location"]["Period"][0]["Rep"][0]["Dm"],today["SiteRep"]["DV"]["Location"]["Period"][1]["Rep"][1]["Nm"]))


    def forecast(self):
        loc = self.client.nearest_loc_forecast(config.lat, config.lng, metoffer.THREE_HOURLY)
        return metoffer.Weather(loc)
