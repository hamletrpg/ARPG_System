import math
import os
from weapon import Weapon
import pygame as pg
import settings
from data_work import load_image
from settings import E_PIC_DICTIONARY

vec = pg.math.Vector2

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
        self.image.set_colorkey(settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.weapon = None

    def check_if_alive(self):
        self.draw_hp(self.game.screen)
        if self.hp <= 0:
            self.kill()


class Player(Character):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        super().__init__(game, name, x, y, w, h, atk, hp)
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

        if self.weapon:
            self.weapon.update()

        self.check_if_alive()

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
            self.weapon = Weapon(self.game, self.rect.x, self.rect.y - 32, 32, 32)
            self.weapon.image = pg.transform.rotate(pg.image.load(os.path.join("sword.png")).convert_alpha(), 0)
            self.game.all_sprites.add(self.weapon)
            self.basic_attack(self.game.enemy)
        elif event.type == pg.MOUSEBUTTONDOWN and self.get_angle() in range(-136, -57):
            self.weapon = Weapon(self.game, self.rect.x + 32, self.rect.y, 32, 32)
            self.weapon.image = pg.transform.rotate(pg.image.load(os.path.join("sword.png")).convert_alpha(), 270)
            self.game.all_sprites.add(self.weapon)
            self.basic_attack(self.game.enemy)
        elif event.type == pg.MOUSEBUTTONDOWN and self.get_angle() in range(-222, -137):
            self.weapon = Weapon(self.game, self.rect.x, self.rect.y + 32, 32, 32)
            self.weapon.image = pg.transform.rotate(pg.image.load(os.path.join("sword.png")).convert_alpha(), 180)
            self.game.all_sprites.add(self.weapon)
            self.basic_attack(self.game.enemy)
        elif event.type == pg.MOUSEBUTTONDOWN and (self.get_angle() in range(52, 90) or self.get_angle() in range(-269, -237)):
            self.weapon = Weapon(self.game, self.rect.x - 32, self.rect.y, 32, 32)
            self.weapon.image = pg.transform.rotate(pg.image.load(os.path.join("sword.png")).convert_alpha(), 90)
            self.game.all_sprites.add(self.weapon)
            self.basic_attack(self.game.enemy)

    def basic_attack(self, target):
        if self.weapon:
            if self.weapon.rect.colliderect(target):
                raw_damage = target.hp - self.atk
                target.hp = raw_damage


class Enemy(Character):
    def __init__(self, game, name, x, y, w, h, atk, hp):
        super().__init__(game, name, x, y, w, h, atk, hp)
        self.index = 0
        self.idle = []
        self.load_images()
        self.elapsed = 0
        self.speed = 0


    def load_images(self):
        for dirr, values in E_PIC_DICTIONARY.items():
            for value in values:
                if dirr == "Monster":
                    self.idle.append(load_image(self, dirr, value))

    def animation(self):
        now = pg.time.get_ticks()
        if now - self.elapsed > 250:
            self.elapsed = now
            self.index += 1
            try:
                if self.index >= len(self.idle):
                    self.index = 0
                self.image = self.idle[self.index]
            except IndexError:
                self.index = 0
        self.image.set_colorkey(settings.BLACK)

    def update(self):
        self.check_if_alive()
        self.animation()
        if self.alive():
            self.move_towards_player(self.game.player)

    def move_towards_player(self, player):
        dirvect = vec(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        if dirvect.length() > 0:
            dirvect.normalize()
            dirvect.scale_to_length(self.speed)
            self.rect.move_ip(dirvect)
        else:
            self.rect.x -= 32
            self.rect.y -= 32

