import pygame
from game import Game
from player import Player
pygame.init()

#Fênetre du jeu
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080, 720))

#Chargement de l'arrièrep plan
background = pygame.image.load('assets/bg.jpg')

#Chargement du joueur
player = Player()

#Chargement du jeu
game = Game()

running = True

#Boucle tant que la condition est vraie
while running:

    #appliquer la fênetre du jeu
    screen.blit(background, (0,-200))

    #appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)

    #récuperer les projectiles du joueur
    for projectile in game.player.all_projectiles:
        projectile.move()

    #appliquer l'ensemble des images de mon groupe de projectiles
    game.player.all_projectiles.draw(screen)

    #verifie si le joueur veut aller à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game .pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()

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