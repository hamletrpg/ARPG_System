import pygame as pg
from settings import *
import os
import math

class Weapon(pg.sprite.Sprite):
    def __init__(self, game, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pg.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.time = pg.time.get_ticks()

    def update(self):
        if self.time is not None:
            if pg.time.get_ticks() - self.time >= 100:
                self.kill()
