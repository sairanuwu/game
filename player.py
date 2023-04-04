import pygame
from projectile import Projectile
import animation

#la classe JOUEUR

class Player(animation.AnimateSprite): 

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
       


    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le joueur n'a plus de pdv
            self.game.game_over()
    def update_animation(self):
        self.animate()
    
    
    def update_health_bar(self, surface):
        #dessin de l'arrière plan de la barre de vie
        pygame.draw.rect(surface, (61, 61, 61), [self.rect.x + 50, self.rect.y +20, self.max_health, 5])
        
        #dessin de la barre de vie
        pygame.draw.rect(surface, (55, 201, 0), [self.rect.x + 50, self.rect.y +20, self.health, 5])
        

        
    def launch_projectile(self):
        #instance de la class projectile
        self.all_projectiles.add(Projectile(self))
        #démarre l'animation du lancer
        self.start_animation()
        #joue le son du projectile
        self.game.sound_manager.play('tir')
    def move_right(self):
        #déplacement se fait uniquement si il n'y a pas de collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity