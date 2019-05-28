from os import path
from pygame import draw, image

# Classe do projétil
class Projetil():

    PROJETIL_BG = image.load(path.join('../assets', 'projetil.png'))

    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 6
    
    # Função para desenhar um projetil
    def draw(self, janela):
        janela.blit(self.PROJETIL_BG, (self.x, self.y))
        #draw.circle(janela, self.color, (self.x, self.y), self.radius)
        self.move()
    
    def move(self):
        self.x += self.vel