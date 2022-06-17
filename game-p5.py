import pygame
from random import randint #função randomiza valores
pygame.font.init() # Inicializa objeto font
pygame.init #iniciar aplicação

x = 400
y = 50
pos_x = 200
pos_y = 800
pos_y_a = 800
pos_y_c = 800
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
    if comandos[pygame.K_LEFT] and x >=180:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 580:
        x += velocidade
    if(pos_y <= -200):
        pos_y = 900
    pos_y -= velocidade_outros

    #movimentação cachorros
    if (pos_y <= -180) and (pos_y_a <= -180) and (pos_y_c <= -180):
        pos_y = randint(800,2000)
        pos_y_a = randint(800,2000)
        pos_y_c = randint(800,2000)

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros +5
    pos_y_c -= velocidade_outros +12

    if (timer < 20):
        timer +=1
    else :
        tempo_segundos +=1
        texto = font.render("Tempo: "+str(tempo_segundos),True,(255,255,255),(0,0,0)) #cor da letra e fonte
        timer = 0

    janela.blit(fundo,(0,0))
    janela.blit(cachorro1,(pos_x - 170,pos_y))
    janela.blit(cachorro2,(pos_x  + 50,pos_y))
    janela.blit(cachorro4,(pos_x + 300,pos_y))
    janela.blit(cachorro,(x,y))
    janela.blit(texto,(5,50))
    pygame.display.update()








pygame.QUIT() # Encerrar o game
