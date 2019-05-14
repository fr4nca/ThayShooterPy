from random import randint
from os import path
from pygame import draw, display, image

# Classe do inimigo
class Inimigo():
    
    INIMIGO_BG = image.load(path.join('../assets', 'inimigo.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = -3
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
    
    def draw(self, janela):
        self.move()
        janela.blit(self.INIMIGO_BG, (self.x, self.y))
        #draw.rect(janela, (255, 0, 0), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
        display.update()
    
    def move(self):
        self.x += self.vel

    def hit(self):
        if self.vida > 0:
            self.vida -= 34
