import pygame
import sys
import random
import math

from Settings import Settings
from Background import Background
from Text import Text
from Score import Score

from Player import Player

from Crates import Crates
from Container import Container

class Main:
    def __init__(self):
        pygame.init()

        self.scoreObj = Score()
        self.lives = self.scoreObj.lives
        self.score = self.scoreObj.score
        self.difficulty = self.scoreObj.difficulty

        self.sets = Settings()
        self.length = self.sets.screen_length
        self.center = self.length / 2

        self.mode = pygame.display.set_mode((self.length, self.length))

        self.Background = Background(self)

        self.Player = Player(self)

        self.crates = pygame.sprite.Group()
        self.init_crates()

        self.containers = pygame.sprite.Group()
        self.init_containers()
    
    # METHODS RELATED TO THE CONTAINER OBJECTS

    def init_containers(self):
        container = self.build_container(80)
        container2 = self.build_container(288)

        self.containers.add(container, container2)
        self.container_height = container.height

    def build_container(self, x_position):
        container = Container(self)
        container.rect.x = x_position
        return container

    def update_container(self):
        for container in self.containers:
            if container.rect.y > 0 - self.container_height:
                if (self.random_value(16) == 1):
                    container.rect.y -= self.adjust_speed_by_diff(6)
            if container.rect.y <= 0 - self.container_height:
                container.rect.y = self.length + self.container_height

        isGameOver = self.has_container_collided()
        return isGameOver

    def has_container_collided(self):
        isGameOver = False
        if pygame.sprite.spritecollideany(self.Player, self.containers):
            isGameOver = True
        return isGameOver

    # METHODS RELATED TO THE CRATE OBJECTS

    def init_crates(self):
        crate = self.build_crate(16)
        crate2 = self.build_crate(160)
        crate3 = self.build_crate(224)
        crate4 = self.build_crate(368)

        self.crates.add(crate, crate2, crate3, crate4)
        self.crate_height = crate.height

    def build_crate(self, x_position):
        crate = Crates(self)
        crate.rect.x = x_position
        return crate

    def update_crates(self):
        for crate in self.crates:
            if crate.rect.y < (self.length + self.crate_height):
                if (self.random_value(8) == 1):
                    crate.rect.y += self.adjust_speed_by_diff(3)
            if crate.rect.y >= (self.length + self.crate_height):
                crate.rect.y = 0 - self.crate_height

        isGameOver = self.has_crate_collided()
        return isGameOver

    def has_crate_collided(self):
        isGameOver = False
        if pygame.sprite.spritecollideany(self.Player, self.crates):
            isGameOver = True
        return isGameOver

    # METHODS FOR RUNNING THE GAME

    def run(self):
        while True:
            isGameOver = False

            self.startup_screen()

            canGameRun = self.startup_events()

            while canGameRun == True:
                self.game_events()

                isGameOver = self.update_screen()

                self.update_score_difficulty()

                if isGameOver == True:
                    self.__init__()

    def startup_screen(self):
        self.mode.fill(self.sets.background_color)
        self.Text = Text(self, 'Milestone #1: click the screen or press ENTER to continue.', 16)
        pygame.display.flip()

    def startup_events(self):
        canGameRun = False

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_RETURN:
                    canGameRun = True
            elif e.type == pygame.MOUSEBUTTONDOWN:
                canGameRun = True

        return canGameRun

    # METHODS FOR THE GAME PLAY AREA

    def game_events(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_w:
                    if self.Player.rect.y > self.Player.height:
                        self.Player.rect.y -= self.Player.speed
                if e.key == pygame.K_a:
                    if self.Player.rect.x > self.Player.width:
                        self.Player.rect.x -= self.Player.speed
                if e.key == pygame.K_s:
                    if self.Player.rect.y < (self.length - self.Player.height * 2):
                        self.Player.rect.y += self.Player.speed
                if e.key == pygame.K_d:
                    if self.Player.rect.x < (self.length - self.Player.width * 2):
                        self.Player.rect.x += self.Player.speed
                if e.key == pygame.K_ESCAPE:
                    sys.exit()

    def update_screen(self):
        isGameOver = False
        didCrateCollide = False
        didContainerCollide = False

        didCrateCollide = self.update_crates()

        didContainerCollide = self.update_container()

        self.draw_all_objects()

        pygame.display.flip()

        if (self.score >= 50000):
            isGameOver = True

        if (didCrateCollide == True) or (didContainerCollide == True):
            self.lives -= 1
            if self.lives <= 0:
                isGameOver = True

        return isGameOver

    def draw_all_objects(self):
        self.Background.blit_background()

        self.Player.blit_player()

        self.crates.draw(self.mode)

        self.containers.draw(self.mode)

        self.draw_hud()

    def update_score_difficulty(self):
        self.score += 1

        if (self.score > 1000):
            self.difficulty = 1 + math.floor(self.score / 2500) * 0.1

    # METHODS TO DRAW THE HUD (game interface)

    def draw_hud(self):
        sHealth = self.make_hud_string_obj(self.lives)
        sScore = self.make_hud_string_obj(math.floor(self.score / 100))
        sDiff = self.make_hud_string_obj(self.difficulty)

        self.HUD = Text(self, f'Health : {sHealth}      Score : {sScore}      Difficulty : {sDiff}', 16)

    def make_hud_string_obj(self, value):
        sValue = str(value)
        return sValue

    # METHOD FOR ADJUSTING SPEED BY DIFFICULTY

    def adjust_speed_by_diff(self, base_speed):
        speed = base_speed * self.difficulty
        return speed

    # METHOD FOR RETURNING A RANDOM NUMBER

    def random_value(self, number):
        randnum = random.randrange(0, number)
        return randnum

if __name__ == '__main__':
    main = Main()
    main.run()