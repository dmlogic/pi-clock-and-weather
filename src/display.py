import pygame
from threading import Timer

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
WIDTH = 400
HEIGHT = 400

class Display:

    def __init__(self,clock):
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT ))
        self.clock = clock
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.display_surface.fill(white)
        self.update()

    def updateTime(self):
        print("Update time")
        theTime = self.font.render(self.clock.hour()+self.clock.second()+self.clock.minute(), True, green)
        timeRect = theTime.get_rect()
        timeRect.center = (WIDTH // 2, HEIGHT // 2)
        self.display_surface.blit(theTime, timeRect)
        self.update()
        Timer(5, self.updateTime)

    def updateDate(self):
        theDate = self.font.render(self.clock.fullDate(), True, green, blue)
        self.display_surface.blit(theDate, (50,50))

    def update(self):
        self.updateDate()
        pygame.display.update()