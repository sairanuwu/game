import pygame
import random
import animation

#Classe qui gère l'ennemie dans le jeu

class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.loot_amount = 10
        self.velocity = random.randint(1, 3)
        self.start_animation()

    def set_loot_amount(self, amount):
        self.loot_amount = amount

        
    def damage(self, amount):
        #dégats subis
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health
            #ajout de point au score
            self.game.add_score(self.loot_amount)
            #si la barre d'évenement est chargé au max
            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)

        #méthode pour déclancher la pluie de comètes
        self.game.comet_event.attempt_fall()      

    def update_animation(self):
        self.animate(loop=True)



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

#Classe de la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_loot_amount(20)

#Classe de l'alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.set_loot_amount(80)