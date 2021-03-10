import pygame

class Player():
    def __init__(self, game):
        self.mode = game.mode
        self.icon = pygame.image.load('media/cardboard_box.png')

        self.width = self.icon.get_width()
        self.height = self.icon.get_height()

        self.rect = self.icon.get_rect()
        self.rect.center = game.mode.get_rect().center
        
        self.speed = 24

    def blit_player(self):
        self.mode.blit(self.icon, self.rect)