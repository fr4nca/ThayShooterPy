from random import randint
from pygame import draw, display

# Classe do inimigo
class Inimigo():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = -2 
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
    
    def draw(self, janela):
        self.move()
        draw.rect(janela, (255, 255, 255), (self.x, self.y, self.width, self.height))
        self.hitbox = (self.x, self.y, self.width, self.height)
        display.update()
    
    def move(self):
        self.x += self.vel

    def hit(self):
        if self.vida > 0:
            self.vida -= 34
