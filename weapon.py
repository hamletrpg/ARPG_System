import pygame as pg
from settings import *

class Weapon(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h, atk):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.atk = atk
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pg.Surface((w, h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = pg.time.get_ticks()

    def update(self):
        if self.time is not None:
            if pg.time.get_ticks() - self.time >= 100:
                # self.game.all_sprites.remove(self)
                self.kill()
                self.game.player.weapon = None
