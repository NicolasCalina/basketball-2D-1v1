from utils import *

class Hoop(pygame.sprite.Sprite):
    def __init__(self, groups, image, position, basketball, players_score):
        super().__init__(groups)
        self.image = image
        self.rect = self.image.get_frect(topleft=position)
        self.old_rect = self.rect.copy()
        self.mask = pygame.mask.from_surface(self.image)
        
        self.basketball = basketball
        
        self.players_score = players_score
    
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
        #print(self.basketball.rect.right, self.basketball.rect.left , self.basketball.rect.bottom)
        if self.basketball.rect.right < 230 and self.basketball.rect.left > 120 and self.basketball.rect.bottom > 220 and self.basketball.rect.top < 220:
            self.basketball.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            self.basketball.speed.x = 0
            self.basketball.speed.y = 0
            self.basketball.direction.x = 0
            self.basketball.direction.y = 1
            self.players_score[0] += 1
            
        if self.basketball.rect.right < 1175 and self.basketball.rect.left > 1060 and self.basketball.rect.bottom > 220 and self.basketball.rect.top < 220:
            self.basketball.rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            self.basketball.speed.x = 0
            self.basketball.speed.y = 0
            self.basketball.direction.x = 0
            self.basketball.direction.y = 1
            self.players_score[1] += 1
            
    def update(self, dt):
        self.old_rect = self.rect.copy()
        
        self.collision_with_ball()
        
        self.basket_scored()#
