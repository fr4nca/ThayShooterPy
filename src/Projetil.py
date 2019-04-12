from pygame import draw

# Classe do projétil
class Projetil():
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.vel = 6
    
    # Função para desenhar um projetil
    def draw(self, janela):
        draw.circle(janela, self.color, (self.x, self.y), self.radius)
        self.move()
    
    def move(self):
        self.x += self.vel