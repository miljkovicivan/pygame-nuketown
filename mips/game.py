import pygame, sys, time
from pygame.locals import QUIT

from mips.vehicle import Vehicle


FPS = 30


UP = 'up'
LEFT = 'left'
RIGHT = 'right'
DOWN = 'down'


def run():
    """Main game loop."""
    pygame.init()

    fps_clock = pygame.time.Clock()

    width = 700
    height = 500
    displaysurf = pygame.display.set_mode((width, height), 0, 32)
    pygame.display.set_caption('Animation')
    background = pygame.image.load('bg.png')

    drawables = []
    updatables = []

    vehicle = Vehicle('down.png', x=0, y=0, surface=displaysurf)
    drawables.append(vehicle)
    updatables.append(vehicle)

    while True:
        displaysurf.blit(background, (0, 0))

        for drawable in drawables:
            drawable.draw()

        for event in pygame.event.get():
            for updatable in updatables:
                updatable.update(event)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fps_clock.tick(FPS)


if __name__ == "__main__":
    run()
