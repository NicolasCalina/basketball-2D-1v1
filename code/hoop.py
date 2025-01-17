from utils import *

class Hoop(pygame.sprite.Sprite):
    def __init__(self, groups, image, position, basketball):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(topleft=position)
        self.old_rect = self.rect.copy()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.basketball = basketball
    
    def collision_with_ball(self):

        ball_mask = pygame.mask.from_surface(self.basketball.image)
        
        offset = (self.basketball.rect.left - self.rect.left, self.basketball.rect.top - self.rect.top)
        
        collision = self.mask.overlap(ball_mask, offset)
        if collision:
            
            if self.basketball.rect.centery < self.rect.centery:
                self.basketball.direction.y *= -1
            else:
                self.basketball.direction.y *= -1
            
            if self.basketball.rect.centerx < self.rect.centerx:
                self.basketball.direction.x *= -1
            else:
                self.basketball.direction.x *= -1
                
    def basket_scored(self):
        pass
            
    def update(self, dt):
        self.old_rect = self.rect.copy()
        
        self.collision_with_ball()
