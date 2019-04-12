from os import path
from pygame import image

# Classe da jogador
class Thay():
    THAY_BG = image.load(path.join('assets', 'thay1.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3

    # Função para desenhar o jogador
    def draw(self, janela):
        janela.blit(self.THAY_BG, (self.x, self.y))