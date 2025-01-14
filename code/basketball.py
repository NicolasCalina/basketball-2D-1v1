from utils import *

class Basketball(pygame.sprite.Sprite):
    def __init__(self, groups, hands_group, players_group):
        super().__init__(groups)
        self.image = pygame.transform.scale(
            pygame.image.load(join("../", "resources", "sprites", "basketball.png")).convert_alpha(),
            (50, 50)
        )
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.vertical_speed = 0
        self.horizontal_speed = 0
        self.gravity = 2
        self.damping = 0.8
        self.horizontal_damping = 0.9  # Amortizare pentru viteza orizontală
        self.floor = WINDOW_HEIGHT - 70
        self.hands_group = hands_group
        self.players_group = players_group

    def collision_with_hands(self):
        if pygame.sprite.spritecollide(self, self.hands_group, False):
            self.vertical_speed = -200

    def collision_with_players(self):
        if pygame.sprite.spritecollide(self, self.players_group, False):
            self.vertical_speed = -200
            self.horizontal_speed = -self.horizontal_speed * self.damping  # Schimbă direcția și aplică amortizarea

    def falling_under_gravity(self, dt):
        self.vertical_speed += self.gravity
        self.rect.centery += self.vertical_speed * dt

        if self.rect.bottom >= self.floor:
            self.rect.bottom = self.floor
            self.vertical_speed = -self.vertical_speed * self.damping

            if abs(self.vertical_speed) < 10:
                self.vertical_speed = 0

    def horizontal_movement(self, dt):
        self.rect.centerx += self.horizontal_speed * dt

        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.horizontal_speed = -self.horizontal_speed * self.damping

        self.horizontal_speed *= self.horizontal_damping

        if abs(self.horizontal_speed) < 1:
            self.horizontal_speed = 0

    def update(self, dt):
        #movement logic
        self.falling_under_gravity(dt)
        self.horizontal_movement(dt)

        #collision checking
        self.collision_with_hands()
        self.collision_with_players()

        
        
            