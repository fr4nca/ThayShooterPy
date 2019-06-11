import pygame
from os import path
from pygame import font, draw   
from math import floor

WIDTH = 780
HEIGHT = 510
THAYSHOOTER = '../assets/zorque.ttf'
OPTIONS = '../assets/upheavtt.ttf'
MENU_BG = pygame.image.load(path.join('../assets', 'menu.jpg'))
RESUME_BG = pygame.image.load(path.join('../assets', 'bg3.jpg'))

janela = pygame.display.set_mode((WIDTH, HEIGHT))

colorx = (255, 204, 255)
white=(255, 255, 255)
yellow=(255, 255, 0)
blue=(64, 0, 255)



def text_format(msg, font, size, color):
    fonte=pygame.font.Font(font, size)
    texto=fonte.render(msg, 0, color)
    return texto

def janela_blit(janela, texto, pos):
    janela.blit(texto, (WIDTH/2 - (texto.get_width()/2), pos))


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
                    if event.key==pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_x:
                        if selected=="start":       
                            menu=False
                        if selected=="quit":
                            pygame.quit()
                            quit()
            
            janela.fill((0,0,0))
            janela.blit(MENU_BG,(0, 0))

            title=text_format("ThayShooter",THAYSHOOTER, 80, colorx )
            if selected=="start":
                text_start=text_format("START", OPTIONS, 60, yellow)
            else:
                text_start = text_format("START",  OPTIONS,60, white)
            if selected=="quit":
                text_quit=text_format("QUIT",  OPTIONS,60, yellow)
            else:
                text_quit = text_format("QUIT",OPTIONS,  60, white)
                
            janela_blit(janela, title, 80)
            janela_blit(janela, text_start, 250)
            janela_blit(janela, text_quit, 310)
            
            pygame.display.set_caption("Menu")
            pygame.display.update()

    def game_over(score, recorde, novo_recorde):

        selected="restart"
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
                    if event.key==pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_x:
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
                text_restart=text_format("RESTART",  OPTIONS,60, yellow)
            else:
                text_restart = text_format("RESTART",  OPTIONS,60, white)
            if selected=="quit":
                text_quit= text_format("QUIT",  OPTIONS,60, yellow)
            else:
                text_quit = text_format("QUIT",  OPTIONS,60, white)

            if novo_recorde :
                novorecorde = text_format("Novo recorde!", OPTIONS, 60, blue)
                janela_blit(janela, novorecorde, 180)
                janela_blit(janela, pontuacao, 250)
                #janela.blit(novorecorde, (WIDTH/2 - (novorecorde.get_width()/2), 250))
            else:
                text_recorde = text_format('Recorde: %.0f'%recorde, OPTIONS, 50, blue)
                janela_blit(janela, text_recorde, 250)
                janela_blit(janela, pontuacao, 180)
                #janela.blit(text_recorde, (WIDTH/2 - (text_recorde.get_width()/2), 250))

            janela_blit(janela, title, 80)
            
            janela_blit(janela, text_restart, 310)
            janela_blit(janela, text_quit, 360)

            pygame.display.update()
            pygame.display.set_caption("GameOver")

    def resume(hp, pontuacao):        
        selected="resume"
        menu=True

        fonte = pygame.font.SysFont('comicsans', 24, True)

        while menu:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_UP:
                        selected="resume"
                    elif event.key==pygame.K_DOWN:
                        selected="quit"
                    if event.key==pygame.K_RETURN or event.key == pygame.K_KP_ENTER or event.key == pygame.K_x:
                        if selected=="resume":       
                            menu=False
                        if selected=="quit":
                            pygame.quit()
                            quit()
            
            janela.fill((0,0,0))
            janela.blit(RESUME_BG,(0, 30))

            vida = fonte.render("HP: ", 1, (255, 255, 255))
            janela.blit(vida, (5, 10))
            draw.rect(janela, (255, 0, 0), (45, 5, 200, 21))
            draw.rect(janela, (0, 255, 0), (45, 5, 200 - ((200/100) * (100 - hp)), 21))
            pontos = fonte.render("Pontuação: " + str(floor(pontuacao)), 1, (255, 255, 255))
            janela.blit(pontos, (630, 10))
            

            title=text_format("PAUSE",OPTIONS, 80, blue )
            if selected=="resume":
                text_resume=text_format("RESUME", OPTIONS, 60, yellow)
            else:
                text_resume = text_format("RESUME",  OPTIONS,60, white)
            if selected=="quit":
                text_quit=text_format("QUIT",  OPTIONS,60, yellow)
            else:
                text_quit = text_format("QUIT",OPTIONS,  60, white)
    
          
            janela_blit(janela, title, 80)
            janela_blit(janela, text_resume, 250)
            janela_blit(janela, text_quit, 310)
            
            pygame.display.update()
            pygame.display.set_caption("Menu")