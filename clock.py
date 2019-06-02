import time
import pygame
import credentials
from src import backlight
from src import metoffer
from src import weather
from src import clock
from src import display
from threading import Timer,Thread,Event

backlight = backlight.Backlight(5)
# weather = weather.Data( metoffer.MetOffer(credentials.metoffice_key) )
clock = clock.DateTime()
display = display.Display()

class Tocker(Thread):
    def __init__(self, event,clock):
        Thread.__init__(self)
        self.stopped = event
        self.clock = clock

    def run(self):
        while not self.stopped.wait(0.5):
            # print('tick')
            if(clock.isNewSecond()):
                # print('tock')
                display.updateTime(clock.hour()+clock.second()+clock.minute());
                if(clock.isNewHour()):
                    display.updateDate(clock.fullDate());
                display.update()

stopFlag = Event()
thread = Tocker(stopFlag,clock)
thread.start()
# forecast = weather.forecast()
# pprint.pprint(forecast.data)
while True :
    for event in pygame.event.get() :
        # Quit
        if event.type == pygame.QUIT :
            quit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            backlight.toggle()
