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
PROJETIL_VEL = 2
PROJETIL_IS_MOVING = False
RUN = True

pygame.init()
janela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ThayShooter")


def run():
    global RUN
    global THAY_HEIGHT
    global THAY_WIDTH
    global THAY_X
    global THAY_Y
    global THAY_VEL
    global PROJETIL_HEIGHT
    global PROJETIL_WIDTH
    global PROJETIL_X
    global PROJETIL_Y
    global PROJETIL_VEL

    while RUN:
        pygame.time.delay(6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False

        movimentos()

        janela.fill((0))

        pygame.draw.rect(janela, (255, 255, 255),
                         (THAY_X, THAY_Y, THAY_WIDTH, THAY_HEIGHT))
        pygame.draw.rect(janela, (255, 255, 255),
                         (PROJETIL_X, PROJETIL_Y, PROJETIL_WIDTH, PROJETIL_HEIGHT))
        pygame.display.update()

    pygame.quit()


def movimentos():
    global RUN
    global THAY_HEIGHT
    global THAY_WIDTH
    global THAY_X
    global THAY_Y
    global THAY_VEL
    global PROJETIL_HEIGHT
    global PROJETIL_WIDTH
    global PROJETIL_X
    global PROJETIL_Y
    global PROJETIL_VEL
    global PROJETIL_IS_MOVING

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and THAY_X > 0:
        THAY_X -= THAY_VEL
    if keys[pygame.K_RIGHT] and THAY_X < WIDTH - THAY_WIDTH:
        THAY_X += THAY_VEL
    if keys[pygame.K_DOWN] and THAY_Y < HEIGHT - THAY_HEIGHT:
        THAY_Y += THAY_VEL
    if keys[pygame.K_UP] and THAY_Y > 0:
        THAY_Y -= THAY_VEL
    if keys[pygame.K_SPACE]:
        PROJETIL_IS_MOVING = True

    while PROJETIL_IS_MOVING:
        PROJETIL_X += PROJETIL_VEL

    if keys[pygame.K_ESCAPE]:
        RUN = False


if __name__ == "__main__":
    run()
