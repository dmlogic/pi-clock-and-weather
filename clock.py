import time
import pygame
import credentials
from src import backlight
from src import metoffer
from src import weather
from src import clock
from src import display
from threading import Timer

backlight = backlight.Backlight(5)
# weather = weather.Data( metoffer.MetOffer(credentials.metoffice_key) )

display = display.Display( clock.DateTime() )
display.updateTime();
Timer(5, display.updateTime)
# forecast = weather.forecast()
# pprint.pprint(forecast.data)
while True :

    for event in pygame.event.get() :
        # Quit
        if event.type == pygame.QUIT :
            quit()
        if(event.type == pygame.MOUSEBUTTONDOWN):
            backlight.toggle()

        display.update()
