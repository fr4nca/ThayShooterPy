import pygame
from os import path

WIDTH = 780
HEIGHT = 510
THAYSHOOTER = '../assets/zorque.ttf'
OPTIONS = '../assets/upheavtt.ttf'
MENU_BG = pygame.image.load(path.join('../assets', 'menu.jpg'))

janela = pygame.display.set_mode((WIDTH, HEIGHT))

white=(255, 255, 255)
select_color=(255, 255, 0)
yellow=(255, 255, 0)


def text_format(msg, font, size, color):
    fonte=pygame.font.Font(font, size)
    texto=fonte.render(msg, 0, color)
    return texto

class Menu:

    def menu_inicial():        
        selected="start"
        menu=True

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="start"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="start":       
                            menu=False
                        if selected=="quit":
                            pygame.quit()
                            quit()
            
            janela.fill((0,0,0))
            janela.blit(MENU_BG,(0, 0))

            title=text_format("ThayShooter",THAYSHOOTER, 80, white)
            if selected=="start":
                text_start=text_format("START", OPTIONS, 60, select_color)
            else:
                text_start = text_format("START",  OPTIONS,60, white)
            if selected=="quit":
                text_quit=text_format("QUIT",  OPTIONS,60, select_color)
            else:
                text_quit = text_format("QUIT",OPTIONS,  60, white)
    
            title_rect=title.get_rect()
            start_rect=text_start.get_rect()
            quit_rect=text_quit.get_rect()
    
            
            janela.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
            janela.blit(text_start, (WIDTH/2 - (start_rect[2]/2), 250))
            janela.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 310))
            pygame.display.update()
            pygame.display.set_caption("Menu")

    def game_over(score):

        selected="restart"
        recorde = 0
        menu=True

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="restart"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN:
                        if selected=="restart":       
                            menu=False
                        if selected=="quit":
                            pygame.quit()
                            quit()
    
            
            janela.fill((0,0,0))
            janela.blit(MENU_BG,(0, 0))

            title=text_format("GameOver",OPTIONS, 90, yellow)
            pontuacao= text_format('Pontuação: %.0f'%score, OPTIONS,50, white)
            if selected=="restart":
                text_restart=text_format("RESTART",  OPTIONS,60, select_color)
            else:
                text_restart = text_format("RESTART",  OPTIONS,60, white)
            if selected=="quit":
                text_quit= text_format("QUIT",  OPTIONS,60, select_color)
            else:
                text_quit = text_format("QUIT",  OPTIONS,60, white)

            title_rect=title.get_rect()
            pontuacao_rect=pontuacao.get_rect()
            start_rect=text_restart.get_rect()
            quit_rect=text_quit.get_rect()
    
            janela.blit(title, (WIDTH/2 - (title_rect[2]/2), 80))
            janela.blit(pontuacao, (WIDTH/2 - (pontuacao_rect[2]/2), 180))
            janela.blit(text_restart, (WIDTH/2 - (start_rect[2]/2), 280))
            janela.blit(text_quit, (WIDTH/2 - (quit_rect[2]/2), 340))
            pygame.display.update()
            pygame.display.set_caption("GameOver")