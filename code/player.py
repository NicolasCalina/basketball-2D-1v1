from utils import *

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, image, controls, position, padding):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect( center = position )
        self.old_rect = self.rect.copy()
        
        self.direction = pygame.Vector2()
        self.horizontal_speed = 400
        self.vertical_speed = 0
        self.gravity = 0.5
        self.is_on_floor = True
        self.controls = controls
        self.padding = padding

        
    def move(self, dt):
        self.rect.centerx += self.direction.x * self.horizontal_speed * dt
        
    def jump(self,dt, keys):
        if ( keys[self.controls["jump"]] and self.is_on_floor ):
            self.vertical_speed = -15
            self.direction.y = 1
            self.is_on_floor = False
        self.rect.centery += self.direction.y * self.vertical_speed * dt * 100
        self.vertical_speed += self.gravity
        
    def update(self,dt):
        self.old_rect = self.rect.copy()
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[self.controls["right"]] - keys[self.controls["left"]])
        self.move(dt)
        self.jump(dt, keys)
        if ( self.rect.bottom >= WINDOW_HEIGHT - self.padding):
            self.rect.bottom = WINDOW_HEIGHT - self.padding
            self.is_on_floor = True
            self.direction.y = 0
        