from utils import *
from basketball import Basketball
from player import Player
from hand import Hand
from hoop import Hoop

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption("Lebron vs Lebron")
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()
        self.hands_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        
        self.players_score = [0 , 0]
        self.font = pygame.font.Font(None, 50)
        
        
        self.background = pygame.transform.scale(pygame.image.load(join("../", "resources", "background", "basketball_court.jpg")).convert_alpha(), (WINDOW_WIDTH, WINDOW_HEIGHT))
        
        #players settings
        player1_controls = {"left" : pygame.K_a, "right" : pygame.K_d , "jump" : pygame.K_w}
        player2_controls = {"left" : pygame.K_LEFT, "right" : pygame.K_RIGHT , "jump" : pygame.K_UP}
        
        player1_hand_controls = { "down" : pygame.K_s }
        player2_hand_controls = { "down" : pygame.K_DOWN}
        
        player1_position = ( 100, 725 )
        player2_position = ( 1000, 725)
        
        player1_padding = 20
        player2_padding = 20
        
        player1_hand_images = [ 
                               pygame.transform.scale(pygame.image.load(join("../", "resources", "animations", "lebron", "lebron_arm[0].png")).convert_alpha(), (25 , 60) ), 
                               pygame.image.load(join("../", "resources", "animations", "lebron", "lebron_arm[1].png")).convert_alpha()
                               ]
        print(player1_hand_images[1])
        player2_hand_images = [ 
                               pygame.transform.scale(pygame.image.load(join("../", "resources", "animations", "curry", "curry_arm[0].png")).convert_alpha(), (30, 60)), 
                               pygame.transform.scale(pygame.image.load(join("../", "resources", "animations", "curry", "curry_arm[1].png")).convert_alpha(), (120, 26))
                               ]
        
        
        player1_image = pygame.transform.scale(pygame.image.load(join("../", "resources", "sprites", "Lebron.png")).convert_alpha(), (70, 120))
        player2_image = pygame.transform.scale(pygame.image.load(join("../", "resources", "sprites", "Curry.png")).convert_alpha(), (70, 120))
        
        self.player1 = Player( (self.all_sprites , self.player_sprites) , player1_image, player1_controls, player1_position, player1_padding)
        self.player2 = Player( ( self.all_sprites, self.player_sprites ), player2_image, player2_controls, player2_position, player2_padding)
            
        player1_offset = [ -5 , 50]    
        player2_offset = [ 45, 43]
        
        self.basketball = Basketball(self.all_sprites,  self.player_sprites)
        
        self.player1_hand = Hand(self.all_sprites , self.player1, player1_hand_images , player1_hand_controls, player1_offset, self.basketball, 1)
        self.player2_hand = Hand(self.all_sprites, self.player2,player2_hand_images , player2_hand_controls, player2_offset, self.basketball, 2)
        
        
        self.hoop1_image = pygame.transform.scale(pygame.image.load(join("../", "resources", "sprites", "left_hoop.png")).convert_alpha(), (150, 225))
        self.hoop2_image = pygame.transform.scale(pygame.image.load(join("../", "resources", "sprites", "right_hoop.png")).convert_alpha(), (150, 225))
        
        self.hoop1_position = ( 80 ,100)
        self.hoop2_position = ( WINDOW_WIDTH - 225 ,100)
        
        self.hoop1 = Hoop(self.all_sprites, self.hoop1_image, self.hoop1_position, self.basketball, self.players_score)
        self.hoop2 = Hoop(self.all_sprites, self.hoop2_image, self.hoop2_position, self.basketball, self.players_score)
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            dt = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.all_sprites.update(dt)
            self.display_surface.blit(self.background, (0,0))
            pygame.sprite.Group.draw(self.all_sprites, self.display_surface)
            pygame.sprite.Group.draw(self.hands_sprites, self.display_surface)
            # pygame.draw.rect(self.display_surface, (255, 0, 0), self.player1.rect, 2)
            # pygame.draw.rect(self.display_surface, "red", self.player2.rect, 2)
            # pygame.draw.rect(self.display_surface, (255, 0, 0), self.basketball.rect, 2)
            # pygame.draw.rect(self.display_surface, "red", self.player1_hand.rect, 2)
            # pygame.draw.rect(self.display_surface, "red", self.player2_hand.rect, 2)
            # pygame.draw.rect(self.display_surface, "red" , self.hoop1.rect,2)
            # pygame.draw.rect(self.display_surface, "red" , self.hoop2.rect,2)
            # pygame.draw.line(self.display_surface, "green" , (120, 220), (230,220), 5)
            # pygame.draw.line(self.display_surface, "green", ( 1060, 220), ( 1175, 220) , 5)
            text = str(self.players_score[0]) + " - " + str(self.players_score[1])
            text_surface = self.font.render(text, True , "black")
            self.display_surface.blit(text_surface, ( 600, 150))
            pygame.display.update()
            
        pygame.quit()