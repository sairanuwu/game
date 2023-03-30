import pygame
from player import Player

#la classe JEU
class Game:

    def __init__(self):
        #Generer notre joueur lors du début de jeu
        self.player = Player()
        self.pressed = {}