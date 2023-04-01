import pygame
import math
from game import Game
from player import Player


pygame.init()

clock = pygame.time.Clock()

#Fênetre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#Chargement de l'arrièrep plan
background = pygame.image.load('assets/bg.jpg')

#Chargement bannière du jeu
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
#banner_rect.y = math.ceil(screen.get_height() / 5)

#Chargement bouton Play
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

#Chargement du joueur
player = Player(Game)

#Chargement du jeu
game = Game()

running = True

clock = pygame.time.Clock()
#Boucle tant que la condition est vraie
while running:

    #appliquer la fênetre du jeu
    screen.blit(background, (0,-200))

    #vérifie si le jeu à commencé ou non
    if game.is_playing:
        #déclanche les instructions de la partie
        game.update(screen)
    #vérifie si le jeu n'a pas commencé
    else:
        #écran d'acceuil
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)
        

    #mettre à jour l'écran
    pygame.display.flip()

     # Mettre à jour l'écran
    pygame.display.flip()

    # Contrôler le nombre de FPS
    clock.tick(60)

    #si le joueur ferme la fênetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
            #Fênetre fermer

        #Detecte si un joueur lâche une toûche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclancher pour lancer notre projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifie si la souris clique sur le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.start()