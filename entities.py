import math
import os

import pygame as pg

class Character(pg.sprite.Sprite):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.atk = atk
        self.hp = hp
        self.w = w
        self.h = h
        self.name = name
        self.image = pg.Surface((w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class Player(Character):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        super().__init__(game, name, x, y, w, h, atk, hp)
        # self.image = pg.image.load(os.path.join("Character1.png")).convert_alpha()
        self.correction_angle = 90

    def update(self):
        keys = pg.key.get_pressed()  # checking pressed keys
        if keys[pg.K_w]:
            self.rect.y -= 1
        if keys[pg.K_s]:
            self.rect.y += 1
        if keys[pg.K_d]:
            self.rect.x += 1
        if keys[pg.K_a]:
            self.rect.x -= 1

    def rotate_image(self):
        mx, my = pg.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle

        self.rot_image = pg.transform.rotate(pg.image.load(os.path.join("Character1.png")).convert_alpha(), angle)
        self.rot_image_rect = self.rot_image.get_rect(center=self.rect.center)
        self.game.screen.blit(self.rot_image, self.rot_image_rect.topleft)



class Enemy(Character):
    def __init__(self, game, name, x, y, w, h, color, atk, hp):
        super().__init__(game, name, x, y, w, h, color, atk, hp)
