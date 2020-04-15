import pygame
import os
from options import resolution, icon
from scr import life_screen

if __name__ == '__main__':
    # center the window
    os.environ['SDL_VIDEO_CENTERED'] = '1'

    pygame.init()

    # display stuff
    display = pygame.display.set_mode(resolution)
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Game of Life')

    life_screen(display)

    pygame.quit()
