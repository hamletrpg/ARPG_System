import pygame as pg
from settings import *

class Weapon(pg.sprite.Sprite):
    def __init__(self, x, y, w, h, atk):
        pg.sprite.Sprite.__init__(self)
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

