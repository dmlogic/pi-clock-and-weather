import pygame
import pprint

pygame.init()
pygame.mouse.set_visible(0)

fancyFont = 'fonts/Aladin-Regular.ttf'
plainFont = 'fonts/Arial.ttf'

white = (255, 255, 255)
purple = (57,2,68)
pale = (209,203,211)
black = (51,51,51)
rain = (28,116,153)

screen = pygame.display.set_mode((800, 480))
timeFont = pygame.font.Font(fancyFont, 120)
dateFont = pygame.font.Font(fancyFont, 48)
summaryFont = pygame.font.Font(fancyFont, 37)
background = pygame.image.load('images/background.png')


class Display:
    ticktock = True

    def __init__(self):
        screen.blit(background,(0,0))
        self.update();

    def tick(self):
        self.erase(201,35,27,86)
        self.ticktock = not self.ticktock
        if(self.ticktock):
            return
        theSecond = timeFont.render(':', True, purple)
        secondRect = theSecond.get_rect()
        secondRect.center = (210,79)
        screen.blit(theSecond, secondRect)

    def updateMinute(self,value):
        self.erase(225,25,125,119)
        theMinute = timeFont.render(value, True, purple)
        minuteRect = theMinute.get_rect()
        minuteRect.left = 225
        minuteRect.top = 16
        screen.blit(theMinute, minuteRect)

    def updateHour(self,value):
        self.erase(70,25,139,119)
        theHour = timeFont.render(value, True, purple)
        hourRect = theHour.get_rect()
        hourRect.right = 198
        hourRect.top = 16
        screen.blit(theHour, hourRect)

    def updateWeatherSummary(self,summary):
        self.erase(25,143,375,115)
        minTemp = summaryFont.render('min '+summary[1]+'°', True, pale)
        minRect = minTemp.get_rect()
        minRect.right = 198
        minRect.top = 174
        screen.blit(minTemp, minRect)

        maxTemp = summaryFont.render('max '+summary[0]+'°', True, pale)
        maxRect = maxTemp.get_rect()
        maxRect.left = 214
        maxRect.top = 174
        screen.blit(maxTemp, maxRect)

    def updateWeatherForecast(self,rawData,now):
        self.erase(25,258,750,197)
        startIndex = self.findStartOfWeatherRange(rawData,now)
        finishIndex = startIndex + 7
        instance = 0
        for i in range(startIndex,finishIndex):
            fc = Forecast(rawData[i])
            offset = 25 + (instance * 107)
            screen.blit(fc.render(), (offset,258))
            instance +=1

    def findStartOfWeatherRange(self,rawData,now):
        startHour = now.strftime("%Y-%m-%d ") + str(now.hour - now.hour%3)
        for i in range(len(rawData)):
            forecastHour = rawData[i]["timestamp"][0].strftime("%Y-%m-%d %H")
            if(forecastHour == startHour):
                return i
        return 0

    def erase(self,x,y,w,h):
        screen.blit(background, (x, y), pygame.Rect(x, y, w, h))
        pygame.display.update()

    def updateDate(self,dayName,fullDate):
        self.erase(405,25,370,119)
        theDay = dateFont.render(dayName, True, purple)
        dayRect = theDay.get_rect()
        dayRect.center = (587,57)
        screen.blit(theDay, dayRect)

        theDate = dateFont.render(fullDate, True, purple)
        dateRect = theDate.get_rect()
        dateRect.center = (587,109)
        screen.blit(theDate, dateRect)

    def update(self):
        pygame.display.flip()

class Forecast:
    data = None
    tile = None
    font = None
    def __init__(self,data):
        self.data = data
        self.setTile()
        self.font = pygame.font.Font(plainFont, 20)
#
    def setTile(self):
        self.tile = pygame.Surface((105, 196), pygame.SRCALPHA, 32)
        self.tile = self.tile.convert_alpha()

    def setIcon(self):
        icon = pygame.image.load('images/weather_icons/'+str(self.data["W"][0])+'.png')
        self.tile.blit(icon,(15,40))

    def setTime(self):
        theTime = self.font.render(self.data["timestamp"][0].strftime("%H:00"), True, black)
        timeRect = theTime.get_rect()
        timeRect.center = (51,170)
        self.tile.blit(theTime, timeRect)

    def setRainLikelihood(self):
        chance = self.data["Pp"][0]
        if(chance <= 30):
            colour = black
        else:
            colour = rain
        theRain = self.font.render(str(chance)+'%', True, colour)
        rainRect  = theRain.get_rect()
        rainRect .center = (51,24)
        self.tile.blit(theRain, rainRect )

    def setTemperature(self):
        theTemp = self.font.render(str(self.data["T"][0])+'°', True, black)
        tempRect  = theTemp.get_rect()
        tempRect .center = (51,130)
        self.tile.blit(theTemp, tempRect )

    def render(self):
        self.setIcon()
        self.setTime()
        self.setRainLikelihood()
        self.setTemperature()
        return self.tile
        # temperature # T
        # temperatureColour #infer
