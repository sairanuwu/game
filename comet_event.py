import pygame
from comet import Comet
#Classe qui gère l'évenement 
class CometFallEvent:
    
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.all_comets = pygame.sprite.Group() 
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100
    
    def reset_percent(self):
        self.percent = 0
    #nombre de météore qui tombe 
    def meteor_fall(self):
        for i in range(2, 15):
            self.all_comets.add(Comet(self))

       
    def attempt_fall(self):
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True
            
    
    
    def update_bar(self, surface):

        #pourcentage de la barre
        self.add_percent()

       
    #Barre d'évenement NOIR
        pygame.draw.rect(surface, (0, 0, 0), [
            0, #axe des X
            surface.get_height() - 20,#axe des y
            surface.get_width(),#longueur de la fênetre
            10 #épaisseur de la barre
        ])
    #Barre d'évenement ROUGE
        pygame.draw.rect(surface, (187, 11, 11), [
            0, #axe des X
            surface.get_height() - 20,#axe des y
            (surface.get_width() / 100) * self.percent,#longueur de la fênetre
            10 #épaisseur de la barre
        ])