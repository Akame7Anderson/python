import pygame
pygame.init #iniciar aplicação
x = 400
y = 300
velocidade = 10

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho da tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta : #enquanto janela aberta
    pygame.time.delay(50)
    for event in pygame.event.get() : #aguarda evento get
        if event.type == pygame.QUIT: #se evento get for QUIT
            janela_aberta = False #janela vai encerrar

    #comando de movimentação
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]: #seta pra cima
        y -= velocidade #decrementar
    if comandos[pygame.K_DOWN]:
        y += velocidade #incrementar
    if comandos[pygame.K_LEFT]: 
        x -= velocidade #decrementar
    if comandos[pygame.K_RIGHT]:
        x += velocidade #incrementar
    pygame.draw.circle(janela,(0, 255, 0),(x,y), 15)
                                #janela   "cor"    "local,tamanho"
    pygame.display.update()

















pygame.QUIT()# Encerrar jogo
