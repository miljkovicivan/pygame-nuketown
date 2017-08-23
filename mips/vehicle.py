import pygame
from pygame.locals import KEYDOWN, K_LEFT, K_RIGHT, K_UP, K_DOWN

from mips import utils


class Vehicle:
    def __init__(self, image_filename, x, y, surface):
        self.sprite = pygame.image.load(image_filename)
        self._x = x
        self._y = y
        self.surface = surface

    def draw(self):
        """The render method."""
        self.surface.blit(self.sprite, (self._x, self._y))

    def update(self, event):
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                self._x -= 70 + utils.mistake()
                # sprite=pygame.image.load('left.png')
            elif event.key == K_RIGHT:
                self._x += 70 + utils.mistake()
                # sprite=pygame.image.load('right.png')
            elif event.key == K_UP:
                self._y -= 50 + utils.mistake()
                # sprite=pygame.image.load('up.png')
            elif event.key == K_DOWN:
                self._y += 50 + utils.mistake()
                # sprite=pygame.image.load('down.png')
