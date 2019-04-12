import pygame
from os import path
from random import randint

from Inimigo import Inimigo
from Projetil import Projetil
from Thay import Thay

# Constantes
WIDTH = 800
HEIGHT = 500
RUN = True

# Função para desenhos na tela
def drawWindow(janela, ThayNave, projeteis, inimigos):
    BG = pygame.image.load(path.join('assets', 'bg.jpg'))

    janela.blit(BG, (0, 0))
    
    # Desenha a Thay
    ThayNave.draw(janela)
    
    # Desenha inimigos
    if len(inimigos) < 8:
        inimigos.append(Inimigo(randint(WIDTH, WIDTH + 300), randint(0, HEIGHT - 60), 60, 60))

    for inimigo in inimigos:
        inimigo.draw(janela)
        if inimigo.x < 0 - inimigo.width:
            inimigos.pop(inimigos.index(inimigo))

    # Desenha projeteis
    for projetil in projeteis:
        projetil.draw(janela)
        if projetil.x > WIDTH:
            projeteis.pop(projeteis.index(projetil))

    pygame.display.update()

# Função de movimentos e teclas
def teclas(ThayNave, projeteis, inimigos):
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

    # Atira o projétil
    if keys[pygame.K_x]:
        if len(projeteis) < 18:
            if len(projeteis) > 0 and projeteis[len(projeteis) - 1].x > ThayNave.x + 70:
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))
            elif len(projeteis) == 0: 
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0)))

    if keys[pygame.K_ESCAPE]:
        RUN = False
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

# Função de início
def run():
    janela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ThayShooter")
    clock = pygame.time.Clock()

    ThayNave = Thay(40, 40, 64, 48)
    projeteis = []
    inimigos = []


    while RUN:
        clock.tick(60)
        
        teclas(ThayNave, projeteis, inimigos)
        drawWindow(janela, ThayNave, projeteis, inimigos)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    run()
