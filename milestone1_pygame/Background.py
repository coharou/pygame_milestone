import pygame

class Background():
    def __init__(self, game):
        self.mode = game.mode
        self.background = pygame.image.load('media/ship_floor.png')
        self.background_rect = self.background.get_rect()

    def blit_background(self):
        self.mode.blit(self.background, self.background_rect)