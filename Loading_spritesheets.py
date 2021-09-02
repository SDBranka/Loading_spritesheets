import pygame
import spritesheet

# initialize pygame
pygame.init()

# screen set up
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
# change the title of the displayed in display window
pygame.display.set_caption("Loading SpriteSheets")

# load spritesheet image
spritesheet_image = pygame.image.load("doux.png").convert_alpha()
# create instance of Spritesheet class
sprite_sheet = spritesheet.Spritesheet(spritesheet_image)

# set background color
background = (50, 50, 50)

# defining the color black to later remove color from png backgrounds
BLACK = (0, 0, 0)


frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)
frame_1 = sprite_sheet.get_image(1, 24, 24, 3, BLACK)
frame_2 = sprite_sheet.get_image(2, 24, 24, 3, BLACK)
frame_3 = sprite_sheet.get_image(3, 24, 24, 3, BLACK)


run = True
while run:

    # applies background color to screen
    screen.fill(background)

    # display frame image
    screen.blit(frame_0, (0, 0))
    screen.blit(frame_1, (100, 0))
    screen.blit(frame_2, (200, 0))
    screen.blit(frame_3, (300, 0))



    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()