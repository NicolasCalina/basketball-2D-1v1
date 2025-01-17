from utils import *

class Hand(pygame.sprite.Sprite):
    def __init__(self, groups,player,  images, controls, offset, basketball, which_player):
        super().__init__(groups)
        self.images = images
        self.current_frame_indx = 0
        self.image = self.images[self.current_frame_indx]
        self.rect = self.image.get_frect()
        self.old_rect = self.rect.copy()
        
        self.offset = offset
        self.controls = controls
        
        self.player = player
        
        self.which_player = which_player
        
        self.is_raising = False
        self.raising_time = 0
        self.animation_duration = 1
        
        self.basketball = basketball
        
    def follow_player(self):
            self.rect.topleft = (self.player.rect.left + self.offset[0] , self.player.rect.top + self.offset[1])
            if self.which_player == 2 and self.current_frame_indx == 1:
                self.rect.topleft = (self.player.rect.left - 60 , self.player.rect.top + 40)
        
    def animate(self, dt):
        if self.is_raising:
            self.raising_time += dt
            if self.raising_time >= self.animation_duration:
                self.is_raising = False
                self.raising_time = 0
                self.current_frame_indx = 0
            else:
                self.current_frame_indx = 1 if self.raising_time % 0.2 < 1 else 0
                self.image = self.images[self.current_frame_indx]
                self.rect = self.image.get_frect()
        else:
            self.current_frame_indx = 0

            self.image = self.images[self.current_frame_indx]
            self.rect = self.image.get_frect()
        
    
    def collision_with_ball(self):
        collided_hand = pygame.FRect.colliderect(self.rect, self.basketball.rect)
        if collided_hand:
            if self.basketball.rect.bottom >= self.rect.top and self.basketball.old_rect.bottom <= self.old_rect.top:
                self.basketball.rect.bottom = self.rect.top
                self.basketball.direction.y *= -1
                self.basketball.speed.y += 20
    def update(self, dt):
        self.old_rect = self.rect.copy()
        
        self.collision_with_ball()
        self.animate(dt)
        self.follow_player()
        
        keys = pygame.key.get_pressed()
        
        if keys[self.controls["down"]]:
            if not self.is_raising:
                self.is_raising = True
                self.current_frame_indx = 0
                self.raising_time = 0
                self.image = self.images[self.current_frame_indx]

            
        