import pygame

pygame.init()
pygame.mouse.set_visible(0)

fancyFont = 'fonts/Aladin-Regular.ttf'
plainFont = 'freesansbold.ttf'

white = (255, 255, 255)
purple = (57,2,68)

screen = pygame.display.set_mode((800, 480))
timeFont = pygame.font.Font(fancyFont, 120)
dateFont = pygame.font.Font(fancyFont, 48)
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