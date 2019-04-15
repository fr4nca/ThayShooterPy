from os import path
from pygame import image, draw, font, display

# Classe da jogador
class Thay():
    THAY_BG = image.load(path.join('assets', 'thay1.png'))

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
        self.imune = False


    # Função para desenhar o jogador
    def draw(self, janela, fonte):
        janela.blit(self.THAY_BG, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        vida = fonte.render("HP: ", 1, (255, 255, 255))
        janela.blit(vida, (5, 10))
        draw.rect(janela, (255, 0, 0), (45, 5, 200, 21))
        draw.rect(janela, (0, 255, 0), (45, 5, 200 - ((200/100) * (100 - self.vida)), 21))
        display.update()

    def hit(self):
        self.vida -= 20
        