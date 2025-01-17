from utils import *
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image, controls, position, padding):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.old_rect = self.rect.copy()
        
        self.direction = pygame.Vector2()
        self.speed = pygame.Vector2(400, 0)
        self.gravity = 1200
        self.is_on_floor = True
        self.controls = controls
        self.padding = padding

    def move(self, dt):
        self.rect.centerx += self.direction.x * self.speed.x * dt
        
    def jump(self, dt, keys):
        if keys[self.controls["jump"]] and self.is_on_floor:
            self.speed.y = -600
            self.direction.y = 1
            self.is_on_floor = False
        
        # Apply gravity
        self.speed.y += self.gravity * dt
        self.rect.centery += self.direction.y * self.speed.y * dt

    def update(self, dt):
        self.old_rect = self.rect.copy()
        
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[self.controls["right"]] - keys[self.controls["left"]])
        self.move(dt)
        self.jump(dt, keys)
        
        # Check if player is on the floor
        if self.rect.bottom >= WINDOW_HEIGHT - self.padding:
            self.rect.bottom = WINDOW_HEIGHT - self.padding
            self.is_on_floor = True
            self.speed.y = 0
            self.direction.y = 0