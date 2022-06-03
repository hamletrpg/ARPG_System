import math
import os
from weapon import Weapon
import pygame as pg
import settings

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
        self.weapon = Weapon(self.game, 0, 0, 0, 0, 0)


class Player(Character):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        super().__init__(game, name, x, y, w, h, atk, hp)
        # self.image = pg.image.load(os.path.join("Character1.png")).convert_alpha()
        self.correction_angle = 90
        self.angle = 0

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

    def get_angle(self):
        mx, my = pg.mouse.get_pos()
        dx, dy = mx - self.rect.centerx, my - self.rect.centery
        self.angle = math.degrees(math.atan2(-dy, dx)) - self.correction_angle
        return int(self.angle)

    def rotate_image(self):

        self.rot_image = pg.transform.rotate(pg.image.load(os.path.join("Character1.png")).convert_alpha(), self.get_angle())
        self.rot_image_rect = self.rot_image.get_rect(center=self.rect.center)
        self.game.screen.blit(self.rot_image, self.rot_image_rect.topleft)


    def use_weapon(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and self.get_angle() in range(-36, 36):
            self.weapon = Weapon(self.game, self.rect.x, self.rect.y - 32, 32, 32, 20)
            self.game.all_sprites.add(self.weapon)

        elif event.type == pg.MOUSEBUTTONDOWN and self.get_angle() in range(-136, -57):
            self.weapon = Weapon(self.game, self.rect.x + 32, self.rect.y, 32, 32, 20)
            self.game.all_sprites.add(self.weapon)
        elif event.type == pg.MOUSEBUTTONDOWN and self.get_angle() in range(-222, -137):
            self.weapon = Weapon(self.game, self.rect.x, self.rect.y + 32, 32, 32, 20)
            self.game.all_sprites.add(self.weapon)
        elif event.type == pg.MOUSEBUTTONDOWN and (self.get_angle() in range(52, 90) or self.get_angle() in range(-269, -237)):
            self.weapon = Weapon(self.game, self.rect.x - 32, self.rect.y, 32, 32, 20)
            self.game.all_sprites.add(self.weapon)

class Enemy(Character):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        super().__init__(game, name, x, y, w, h, atk, hp)
        self.image.fill(settings.GREEN)
