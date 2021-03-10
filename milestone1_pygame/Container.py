import pygame
from pygame.sprite import Sprite

class Container(Sprite):
    def __init__(self, game):
        super().__init__()
        self.mode = game.mode
        self.image = pygame.image.load('media/container.png')
        self.rect = self.image.get_rect()
        self.height = self.image.get_height()

        # Initial object positions
        self.rect.x = 16
        self.rect.y = game.length + self.height