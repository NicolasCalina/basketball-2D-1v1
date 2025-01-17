from utils import *
import pygame

class Basketball(pygame.sprite.Sprite):
    MAX_SPEED = 500
    
    def __init__(self, groups, players_group):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            pygame.image.load(join("../", "resources", "sprites", "basketball.png")).convert_alpha(),
            (35, 35)
        )
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.old_rect = self.rect.copy()
        
        # Motion variables
        self.speed = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 1)
        self.gravity = 200
        self.friction = 0.8
        self.horizontal_friction = 0.8
        
        self.floor = WINDOW_HEIGHT - 70
        self.players_group = players_group

    def cap_speed(self):
        if self.speed.length() > self.MAX_SPEED:
            self.speed = self.speed.normalize() * self.MAX_SPEED

    def collision_with_players(self, direction):
        collided_player = pygame.sprite.spritecollide(self, self.players_group, False)
        if collided_player:
            player = collided_player[0]

            if direction == "horizontal":
                if self.rect.right > player.rect.left and self.old_rect.right <= player.old_rect.left:
                    self.rect.right = player.rect.left
                    self.direction.x = -1
                    self.speed.x += player.speed.x * 0.1
                            
                if self.rect.left <= player.rect.right and self.old_rect.left >= player.old_rect.right:
                    self.rect.left = player.rect.right
                    self.direction.x = 1
                    self.speed.x += player.speed.x * 0.1     

            if direction == "vertical":
                if self.rect.bottom >= player.rect.top and self.old_rect.bottom <= player.old_rect.top:
                    self.rect.bottom = player.rect.top
                    self.direction.y = -1
                    self.speed.y = 300
                if self.rect.top <= player.rect.bottom and self.old_rect.top >= player.old_rect.bottom:
                    self.rect.top = player.rect.bottom
                    player.speed.y = 0
                    self.speed.y = 0
            
            # Cap speed after collision
            self.cap_speed()

    def screen_collision_vertical(self):
        if self.rect.bottom >= self.floor:
            self.rect.bottom = self.floor
            self.speed.y *= self.friction * -1
            self.cap_speed()
            
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y = 1
            self.speed.y *= self.friction * -1
            self.cap_speed()

    def screen_collision_horizontal(self):
        if self.rect.left <= 0:
            self.rect.left = 0
            self.direction.x *= -1
            self.speed.x *= self.friction
            self.cap_speed()
            
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.direction.x *= -1
            self.speed.x *= self.friction
            self.cap_speed()
        
    def vertical_movement(self, dt):
        self.screen_collision_vertical()
            
        self.speed.y += self.gravity * dt
        self.rect.centery += self.direction.y * self.speed.y * dt
        self.cap_speed()

        if abs(self.speed.y) < 1:
            self.speed.y = 0

    def horizontal_movement(self, dt):
        self.screen_collision_horizontal()
        
        self.speed.x -= self.horizontal_friction 
        self.rect.centerx += self.speed.x * self.direction.x * dt
        self.cap_speed()

        if abs(self.speed.x) < 1:
            self.speed.x = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        
        self.vertical_movement(dt)
        self.collision_with_players("vertical")
        
        self.horizontal_movement(dt)
        self.collision_with_players("horizontal")