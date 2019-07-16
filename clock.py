import time
import pygame
import config
import pprint
from src import backlight
from src import metoffer
from src import weather
from src import clock
from src import display
from threading import Timer,Thread,Event

weather = weather.Data( metoffer.MetOffer(config.metoffice_key) )
clock = clock.DateTime()
display = display.Display()
backlight = backlight.Backlight(config.backlight_delay)

class Tocker(Thread):
    def __init__(self, event,clock):
        Thread.__init__(self)
        self.stopped = event
        self.clock = clock

    def run(self):
        while not self.stopped.wait(0.5):
            if(backlight.state == 'off'):
                continue
            display.tick()
            if(clock.isNewMinute()):
                display.updateMinute(clock.minute())
                if(clock.isNewHour()):
                    display.updateHour(clock.hour())
                    display.updateDate(clock.day(),clock.fullDate())
                    try:
                        display.updateWeatherSummary(weather.daySummary())
                        display.updateWeatherForecast(weather.forecast(),clock.theTime())
                        display.displayActions()
                    except:
                        print('something up with metoffice')
            display.update()

stopFlag = Event()
thread = Tocker(stopFlag,clock)
thread.start()

while True :
    for event in pygame.event.get() :
        # Quit
        if event.type == pygame.QUIT :
            quit()
        if(event.type == pygame.MOUSEBUTTONDOWN and config.backlight_control):
            state = backlight.toggle()
            if(state == 'off'):
                clock.reset()
