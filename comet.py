import pygame
import random

#Classe qui gère la comète

class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #l'image de la comète
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(2, 4)
        self.rect.x = random.randint(20, 800)
        self.rect.y = -random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        #joue le son de la comète
        self.comet_event.game.sound_manager.play('meteorite')

        #verifie si la comete est terminé
        if len(self.comet_event.all_comets) == 0:
            print("évenement terminé")
            self.comet_event.reset_percent()
            self.comet_event.game.start()
    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            print("sol")
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                print("évenement terminé")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")
            self.remove()
            #subis des dmg
            self.comet_event.game.player.damage(20)
        
            