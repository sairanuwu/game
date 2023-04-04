import pygame

#classe qui gère l'animation des entités
class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 #commence l'image à 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #méthode pour le démarrage de l'animation
    def start_animation(self):
        self.animation = True
    
    #Méthode pour animer le sprite
    def animate(self, loop=False):
        #vérifie si l'animation est active
        if self.animation:

            #passe a l'image suivante
            self.current_image += 1 
            #vérifie si la dernière image est atteinte
            if self.current_image >= len(self.images):
                #remet l'animation à 0
                self.current_image = 0
                #vérifie si l'animation n'est pas en mode boucle
                if loop is False:
                    
                    #désactivation de l'animation
                    self.animation = False
            #modifie l'image précedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


#Fonction qui charge les images d'un sprite
def load_animation_images(sprite_name):
    images = []
    path = f"assets/{sprite_name}/{sprite_name}"
    #boucle sur chaque image
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu de la liste d'images
    return images

#Définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien': load_animation_images('alien')
}