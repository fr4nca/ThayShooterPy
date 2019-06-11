from random import randint
from os import path
from pygame import draw, display, image
import random

# Classe do inimigo
class Inimigo():


    def __init__(self, x, y, width, height, isEspecial1, icon):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = -3
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
        self.isEspecial1 = isEspecial1
        self.icon = icon 
        imagens = [ 'inimigos3.png', 'inimigos.png', 'inimigos2.png', 'inimigos4.png' ]
        self.INIMIGO_BG = image.load(path.join('../assets', imagens[icon]))
    
    def draw(self, janela):
        self.move()
        janela.blit(self.INIMIGO_BG, (self.x, self.y))
        #draw.rect(janela, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
        display.update()
    
    def move(self):
        self.x += self.vel

    def hit(self, dano):
        if self.vida > 0:
            self.vida -= dano
