from random import randint
from os import path
from pygame import draw, display, image

# Classe do inimigo
class EspecialAmigo():
    
    ESPECIAL_AMIGO_BG = image.load(path.join('../assets', 'inimigos.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, janela):
        self.move()
        janela.blit(self.ESPECIAL_AMIGO_BG, (self.x, self.y))
        display.update()

    def solta_especial(self, janela):
      # soltar especial dependendo do aliado

