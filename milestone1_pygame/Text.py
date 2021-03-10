import pygame.font

class Text:
    def __init__(self, game, info, font_size):
        self.length = game.length

        self.background = game.sets.background_color
        self.foreground = (0, 0, 0)

        self.font = pygame.font.SysFont('Calibri', font_size, bold = True)

        self.msg = self.font.render(info, True, self.foreground, self.background)
        self.msg_rect = self.msg.get_rect()

        game.mode.blit(self.msg, self.msg_rect)