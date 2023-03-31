import pygame
import random

#Classe qui gère l'ennemie dans le jeu

class Monster(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        #dégats subis
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    def update_health_bar(self, surface):
        #dessin de l'arrière plan de la barre de vie
        pygame.draw.rect(surface, (61, 61, 61), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        
        #dessin de la barre de vie
        pygame.draw.rect(surface, (55, 201, 0), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        

    def forward(self):
        #déplacement ne se fait si il n'y a pas de collision avec un group de player
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        #si le montre est en collision avec le joueur
        else:
            self.game.player.damage(self.attack)