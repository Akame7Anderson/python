import pygame
pygame.init #iniciar aplicação

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho da tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta : #enquanto janela aberta
    for event in pygame.event.get() : #aguarda evento get
        if event.type == pygame.QUIT: #se evento get for QUIT
            janela_aberta = False #janela vai encerrar
    pygame.draw.circle(janela)

















pygame.QUIT()# Encerrar jogo
