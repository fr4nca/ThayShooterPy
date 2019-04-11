import pygame

# Constantes
CLOCK = pygame.time.Clock()
BG = pygame.image.load('bg.jpg')
THAY_BG = pygame.image.load('thay1.png')
WIDTH = 800
HEIGHT = 500
RUN = True

# Classe da jogador
class Thay():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 3

    # Função para desenhar o jogador
    def draw(self, janela):
        janela.blit(THAY_BG, (self.x, self.y))
        
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

# Função para desenhos na tela
def drawWindow(janela, ThayNave, projeteis):
    janela.blit(BG, (0, 0))
    ThayNave.draw(janela)
    for projetil in projeteis:
        projetil.draw(janela)
    pygame.display.update()

# Função de movimentos e teclas
def movimentos(ThayNave, projeteis):
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
    for projetil in projeteis:
        if projetil.x < WIDTH:
            projetil.x += projetil.vel
        else:
            projeteis.pop(projeteis.index(projetil))
    # Atira o projétil
    if keys[pygame.K_x]:
        if len(projeteis) < 50:
            if len(projeteis) > 0 and projeteis[len(projeteis) - 1].x > ThayNave.x + 60:
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))
            elif len(projeteis) == 0: 
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))

    if keys[pygame.K_ESCAPE]:
        RUN = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

# Função de início
def run(ThayNave, projeteis):
    global RUN

    janela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ThayShooter")

    while RUN:
        CLOCK.tick(60)

        movimentos(ThayNave, projeteis)
        drawWindow(janela, ThayNave, projeteis)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    ThayNave = Thay(40, 40, 64, 48)
    projeteis = []
    run(ThayNave, projeteis)
