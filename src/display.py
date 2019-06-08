import pygame
import pprint

pygame.init()
pygame.mouse.set_visible(0)

fancyFont = 'fonts/Aladin-Regular.ttf'
plainFont = 'freesansbold.ttf'

white = (255, 255, 255)
purple = (57,2,68)
pale = (209,203,211)

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
        self.erase(70,25,119,119)
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
        startIndex = self.findStartOfWeatherRange(rawData,now)
        finishIndex = startIndex + 7
        for i in range(startIndex,finishIndex):
            pprint.pprint(rawData[i])

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
    def __init__(self,data):
        self.data = data

    def render(self):
        rainRisk # Pp
        rainRiskColour # infer
        weatherIcon # W
        temperature # T
        temperatureColour #infer
        time # $ minutes since midnight
        # Uv index?