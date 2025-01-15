from utils import *

class Basketball(pygame.sprite.Sprite):
    def __init__(self, groups, hands_group, players_group):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            pygame.image.load(join("../", "resources", "sprites", "basketball.png")).convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.old_rect = self.rect.copy()
        
        self.vertical_speed = 0
        self.horizontal_speed = 0
        self.direction = pygame.Vector2(0, 1)
        self.gravity = 2
        self.damping = 0.8
        self.horizontal_damping = 1  # Amortizare pentru viteza orizontală
        self.floor = WINDOW_HEIGHT - 70
        self.hands_group = hands_group
        self.players_group = players_group

    def collision_with_hands(self):
        if pygame.sprite.spritecollide(self, self.hands_group, False):
            #self.vertical_speed = -200
            pass

    def collision_with_players(self, direction):
        collided_player = pygame.sprite.spritecollide(self, self.players_group, False)
        if collided_player:
            player = collided_player[0]

            if direction == "horizontal":
                if self.rect.right >= player.rect.left and self.old_rect.right >= player.rect.left:
                    self.rect.right = player.rect.left
                    self.direction.x = -1
                    self.horizontal_speed += 20
                    
                if self.rect.left <= player.rect.right and self.old_rect.left >= player.old_rect.right:
                    self.rect.left = player.rect.right
                    self.direction.x = 1
                    self.horizontal_speed += 20

            if direction == "vertical":
                if self.rect.bottom >= player.rect.top and self.old_rect.bottom <= player.old_rect.top:
                    self.rect.bottom = player.rect.top
                    self.direction.y = -1
                    self.vertical_speed += 20
                if player.rect.bottom >= player.rect.top and self.old_rect.bottom <= player.rect.top:
                    self.rect.top = player.rect.bottom
                    self.direction.y = -1
                    self.vertical_speed += 50
                    print("vatafu")
        
    def falling_under_gravity(self):

        if self.rect.bottom >= self.floor:
            self.rect.bottom = self.floor
            self.direction.y = - self.direction.y
            self.vertical_speed *= self.damping
        if self.rect.top <= 0:
            self.rect.top = 0
            self.direction.y *= -1

        if abs(self.vertical_speed) < 1:
            self.vertical_speed = 0

    def horizontal_movement(self):
        if self.rect.left <= 0:
            self.rect.left = 0
            self.horizontal_speed *= -1
            
        if self.rect.right >= WINDOW_WIDTH:
            self.rect.right = WINDOW_WIDTH
            self.horizontal_speed *= -1
        
        self.horizontal_speed *= self.horizontal_damping

        if abs(self.horizontal_speed) < 1:
            self.horizontal_speed = 0

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.vertical_speed += self.gravity * self.direction.y
        self.rect.centery += self.vertical_speed * self.direction.y * dt
        
        self.collision_with_players("vertical")
        self.falling_under_gravity()
        
        self.rect.centerx += self.horizontal_speed * self.direction.x * dt
        self.collision_with_players("horizontal")
        self.horizontal_movement()

        #collision checking
        self.collision_with_hands()