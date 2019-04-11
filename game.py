import pygame

WIDTH = 800
HEIGHT = 500
THAY_WIDTH = 60
THAY_HEIGHT = 40
THAY_X = 50
THAY_Y = 80
THAY_VEL = 3
PROJETIL_WIDTH = 40
PROJETIL_HEIGHT = 10
PROJETIL_X = THAY_X
PROJETIL_Y = THAY_Y + ((THAY_HEIGHT / 2) - PROJETIL_HEIGHT / 2)
PROJETIL_VEL = 4
PROJETIL_IS_MOVING = False
RUN = True
#MERGEEEEEE THAAAAAAY
pygame.init()
janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ThayShooter")

def run():
    global RUN

    while RUN:
        pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        movimentos()

        janela.fill((0))

        pygame.draw.rect(janela, (255, 255, 255), (THAY_X, THAY_Y, THAY_WIDTH, THAY_HEIGHT))
        pygame.draw.rect(janela, (255, 255, 255), (PROJETIL_X, PROJETIL_Y, PROJETIL_WIDTH, PROJETIL_HEIGHT))
        pygame.display.update()

    pygame.quit()


def movimentos():
    global RUN
    global THAY_X
    global THAY_Y
    global PROJETIL_X
    global PROJETIL_IS_MOVING

    keys = pygame.key.get_pressed()

# Movimentos da Thay
    # Move pra esquerda até a margem
    if keys[pygame.K_LEFT] and THAY_X > 0:
        THAY_X -= THAY_VEL
    # Move pra direita até a margem
    if keys[pygame.K_RIGHT] and THAY_X < WIDTH - THAY_WIDTH:
        THAY_X += THAY_VEL
    # Move pra baixo até a margem
    if keys[pygame.K_DOWN] and THAY_Y < HEIGHT - THAY_HEIGHT:
        THAY_Y += THAY_VEL
    # Move pra cima até a margem
    if keys[pygame.K_UP] and THAY_Y > 0:
        THAY_Y -= THAY_VEL

# Movimentos do projétil
    # Atira o projétil
    if not(PROJETIL_IS_MOVING):
        if keys[pygame.K_SPACE]:
            PROJETIL_IS_MOVING = True
    else:
        PROJETIL_X += PROJETIL_VEL

    # Move o projétil até o final e volta para a posição inicial
    if PROJETIL_X >= WIDTH:
        PROJETIL_X = THAY_X
        PROJETIL_IS_MOVING = False

    if keys[pygame.K_ESCAPE]:
        RUN = False

if __name__ == "__main__":
    run()
