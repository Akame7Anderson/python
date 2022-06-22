import pygame
from random import randint #função randomiza valores
pygame.font.init() # Inicializa objeto font
pygame.init #iniciar aplicação

x = 380
y = 100
pos_x = 526
pos_y = 1200
pos_y_a = 800
pos_y_c = 2000 
velocidade = 25
velocidade_outros = 12

timer = 0
tempo_segundos = 0


fundo = pygame.image.load('imgfundo.png')
cachorro1 = pygame.image.load('cachorro1.png')
cachorro2 = pygame.image.load('cachorro2.png')
cachorro = pygame.image.load('cachorro.png')
cachorro4 = pygame.image.load('cachorro4.png')

#time
font = pygame.font.SysFont('arial',30) #objeto fonte
texto = font.render("Tempo: ",True,(255,255,255),(0,0,0)) #cor da letra e fonte
pos_texto = texto.get_rect()
pos_texto.center = (65,50)

#criando janela
janela = pygame.display.set_mode((800,600)) #tamanho tela
pygame.display.set_caption("Jogo em Python") #nome da tela

janela_aberta = True
while janela_aberta : #enquanto janela aberta
    pygame.time.delay(50)
    for event in pygame.event.get() : #aguarda evento get
        if event.type == pygame.QUIT:# se evento get for QUIT 
            janela_aberta = False # janela vai encerrar

    # comando de movimentação
    comandos = pygame.key.get_pressed()
#    if comandos[pygame.K_UP]: #seta pra cima
#        y -= velocidade #decrementar
#    if comandos[pygame.K_DOWN]:
#        y += velocidade
    if comandos[pygame.K_LEFT] and x >=230:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 520:
        x += velocidade
    #if(pos_y <= -200):
     #   pos_y = 900
    # pos_y -= velocidade_outros

    #detecta a colisão
    if ((x + 80 > pos_x and y + 180 > pos_y)): #COLISÃO DIREITA
        y = 1200

    if ((x - 80 < pos_x - 300 and y + 180 > pos_y_a)): #COLISÃO ESQUERDA
        y = 1200

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c)) and ((x - 80 < pos_x - 136 and y + 180 > pos_y_c)): #COLISÃO CENTRAL
        y = 1200


    #movimentação cachorros
    if (pos_y <= -80) :
        pos_y = randint(800,1000)

    if (pos_y_a <= -80):
        pos_y_a = randint(1200,2000)

    if (pos_y_c <= -80):
        pos_y_c = randint(2200,3000)

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +5
    pos_y_c -= velocidade_outros +12

    if (timer < 20):
        timer +=1
    else :
        tempo_segundos +=1
        texto = font.render("Tempo: "+str(tempo_segundos),True,(255,255,255),(0,0,0)) #cor da letra e fonte
        timer = 0

    pos_y  -= velocidade_outros
    pos_y_a -= velocidade_outros +2
    pos_y_c -= velocidade_outros +10

    janela.blit(fundo,(0,0))
    janela.blit(cachorro,(x,y))
    janela.blit(cachorro1,(pos_x,pos_y))
    janela.blit(cachorro2,(pos_x  - 300,pos_y_a))
    janela.blit(cachorro4,(pos_x - 136,pos_y_c))
    janela.blit(texto,pos_texto)
    pygame.display.update()








pygame.QUIT() # Encerrar o game
