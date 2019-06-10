from os import path
from pygame import image, draw, font, display

# Classe da jogador
class Thay():
    THAY_BG = image.load(path.join('../assets', 'ThayShooter2.png'))

    def __init__(self, x, y, width, height, isEspecial2, isEspecial3):
        self.isEspecial2 = isEspecial2
        self.isEspecial3 = isEspecial3
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5 if not self.isEspecial2 else 10
        self.hitbox = (self.x, self.y, self.width, self.height)
        self.vida = 100
        self.imune = False if not self.isEspecial3 else True


    # Função para desenhar o jogador
    def draw(self, janela, fonte):
        janela.blit(self.THAY_BG, (self.x, self.y))
        self.hitbox = (self.x, self.y, self.width, self.height)
        vida = fonte.render("HP: ", 1, (255, 255, 255))
        janela.blit(vida, (5, 17))
        draw.rect(janela, (255, 0, 0), (45, 15, 200, 21))
        draw.rect(janela, (0, 255, 0), (45, 15, 200 - ((200/100) * (100 - self.vida)), 21))
        display.update()

    def hit(self):
        self.vida -= 20
    
    def especial2(self, isEspecial):
        self.isEspecial2 = isEspecial
        self.vel = 5 if not self.isEspecial2 else 10

    def especial3(self, isEspecial):
        self.isEspecial3 = isEspecial
        self.imune = False if not self.isEspecial3 else True