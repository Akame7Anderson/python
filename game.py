import pygame
pygame.init #iniciar aplicação
x = 400
y = 300
pos_x = 300
pos_y = 300
velocidade = 10
fundo = pygame.image.load('imgfundo.png')
cachorro1 = pygame.image.load('cachorro1.png')
cachorro2 = pygame.image.load('cachorro2.png')
cachorro = pygame.image.load('cachorro.png')
cachorro4 = pygame.image.load('cachorro4.png')

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho da tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta : #enquanto janela aberta
    pygame.time.delay(10)
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
    janela.fill((0,0,0))
    pygame.draw.circle(janela,(0, 255, 0),(x,y), 15)
                                #janela   "cor"    "local,tamanho"

    janela.blit(fundo,(0,0))
    janela.blit(cachorro1,(pos_x - 170,pos_y))
    janela.blit(cachorro2,(pos_x  + 50,pos_y))
    janela.blit(cachorro4,(pos_x + 300,pos_y))
    janela.blit(cachorro,(x,y))

    
    pygame.display.update()
    

















pygame.QUIT()# Encerrar jogo
