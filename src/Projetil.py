from os import path
from pygame import draw, image

# Classe do projétil
class Projetil():

    def __init__(self, x, y, radius, color, isEspecial1):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 6
        self.isEspecial1 = isEspecial1
        self.projetil_bg = image.load(path.join('../assets', 'projetao.png' if self.isEspecial1 else 'projetil.png'))
        self.dano = 34 if not self.isEspecial1 else 100

    
    # Função para desenhar um projetil
    def draw(self, janela):
        janela.blit(self.projetil_bg, (self.x, self.y))
        #draw.circle(janela, self.color, (self.x, self.y), self.radius)
        self.move()
    
    def move(self):
        self.x += self.vel