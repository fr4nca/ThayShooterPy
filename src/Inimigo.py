from random import randint
from pygame import draw

# Classe do inimigo
class Inimigo():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = randint(-3, -1)
    
    def draw(self, janela):
        draw.rect(janela, (255, 255, 255), (self.x, self.y, self.width, self.height))
        self.move()
    
    def move(self):
        self.x += self.vel