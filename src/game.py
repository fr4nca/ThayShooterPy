import pygame
from os import path
from math import floor
from random import randint

from Inimigo import Inimigo
from Projetil import Projetil
from Thay import Thay

# Constantes
WIDTH = 800
HEIGHT = 500
OFFSET = 30
RUN = True

# Globais
PONTUACAO = 0
imunidadeTimer = 0

# Função para desenhos na tela
def drawWindow(janela, ThayNave, projeteis, inimigos):
    global PONTUACAO
    global imunidadeTimer
    global RUN

    fonte = pygame.font.SysFont('comicsans', 24, True)
    fonte2 = pygame.font.SysFont('comicsans', 100, True)

    BG = pygame.image.load(path.join('assets', 'bg.jpg'))
    janela.fill((0,0,0))
    janela.blit(BG, (0, OFFSET))
    pontuacao = fonte.render("Pontuação: " + str(floor(PONTUACAO)), 1, (255, 255, 255))
    janela.blit(pontuacao, (650, 10))
    
    # Desenha a Thay
    ThayNave.draw(janela, fonte)

    if imunidadeTimer > 0:
        imunidadeTimer += 1
    if imunidadeTimer > 150:
        imunidadeTimer = 0
        ThayNave.imune = False
    
    # Desenha inimigos
    if len(inimigos) < 8:
        inimigos.append(Inimigo(randint(WIDTH, WIDTH + 300), randint(OFFSET, HEIGHT - 60), 60, 60))

    for inimigo in inimigos:
        if ThayNave.vida > 0:
            if not ThayNave.imune and imunidadeTimer == 0: 
                if ThayNave.hitbox[1] < inimigo.hitbox[1] + inimigo.hitbox[3] and ThayNave.hitbox[1] + ThayNave.hitbox[3] > inimigo.hitbox[1]:
                        if ThayNave.hitbox[0] + ThayNave.hitbox[2] > inimigo.hitbox[0] and ThayNave.hitbox[0] < inimigo.hitbox[0] + inimigo.hitbox[2]:
                            ThayNave.hit()
                            ThayNave.imune = True
                            imunidadeTimer = 1
        else:
            gameOver = fonte2.render("GAME OVER", 1, (255, 0, 0))
            janela.blit(gameOver, (((WIDTH / 2) - (gameOver.get_width() / 2)), ((HEIGHT / 2) - (gameOver.get_height() / 2))))
            RUN = False

        if inimigo.vida > 0:
            inimigo.draw(janela)
            if inimigo.x < 0 - inimigo.width:
                inimigos.pop(inimigos.index(inimigo))
        else:
            PONTUACAO += 20
            inimigos.pop(inimigos.index(inimigo))

    # Desenha projeteis
    for projetil in projeteis:
        projetil.draw(janela)

        if projetil.x > WIDTH:
            projeteis.pop(projeteis.index(projetil))
            continue

        for inimigo in inimigos:
            if projetil.y - projetil.radius < inimigo.hitbox[1] + inimigo.hitbox[3] and projetil.y + projetil.radius > inimigo.hitbox[1]:
                if projetil.x + projetil.radius > inimigo.hitbox[0] and projetil.x - projetil.radius < inimigo.hitbox[0] + inimigo.hitbox[2]:
                    inimigo.hit()
                    projeteis.pop(projeteis.index(projetil))
            

    pygame.display.update()

# Função de movimentos e teclas
def teclas(ThayNave, projeteis, inimigos):
    global RUN

    keys = pygame.key.get_pressed()

    # Movimentos da Thay
    # Move pra esquerda até a margem
    if keys[pygame.K_LEFT] and ThayNave.x > 1:
        ThayNave.x -= ThayNave.vel
    # Move pra direita até a margem
    if keys[pygame.K_RIGHT] and ThayNave.x < WIDTH - ThayNave.width - 1:
        ThayNave.x += ThayNave.vel
    # Move pra baixo até a margem
    if keys[pygame.K_DOWN] and ThayNave.y < HEIGHT - ThayNave.height - 1:
        ThayNave.y += ThayNave.vel
    # Move pra cima até a margem
    if keys[pygame.K_UP] and ThayNave.y > OFFSET + 1:
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
            
def reset(ThayNave, inimigos):
    ThayNave.x = 10
    ThayNave.y = ((HEIGHT / 2) - (ThayNave.height / 2))
    inimigos.clear()

# Função de início
def run():
    janela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ThayShooter")
    clock = pygame.time.Clock()

    ThayNave = Thay(10, (HEIGHT / 2) - (48 / 2), 64, 48)
    projeteis = []
    inimigos = []
    global PONTUACAO
    global imunidadeTimer

    while RUN:
        clock.tick(60)

        PONTUACAO += 0.1
        teclas(ThayNave, projeteis, inimigos)
        drawWindow(janela, ThayNave, projeteis, inimigos)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    run()
