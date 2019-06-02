import pygame

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
WIDTH = 800
HEIGHT = 480


class Display:

    theDate = None
    timeRect = None
    font = None
    display_surface = None

    def __init__(self):
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.display_surface.fill(white)

    def updateTime(self,value):
        theTime = self.font.render(value, True, green)
        self.timeRect = theTime.get_rect()
        self.timeRect.center = (WIDTH // 2, HEIGHT // 2)
        blank = pygame.Surface((self.timeRect.width,self.timeRect.height))
        blank.fill(white)
        self.display_surface.blit(blank, self.timeRect)
        self.display_surface.blit(theTime, self.timeRect)
        # print("Update time to "+value)

    def updateDate(self,value):
        self.theDate = self.font.render(value, True, green, blue)
        self.display_surface.blit(self.theDate, (50,50))

    def update(self):
        # print("update the things")
        pygame.display.update()