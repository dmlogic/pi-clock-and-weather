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
    actions = None

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
        self.actions = {
            "uv":False,
            "wet":0,
            "cold":False,
        }
        self.erase(25,258,750,197)
        startIndex = self.findStartOfWeatherRange(rawData,now)
        finishIndex = startIndex + 7
        instance = 0
        for i in range(startIndex,finishIndex):
            fc = Forecast(rawData[i])
            offset = 25 + (instance * 107)
            screen.blit(fc.render(), (offset,258))
            if(self.isRelevantToActions(rawData[i]["timestamp"][0].hour,now.hour)):
                self.updateActionValues(rawData[i])
            instance +=1

    def isRelevantToActions(self,hour,now):
        if(hour > now and hour >= 9 and hour <= 18):
            return True
        return False

    def updateActionValues(self,data):
        # UV index above 5 is a flag
        if(data["U"][0] > 5):
            self.actions["uv"] = True

        # 30% chance of rain counts as one warning score
        if(data["Pp"][0] >= 30):
            self.actions["wet"] +=1

        # Anything 5 degrees or below is cold
        if(data["T"][0] <= 5):
            self.actions["cold"] = True

    def displayActions(self):
        # Any UV warning in the day gives an icon
        if(self.actions["uv"]):
            uvIcon = pygame.image.load('images/suncream.png')
            screen.blit(uvIcon,(405,143))
        # Rain score of 2 or more gives an icon
        if(self.actions["wet"] > 1):
            uvIcon = pygame.image.load('images/umbrella.png')
            screen.blit(uvIcon,(528,143))
        # Cold warning gives icon
        if(self.actions["cold"]):
            uvIcon = pygame.image.load('images/hat.png')
            screen.blit(uvIcon,(651,143))

    def findStartOfWeatherRange(self,rawData,now):
        startHour = now.strftime("%Y-%m-%d ") + str(now.hour - now.hour%3)
        for i in range(len(rawData)):
            forecastHour = rawData[i]["timestamp"][0].strftime("%Y-%m-%d %-H")
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
    temperatureColours = {
        "-10":(127,141,184),
        "-9":(139,152,191),
        "-8":(152,164,198),
        "-7":(162,172,203),
        "-6":(175,184,211),
        "-5":(187,194,217),
        "-4":(198,204,223),
        "-3":(211,215,230),
        "-2":(222,226,237),
        "-1":(234,237,243),
        "0":(245,246,250),
        "1":(255,249,232),
        "2":(255,245,217),
        "3":(255,241,202),
        "4":(255,237,186),
        "5":(255,234,172),
        "6":(255,229,155),
        "7":(255,226,141),
        "8":(255,222,125),
        "9":(255,218,109),
        "10":(255,215,101),
        "11":(255,210,98),
        "12":(255,204,95),
        "13":(255,199,92),
        "14":(255,194,89),
        "15":(255,189,86),
        "16":(255,184,83),
        "17":(255,179,80),
        "18":(255,173,77),
        "19":(255,168,74),
        "20":(255,164,71),
        "21":(255,158,68),
        "22":(255,153,66),
        "23":(255,148,62),
        "24":(255,143,59),
        "25":(255,138,57),
        "26":(255,131,53),
        "27":(254,125,51),
        "28":(250,116,51),
        "29":(248,109,51),
        "30":(243,98,51),
        "31":(239,87,51),
        "32":(235,78,51),
        "33":(231,68,51),
        "34":(227,58,51),
        "35":(222,46,51),
        "36":(218,36,51),
        "37":(214,25,51),
        "38":(209,13,51),
        "39":(205,3,51),
        "40":(195,0,49),
    }

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
        t = self.data["T"][0]
        panel = pygame.Surface((51, 38))
        panel.fill(self.getTempColour(t))
        theTemp = self.font.render(str(t)+'°', True, black)
        fontRect  = theTemp.get_rect()
        fontRect.center = (27,19)
        panel.blit(theTemp, fontRect )
        tempRect  = panel.get_rect()
        tempRect.center = (52,130)
        self.tile.blit(panel, tempRect )

    def getTempColour(self,t):
        if(t < -10):
            return self.temperatureColours["-10"]
        if(t > 40):
            return self.temperatureColours["40"]
        return self.temperatureColours[str(t)]

    def render(self):
        self.setIcon()
        self.setTime()
        self.setRainLikelihood()
        self.setTemperature()
        return self.tile
