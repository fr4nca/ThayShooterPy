
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
bgs = [pygame.image.load(path.join('../assets', 'bg3.jpg')), pygame.image.load(path.join('../assets', 'bg.jpg'))]
BG = bgs[0]
# THAY TROCAR PRA IMAGEM CERTA
preto = image.load(path.join('../assets', 'preto.png'))

# Globais
pontuacao = 0
imunidadeTimer = 0
tiroTimer = 0
recorde = 0

# Rodolfo - Tiros mais fortes
isEspecial1 = False
especial1Timer = 0
especial1Enabled = False
especial1Pontuacao = 0
rodolfoImgs = [image.load(path.join('../assets', 'rodolfo_ativo.png')), image.load(path.join('../assets', 'rodolfo_inativo.png'))]
rodolfo = rodolfoImgs[1]

# Barbosa - movimentação mais rápida
isEspecial2 = False
especial2Timer = 0
especial2Enabled = False
especial2Pontuacao = 0
barbosaImgs = [image.load(path.join('../assets', 'barbosa_ativo.png')), image.load(path.join('../assets', 'barbosa_inativo.png'))]
barbosa = barbosaImgs[1]

# Chiquinho - imunidade
isEspecial3 = False
especial3Timer = 0
especial3Enabled = False
especial3Pontuacao = 0
chiquinhoImgs = [image.load(path.join('../assets', 'chiquinho_ativo.png')), image.load(path.join('../assets', 'chiquinho_inativo.png'))]
chiquinho = chiquinhoImgs[1]


inimigosImgs = [image.load(path.join('../assets', 'vazio.png')), image.load(path.join('../assets', 'rubia.png')), image.load(path.join('../assets', 'oswaldo.png'))]
especialinimigo = inimigosImgs[0]

# Rubia - troca os controles
isEspecialInimigo1 = False
especialInimigo1Timer = 0
especialInimigo1Enable = False
especialInimigo1Pontuacao = 0


# Oswaldo - diminui visão do mapa
isEspecialInimigo2 = False
especialInimigo2Timer = 0
especialInimigo2Enable = False
especialInimigo2Pontuacao = 0

# Osmar - ainda não sei kkk
isEspecialInimigo3 = False
especialInimigo3Enable = False
especialInimigo3Timer = 0
especialInimigo3Pontuacao = 0

def reset():
    global isEspecial1
    global isEspecial2
    global isEspecial3

    global especial1Enabled
    global especial2Enabled
    global especial3Enabled

    global especial1Timer
    global especial2Timer
    global especial3Timer

    global especial1Pontuacao
    global especial2Pontuacao
    global especial3Pontuacao

    global rodolfo
    global barbosa
    global chiquinho

    global isEspecialInimigo1
    global especialInimigo1Timer
    global especialInimigo1Enable 
    global especialInimigo1Pontuacao

    global isEspecialInimigo2
    global especialInimigo2Timer
    global especialInimigo2Enable 
    global especialInimigo2Pontuacao

    global isEspecialInimigo3
    global especialInimigo3Timer
    global especialInimigo3Enable 
    global especialInimigo3Pontuacao

    # Rodolfo - Tiros mais fortes
    isEspecial1 = False
    especial1Timer = 0
    especial1Enabled = False
    especial1Pontuacao = 0
    rodolfo = rodolfoImgs[1]

    # Barbosa - movimentação mais rápida
    isEspecial2 = False
    especial2Timer = 0
    especial2Enabled = False
    especial2Pontuacao = 0
    barbosa = barbosaImgs[1]

    # Chiquinho - imunidade
    isEspecial3 = False
    especial3Timer = 0
    especial3Enabled = False
    especial3Pontuacao = 0
    chiquinho = chiquinhoImgs[1]

    # Rubia - troca os controles
    isEspecialInimigo1 = False
    especialInimigo1Timer = 0
    especialInimigo1Enable = False
    especialInimigo1Pontuacao = 0

    # Oswaldo - diminui visão do mapa
    isEspecialInimigo2 = False
    especialInimigo2Timer = 0
    especialInimigo2Enable = False
    especialInimigo2Pontuacao = 0

    # Osmar - ainda não sei kkk
    isEspecialInimigo3 = False
    especialInimigo3Enable = False
    especialInimigo3Timer = 0
    especialInimigo3Pontuacao = 0

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
    global bgs
    global BG
    
    global isEspecial1
    global especial1Enabled
    global especial1Pontuacao
    global rodolfo
    global rodolfoImgs

    global especial2Enabled
    global especial2Pontuacao
    global barbosa
    global barbosaImgs

    global especial3Enabled
    global especial3Pontuacao
    global chiquinho
    global chiquinhoImgs

    global especialinimigo

    global isEspecialInimigo1
    global especialInimigo1Pontuacao
    global especialInimigo1Enable
    
    global isEspecialInimigo2
    global especialInimigo2Pontuacao
    global especialInimigo2Enable
    global especialInimigo2Timer

    global isEspecialInimigo3
    global especialInimigo3Pontuacao
    global especialInimigo3Enable
    global especialInimigo3Timer

    fonte = pygame.font.SysFont('comicsans', 24, True)
    fonte2 = pygame.font.SysFont('comicsans', 100, True)

    janela.fill((0,0,0))
    janela.blit(BG, (0, OFFSET)) 
    pontos = fonte.render("Pontuação: " + str(floor(pontuacao)), 1, (255, 255, 255))
    janela.blit(pontos, (630, 10))
    janela.blit(rodolfo, (280,4))
    janela.blit(barbosa, (330, 4))
    janela.blit(chiquinho, (380, 4))
    janela.blit(especialinimigo, (520, 4))
    
    # Desenha a Thay
    ThayNave.draw(janela, fonte)

    if imunidadeTimer > 0:
        imunidadeTimer += 1
    if imunidadeTimer > 150:
        imunidadeTimer = 0
        ThayNave.imune = False
    
    # Desenha inimigos
    if len(inimigos) < 8:
        inimigos.append(Inimigo((randint(14, 20) * 60), (randint(0, 6) * 60) + OFFSET, 60, 60, isEspecialInimigo3))

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
            reset()
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

    # Especiais amigos
    if especial1Pontuacao > 1000: 
        especial1Enabled = True
        
    if especial1Enabled:
        rodolfo = rodolfoImgs[0]
    else: 
        rodolfo = rodolfoImgs[1]

    especial1Pontuacao += 1


    if especial2Pontuacao > 1500: 
        especial2Enabled = True

    if especial2Enabled:
        barbosa = barbosaImgs[0]
    else: 
        barbosa = barbosaImgs[1]

    especial2Pontuacao += 1


    if especial3Pontuacao > 2000: 
        especial3Enabled = True
        
    if especial3Enabled:
        chiquinho = chiquinhoImgs[0]
    else: 
        chiquinho = chiquinhoImgs[1]

    especial3Pontuacao += 1

    # Especiais inimigos
    # Rubia
    if especialInimigo1Pontuacao > 650:
        isEspecialInimigo1 = True
        especialinimigo = inimigosImgs[1]
        especialInimigo1Enable = True

    especialInimigo1Pontuacao += 1

    # Oswaldo
    if especialInimigo2Pontuacao > 1000: 
        isEspecialInimigo2 = True
        especialinimigo = inimigosImgs[2]
        especialInimigo2Enable = True

    especialInimigo2Pontuacao += 1

    if especialInimigo2Timer > 0:
        especialInimigo2Enable = False
        especialInimigo2Timer += 1
    if especialInimigo2Timer > 300:
        isEspecialInimigo2 = False
        especialinimigo = inimigosImgs[0]
        especialInimigo2Pontuacao = 0
        especialInimigo2Timer = 0
        
    if especialInimigo2Enable:
        especialInimigo2Timer = 1

    if isEspecialInimigo2:
        janela.blit(preto, (150, OFFSET))

    # Osmar
    if especialInimigo3Pontuacao > 100: 
        isEspecialInimigo3 = True
        especialinimigo = inimigosImgs[2]
        especialInimigo3Enable = True

    especialInimigo3Pontuacao += 1

    if especialInimigo3Timer > 0:
        especialInimigo3Enable = False
        especialInimigo3Timer += 1
    if especialInimigo3Timer > 230:
        isEspecialInimigo3 = False
        especialinimigo = inimigosImgs[0]
        especialInimigo3Pontuacao = 0
        especialInimigo3Timer = 0
        
    if especialInimigo3Enable:
        especialInimigo3Timer = 1

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

    global isEspecial2
    global especial2Timer
    global especial2Enabled
    global especial2Pontuacao

    global isEspecial3
    global especial3Timer
    global especial3Enabled
    global especial3Pontuacao

    global isEspecialInimigo1
    global especialInimigo1Timer
    global especialInimigo1Pontuacao
    global especialInimigo1Enable

    global especialinimigo

    keys = pygame.key.get_pressed()

    # Movimentos da Thay
    if not isEspecialInimigo1:
        if keys[pygame.K_DOWN] and ThayNave.y < HEIGHT - ThayNave.height - 1:
            ThayNave.y += ThayNave.vel
        # Move pra cima até a margem
        if keys[pygame.K_UP] and ThayNave.y > OFFSET + 1:
            ThayNave.y -= ThayNave.vel
    else:    
        if keys[pygame.K_UP] and ThayNave.y < HEIGHT - ThayNave.height - 1:
            ThayNave.y += ThayNave.vel
        # Move pra cima até a margem
        if keys[pygame.K_DOWN] and ThayNave.y > OFFSET + 1:
            ThayNave.y -= ThayNave.vel

    if especialInimigo1Timer > 0:
        especialInimigo1Enable = False
        especialInimigo1Timer += 1
    if especialInimigo1Timer > 250:
        isEspecialInimigo1 = False
        especialinimigo = inimigosImgs[0]
        especialInimigo1Pontuacao = 0
        especialInimigo1Timer = 0
        
    if especialInimigo1Enable:
        especialInimigo1Timer = 1

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
        isEspecial1 = False
        especial1Enabled = False
        especial1Pontuacao = 0
        especial1Timer = 0

        
    if especial2Timer > 0:
        especial2Timer += 1
    if especial2Timer > 250:
        isEspecial2 = False
        especial2Enabled = False
        especial2Pontuacao = 0
        ThayNave.especial2(isEspecial2)
        especial2Timer = 0


    if especial3Timer > 0:
        especial3Timer += 1
    if especial3Timer > 250:
        isEspecial3 = False
        especial3Enabled = False
        especial3Pontuacao = 0
        ThayNave.especial3(isEspecial3)
        especial3Timer = 0


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