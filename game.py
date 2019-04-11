import pygame
import random

# Constantes
CLOCK = pygame.time.Clock()
WIDTH = 800
HEIGHT = 500
RUN = True

# Classe da jogador
class Thay():
    THAY_BG = pygame.image.load('thay1.png')

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3

    # Função para desenhar o jogador
    def draw(self, janela):
        janela.blit(self.THAY_BG, (self.x, self.y))

# Classe do inimigo
class Inimigo():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = random.randint(-3, -1)
    
    def draw(self, janela):
        pygame.draw.rect(janela, (255, 255, 255), (self.x, self.y, self.width, self.height))
        self.move()
    
    def move(self):
        self.x += self.vel
    
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
        pygame.draw.circle(janela, self.color, (self.x, self.y), self.radius)
        self.move()
    
    def move(self):
        self.x += self.vel

# Função para desenhos na tela
def drawWindow(janela, ThayNave, projeteis, inimigos):
    BG = pygame.image.load('bg.jpg')

    janela.blit(BG, (0, 0))
    ThayNave.draw(janela)
    # inimigo.draw(janela)
    for inimigo in inimigos:
        inimigo.draw(janela)
        if inimigo.x < 0 - inimigo.width:
            inimigos.pop(inimigos.index(inimigo))

    for projetil in projeteis:
        projetil.draw(janela)
        if projetil.x > WIDTH:
            projeteis.pop(projeteis.index(projetil))
    pygame.display.update()

# Função de movimentos e teclas
def movimentos(ThayNave, projeteis, inimigos):
    global RUN

    keys = pygame.key.get_pressed()
# Movimentos da Thay
    # Move pra esquerda até a margem
    if keys[pygame.K_LEFT] and ThayNave.x > 0:
        ThayNave.x -= ThayNave.vel
    # Move pra direita até a margem
    if keys[pygame.K_RIGHT] and ThayNave.x < WIDTH - ThayNave.width:
        ThayNave.x += ThayNave.vel
    # Move pra baixo até a margem
    if keys[pygame.K_DOWN] and ThayNave.y < HEIGHT - ThayNave.height:
        ThayNave.y += ThayNave.vel
    # Move pra cima até a margem
    if keys[pygame.K_UP] and ThayNave.y > 0:
        ThayNave.y -= ThayNave.vel

# Movimentos do projétil
    # Atira o projétil
    if keys[pygame.K_x]:
        if len(projeteis) < 50:
            if len(projeteis) > 0 and projeteis[len(projeteis) - 1].x > ThayNave.x + 50:
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))
            elif len(projeteis) == 0: 
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))

# Movimento do inimigo
    if len(inimigos) < 8:
        inimigos.append(Inimigo(random.randint(WIDTH, WIDTH + 300), random.randint(0, HEIGHT - 60), 60, 60))

    if keys[pygame.K_ESCAPE]:
        RUN = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

# Função de início
def run(ThayNave, projeteis, inimigos):
    janela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ThayShooter")

    while RUN:
        CLOCK.tick(60)

        movimentos(ThayNave, projeteis, inimigos)
        drawWindow(janela, ThayNave, projeteis, inimigos)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    ThayNave = Thay(40, 40, 64, 48)
    projeteis = []
    inimigos = []
    run(ThayNave, projeteis, inimigos)
