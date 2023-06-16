import pygame, palheta as Palheta, bola as Bola
from palheta import Palheta,PalhetaHumana
from bola import Bola
from redeneural import RN
import time 
import numpy
from algGenet import AlgGenet
pygame.init()
fonte = pygame.font.Font('freesansbold.ttf', 20)
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
tela = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
FPS = 60
def treino_ia(jog1,bola,jogadores,rn):
        pygame.display.update()
        tela.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for jogador in jogadores:
                if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                    bola.colisao()
                    
        #jog1.IA_segue_bola(bola)
        jog1.segue_bola(rn)
        ponto = bola.updateTreino()

        if ponto == -1:
            jog1.score +=1
            bola.resetTreino()
        elif ponto == 1:
            jogadores
            bola.reset()

        jog1.drawPlacar("Jogador 1 : ", jog1.score, 100, 20, WHITE)
        jog1.display()
        bola.display()
        pygame.display.update()
        clock.tick(FPS)

   
class Pong:
    def draw(text,x, y, color):
            text = fonte.render(text, True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)
            tela.blit(text, textRect)
    
    def treino_ia(jog1,bola,jogadores,rn):
        pygame.display.update()
        tela.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for jogador in jogadores:
                if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                    bola.colisao()
                    
        #jog1.IA_segue_bola(bola)
        jog1.segue_bola(rn)
        ponto = bola.updateTreino()

        if ponto == -1:
            jog1.score +=1
            bola.resetTreino()
        elif ponto == 1:
            jogadores
            bola.reset()

        jog1.drawPlacar("Jogador 1 : ", jog1.score, 100, 20, WHITE)
        jog1.display()
        bola.display()
        pygame.display.update()
        clock.tick(FPS)
    def start_game():
        
        running = True
        bola = Bola(WIDTH // 2, HEIGHT // 2, 7, WHITE)
        jogIA = Palheta(WHITE,0,[-0.15273317, -0.15867392, -0.01781071,  0.71855971,  0.26231887],[0.95256012])
        rn = RN(3,6,1,jogIA.genom_ent,jogIA.genom_ext)
        jog2 = PalhetaHumana(WHITE,0,numpy.random.uniform(-1,1,3),numpy.random.uniform(-1,1,1))
       
        jogadores = [jogIA,jog2]

        jog2YFac = 0, 0
        escolha = 0
        while running:

            while escolha == 0:
                tela.fill(BLACK)
                Pong.draw("Pong", 400, 50, WHITE)
                
                Pong.draw("2: VS IA",400,350, WHITE)
                Pong.draw("1: Treinar IA", 400, 300, WHITE)
                Pong.draw("4: Quit", 400, 450, WHITE)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            escolha = 1
                        if event.key == pygame.K_2:
                            escolha = 2
                        if event.key == pygame.K_3:
                            escolha = 3
                        if event.key == pygame.K_4:
                            pygame.QUIT
                pygame.display.update()
                clock.tick(FPS)
            while escolha ==  1:
                treinador = AlgGenet()
                treinador.treino()
            
            while escolha == 2:
                pygame.display.update()
                tela.fill(BLACK)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            jog2YFac = -1
                        if event.key == pygame.K_DOWN:
                            jog2YFac = 1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            jog2YFac = 0
                        if event.key == pygame.K_x:
                            pygame.QUIT
                        
                for jogador in jogadores:
                    if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                        print("contato")
                        bola.colisao()

                jogIA.segue_bola(rn,bola)
                jog2.movimento(jog2YFac)

                ponto = bola.update()
                if ponto == -1: #direita
                    jogIA.score += 1
                    bola.reset()
                elif ponto == 1: #esquerda
                    jog2.score += 1
                    bola.reset()
                
                if jogIA.score == 5:
                    tela.fill(BLACK)
                    Pong.draw("IA WINS",400,200, WHITE)
                    time.sleep(5)
                    break
                if jog2.score == 5:
                    tela.fill(BLACK)
                    Pong.draw("HUMANO WINS",400,200, WHITE)
                    time.sleep(5)
                    break
                jogIA.display()  
                jog2.display()
                bola.display()
                jogIA.drawPlacar("Jogador 1 : ", jogIA.score, 100, 20, WHITE)
                jog2.drawPlacar("Jogador 2 : ", jog2.score, WIDTH - 100, 20, WHITE)
                pygame.display.update()
                clock.tick(FPS)
            
            pygame.display.update()
            clock.tick(FPS)
        


if __name__ == "__main__":
    Pong.start_game()
    pygame.quit()
