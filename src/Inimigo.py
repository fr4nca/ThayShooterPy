from random import randint
from os import path
from pygame import draw, display, image
import random

# Classe do inimigo
class Inimigo():
    def __init__(self, x, y, width, height, isEspecialInimigo3):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isEspecialInimigo3 = isEspecialInimigo3
        self.vel = -2 if not isEspecialInimigo3 else randint(-5, -2)
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
        imagens = [ 'inimigos3.png', 'inimigos.png', 'inimigos2.png', 'inimigos4.png' ]
        self.INIMIGO_BG = image.load(path.join('../assets', imagens[randint(0,3)]))
    
    def draw(self, janela):
        self.move()
        janela.blit(self.INIMIGO_BG, (self.x, self.y))
        #draw.rect(janela, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
    
    def move(self):
        self.x += self.vel

    def hit(self, dano):
        if self.vida > 0:
            self.vida -= dano
