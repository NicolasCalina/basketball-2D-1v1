from utils import *

class Hand(pygame.sprite.Sprite):
    def __init__(self, groups,player,  images, controls, offset, which_player):
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
        self.animation_duration = 0.5
        
    def follow_player(self):
        if self.which_player == 1:
            self.rect.topleft = (self.player.rect.left + self.offset[0] , self.player.rect.top + self.offset[1])
        else:
            self.rect.topright = (self.player.rect.right - self.offset[0], self.player.rect.top + self.offset[1])
        
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
        else:
            self.current_frame_indx = 0
            self.image = self.images[self.current_frame_indx]
        
    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.follow_player()
        self.animate(dt)
        
        keys = pygame.key.get_pressed()
        
        if keys[self.controls["down"]]:
            if not self.is_raising:
                self.is_raising = True
                self.current_frame_indx = 0
                self.raising_time = 0
                self.image = self.images[self.current_frame_indx]
            
        