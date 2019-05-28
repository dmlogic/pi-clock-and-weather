import pygame
from src import backlight

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

# assigning values to X and Y variable
X = 400
Y = 400


# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y ))

# set the pygame window name
pygame.display.set_caption('Show Text')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)

# create a text suface object,
# on which text is drawn on it.
theTime = font.render('20:58', True, green)
theDate = font.render('15th May 2019', True, green, blue)

# create a rectangular object for the
# text surface object
timeRect = theTime.get_rect()

# set the center of the rectangular object.
timeRect.center = (X // 2, Y // 2)

backlight = backlight.Backlight(5)

# infinite loop
while True :

    # completely fill the surface object
    # with white color
    display_surface.fill(white)

    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(theTime, timeRect)
    display_surface.blit(theDate, (50,50))

    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get() :
        # Quit
        if event.type == pygame.QUIT :
            quit()

        if(event.type == pygame.MOUSEBUTTONDOWN):
            backlight.toggle()

        # Draws the surface object to the screen.
        pygame.display.update()