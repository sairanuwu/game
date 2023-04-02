import pygame

#Class projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #Constructeur de la class
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        #emplacement du projectile
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        #rotation du projectile
        self.origine_image = self.image
        self.angle = 2
    
    def rotate(self):
        #fait tourner le projectile
        self.angle += 6
        self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
    def remove(self):
        self.player.all_projectiles.remove(self)
    
    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        
        #verifie si le projectile entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)
        #vérifie si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1080:
            #supprime le projectile hors d'écran
            self.remove()
         