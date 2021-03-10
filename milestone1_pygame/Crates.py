import pygame
from pygame.sprite import Sprite

class Crates(Sprite):
    def __init__(self, game):
        super().__init__()
        self.mode = game.mode

        self.image = pygame.image.load('media/crate.png')

        self.rect = self.image.get_rect()
        
        self.height = self.image.get_height()

        # Initial object positions
        self.rect.x = 16
        self.rect.y = 0 - self.height