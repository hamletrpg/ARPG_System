import pygame as pg
from settings import *
from entities import Player, Enemy

class Game:
    def __init__(self):
        pg.init()
        pg.font.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.player = Player(self, *PLAYER_ATT_1.values())
        self.enemy = Enemy(self, *ENEMY_ATT_1.values())

        self.all_sprites.add(self.enemy)
        self.all_sprites.add(self.player)
        self.run()

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()

    def update(self):
        self.player.update()
        self.enemy.update()

    def event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
            self.running = False
            self.player.use_weapon(event)

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.player.rotate_image()
        pg.display.flip()

g = Game()
while g.running:
    g.new()

pg.quit()