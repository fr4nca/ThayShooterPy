
import pygame
from pygame import image
from os import path
from math import floor
from random import randint

from Inimigo import Inimigo
from Projetil import Projetil
from Thay import Thay
from Menu import Menu

# Constantes
WIDTH = 780
HEIGHT = 510
OFFSET = 50
RUN = True
icon = image.load(path.join('../assets', 'inimigos.png'))


# Globais
pontuacao = 0
imunidadeTimer = 0
tiroTimer = 0
recorde = 0

isEspecial1 = False
especial1Timer = 0
especial1Enabled = False
especial1Pontuacao = 0
rodolfo = image.load(path.join('../assets', 'rodolfo_inativo.png'))

isEspecial2 = False
especial2Timer = 0
especial2Enabled = False
especial2Pontuacao = 0
barbosa = image.load(path.join('../assets', 'barbosa_inativo.png'))

isEspecial3 = False
especial3Timer = 0
especial3Enabled = False
especial3Pontuacao = 0
chiquinho = image.load(path.join('../assets', 'chiquinho_inativo.png'))

def novo_recorde():
    global pontuacao
    global recorde
    
    if pontuacao > recorde :
        return True
    return False

# Função para desenhos na tela
def drawWindow(janela, ThayNave, projeteis, inimigos):

    global pontuacao
    global imunidadeTimer
    global RUN
    global recorde
    
    global isEspecial1
    global especial1Enabled
    global especial1Pontuacao
    global rodolfo

    global especial2Enabled
    global especial2Pontuacao
    global barbosa

    global especial3Enabled
    global especial3Pontuacao
    global chiquinho

    fonte = pygame.font.SysFont('comicsans', 24, True)
    fonte2 = pygame.font.SysFont('comicsans', 100, True)

    BG = pygame.image.load(path.join('../assets', 'bg3.jpg'))
    janela.fill((0,0,0))
    janela.blit(BG, (0, OFFSET))
    pontos = fonte.render("Pontuação: " + str(floor(pontuacao)), 1, (255, 255, 255))
    janela.blit(pontos, (630, 10))
    janela.blit(rodolfo, (280,4))
    janela.blit(barbosa, (330, 4))
    janela.blit(chiquinho, (380, 4))
    
    # Desenha a Thay
    ThayNave.draw(janela, fonte)

    if imunidadeTimer > 0:
        imunidadeTimer += 1
    if imunidadeTimer > 150:
        imunidadeTimer = 0
        ThayNave.imune = False
    
    # Desenha inimigos
    if len(inimigos) < 8:
        inimigos.append(Inimigo((randint(14, 20) * 60), (randint(0, 6) * 60) + OFFSET, 60, 60, isEspecial1))

    # Colisão dos inimigos com a Thay
    for inimigo in inimigos:
        if ThayNave.vida > 0:
            if not ThayNave.imune and imunidadeTimer == 0: 
                if ThayNave.hitbox[1] < inimigo.hitbox[1] + inimigo.hitbox[3] and ThayNave.hitbox[1] + ThayNave.hitbox[3] > inimigo.hitbox[1]:
                        if ThayNave.hitbox[0] + ThayNave.hitbox[2] > inimigo.hitbox[0] and ThayNave.hitbox[0] < inimigo.hitbox[0] + inimigo.hitbox[2]:
                            ThayNave.hit()
                            ThayNave.imune = True
                            imunidadeTimer = 1
        else:
            if novo_recorde(): 
                recorde = pontuacao
                Menu.game_over(pontuacao, recorde, True)
            else:
                Menu.game_over(pontuacao, recorde, False)
            pontuacao = 0
            run()

        if inimigo.vida > 0:
            inimigo.draw(janela)
            if inimigo.x < 0 - inimigo.width:
                inimigos.pop(inimigos.index(inimigo))
        else:
            pontuacao += 20
            inimigos.pop(inimigos.index(inimigo))

        if inimigo.x == 0 and not isEspecial3:
            ThayNave.vida -= 5

    # Desenha projeteis
    for projetil in projeteis:
        projetil.draw(janela)

        if projetil.x > WIDTH:
            projeteis.pop(projeteis.index(projetil))
            continue

        # Colisão do projetil com inimigo
        for inimigo in inimigos:
            if projetil.y - projetil.radius < inimigo.hitbox[1] + inimigo.hitbox[3] and projetil.y + projetil.radius > inimigo.hitbox[1]:
                if projetil.x + projetil.radius > inimigo.hitbox[0] and projetil.x - projetil.radius < inimigo.hitbox[0] + inimigo.hitbox[2]:
                    inimigo.hit(projetil.dano)
                    if projetil in projeteis:
                        projeteis.pop(projeteis.index(projetil))
                    continue


    if especial1Pontuacao > 1000: 
        especial1Enabled = True
        
    if especial1Enabled:
        rodolfo = pygame.image.load(path.join('../assets', 'rodolfo_ativo.png'))
    else: 
        rodolfo = pygame.image.load(path.join('../assets', 'rodolfo_inativo.png'))

    especial1Pontuacao += 1


    if especial2Pontuacao > 2000: 
        especial2Enabled = True
        rodolfo
    if especial2Enabled:
        barbosa = pygame.image.load(path.join('../assets', 'barbosa_ativo.png'))
    else: 
        barbosa = pygame.image.load(path.join('../assets', 'barbosa_inativo.png'))

    especial2Pontuacao += 1


    if especial3Pontuacao > 3000: 
        especial3Enabled = True
        
    if especial3Enabled:
        chiquinho = pygame.image.load(path.join('../assets', 'chiquinho_ativo.png'))
    else: 
        chiquinho = pygame.image.load(path.join('../assets', 'chiquinho_inativo.png'))

    especial3Pontuacao += 1

    pygame.display.update()

# Função de movimentos e teclas
def teclas(ThayNave, projeteis, inimigos):
    global RUN
    global tiroTimer
    global pontuacao

    global isEspecial1
    global especial1Timer
    global especial1Enabled
    global especial1Pontuacao
    global rodolfo

    global isEspecial2
    global especial2Timer
    global especial2Enabled
    global especial2Pontuacao
    # global rodolfo

    global isEspecial3
    global especial3Timer
    global especial3Enabled
    global especial3Pontuacao
    # global rodolfo


    keys = pygame.key.get_pressed()

    # Movimentos da Thay
    # Move pra esquerda até a margem
    # if keys[pygame.K_LEFT] and ThayNave.x > 1:
    #     ThayNave.x -= ThayNave.vel
    # # Move pra direita até a margem
    # if keys[pygame.K_RIGHT] and ThayNave.x < WIDTH - ThayNave.width - 1:
    #     ThayNave.x += ThayNave.vel
    # Move pra baixo até a margem
    if keys[pygame.K_DOWN] and ThayNave.y < HEIGHT - ThayNave.height - 1:
        ThayNave.y += ThayNave.vel
    # Move pra cima até a margem
    if keys[pygame.K_UP] and ThayNave.y > OFFSET + 1:
        ThayNave.y -= ThayNave.vel

    # Atira o projétil
    if tiroTimer > 0:
        tiroTimer += 1
    if tiroTimer > 4:
        tiroTimer = 0

    if keys[pygame.K_x] and tiroTimer == 0:
        if len(projeteis) < 18:
            if len(projeteis) > 0:
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0), isEspecial1))
            elif len(projeteis) == 0: 
                projeteis.append(Projetil(round(ThayNave.x + ThayNave.width // 2), round(ThayNave.y + ThayNave.height // 2), 3, (255, 0, 0), isEspecial1))
            tiroTimer = 1

    if especial1Timer > 0:
        especial1Timer += 1
    if especial1Timer > 250:
        especial1Timer = 0
        isEspecial1 = False
        especial1Enabled = False
        especial1Pontuacao = 0

    if especial2Timer > 0:
        especial2Timer += 1
    if especial2Timer > 250:
        especial2Timer = 0
        isEspecial2 = False
        especial2Enabled = False
        especial2Pontuacao = 0
        ThayNave.especial2(isEspecial2)

    if especial3Timer > 0:
        especial3Timer += 1
    if especial3Timer > 250:
        especial3Timer = 0
        isEspecial3 = False
        especial3Enabled = False
        especial3Pontuacao = 0
        ThayNave.especial3(isEspecial3)

    if keys[pygame.K_a] and especial1Enabled:
        isEspecial1 = True
        especial1Timer = 1

    if keys[pygame.K_s] and especial2Enabled:
        isEspecial2 = True  
        ThayNave.especial2(isEspecial2)
        especial2Timer = 1

    if keys[pygame.K_d] and especial3Enabled:
        isEspecial3 = True
        ThayNave.especial3(isEspecial3)
        especial3Timer = 1

    if keys[pygame.K_ESCAPE]:
        Menu.resume(ThayNave.vida, pontuacao)
        RUN=True
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUN = False

# Função de início
def run():
    global isEspecial2
    global isEspecial3
    global pontuacao
    global recorde

    janela = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ThayShooter")
    
    clock = pygame.time.Clock()

    ThayNave = Thay(10, (HEIGHT / 2) - (48 / 2), 64, 48, isEspecial2, isEspecial3)
    projeteis = []
    inimigos = []

    while RUN:
        clock.tick(60)

        pontuacao += 0.1
        teclas(ThayNave, projeteis, inimigos)
        
        drawWindow(janela, ThayNave, projeteis, inimigos)

    pygame.quit()

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_icon(icon)
    Menu.menu_inicial()
    run()