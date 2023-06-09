import pygame
from player import Player
from monster import Alien, Monster, Mummy
from comet_event import CometFallEvent
from sounds import SoundManager

#la classe JEU
class Game:

    def __init__(self):
        #Définit si le jeu a commencé ou non
        self.is_playing = False
        #Generer notre joueur lors du début de jeu
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        #effets sonore
        self.sound_manager = SoundManager()
        #Score 0
        self.font = pygame.font.Font("assets/custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}
        #Evenement
        self.comet_event = CometFallEvent(self)
        

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points):
        self.score += points   

    def game_over(self):
        #remettre le jeu à zéro
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        #joue le son game over
        self.sound_manager.play('game_over')
    def update(self, screen):

        #Affichage du score
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))
        

        #appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        #actualise la barre de vie du joueur
        self.player.update_health_bar(screen)

        #récuperer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        #actualise la barre d'évenement du jeu
        self.comet_event.update_bar(screen)

        #actualise l'animation du joueur
        self.player.update_animation()

        #récuperer les monstres du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #récuperer les cometes du jeu 
        for comet in self.comet_event.all_comets:
            comet.fall()

        #appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        #appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        #applique l'ensemble des images de mon groupe de comète
        self.comet_event.all_comets.draw(screen)

        #verifie si le joueur veut aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self .pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

        

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
    
    def spawn_monster(self, monster_class_name):
        
        self.all_monsters.add(monster_class_name.__call__(self))