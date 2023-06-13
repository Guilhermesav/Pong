import pygame, palheta as Palheta, bola as Bola
from palheta import Palheta
from bola import Bola


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
class Pong:
    def draw(text,x, y, color):
            text = fonte.render(text, True, color)
            textRect = text.get_rect()
            textRect.center = (x, y)
            tela.blit(text, textRect)

    def start_game():
        running = True

        jog1 = Palheta(20, 0, 10, 100, 7, WHITE,0)
        jog2 = Palheta(WIDTH - 20, 0, 10, 100, 7, WHITE,0)
        bola = Bola(WIDTH // 2, HEIGHT // 2, 7, 10, WHITE)

        jogadores = [jog1, jog2]

        jog1YFac, jog2YFac = 0, 0
        escolha = "1"
        while running:

            while escolha == "0":
                tela.fill(BLACK)

                Pong.draw("Pong", 400, 50, WHITE)
                
                Pong.draw("Multi Player",400,300, WHITE)
                Pong.draw("Single Player",400,350, WHITE)
                Pong.draw("Treinar IA", 400, 400, WHITE)
            
                if pygame.mouse.get_pressed():
                    if pygame.mouse.get_pos() == (400, 300):
                        escolha = "multiplayer"
                    pygame.display.update()
            
            while escolha ==  "1":
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
                        if event.key == pygame.K_w:
                            jog1YFac = -1
                        if event.key == pygame.K_s:
                            jog1YFac = 1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            jog2YFac = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            jog1YFac = 0
                for jogador in jogadores:
                        if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                            bola.colisao()
                            
                #jog1.IA_segue_bola(bola)
                jog1.movimento(jog1YFac)
                ponto = bola.updateTreino()

                if ponto == -1:
                    jog1.score +=1
                    bola.resetTreino()
                elif ponto == 1:
                    bola.reset()

                jog1.drawPlacar("Jogador 1 : ", jog1.score, 100, 20, WHITE)
                jog1.display()
                bola.display()
                pygame.display.update()
                clock.tick(FPS)

            while escolha == "2":
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
                        if event.key == pygame.K_w:
                            jog1YFac = -1
                        if event.key == pygame.K_s:
                            jog1YFac = 1
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                            jog2YFac = 0
                        if event.key == pygame.K_w or event.key == pygame.K_s:
                            jog1YFac = 0

                    for jogador in jogadores:
                        if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                            bola.colisao()

                jog1.movimento(jog1YFac)
                jog2.movimento(jog2YFac)
                ponto = bola.update()
                if ponto == -1:
                    jog1.score += 1
                    bola.reset()
                elif ponto == 1:
                    jog2.score += 1
                    bola.reset()

                jog1.display()  
                #jog2.display()
                bola.display()
                jog1.drawPlacar("Jogador 1 : ", jog1.score, 100, 20, WHITE)
                jog2.drawPlacar("Jogador 2 : ", jog2.score, WIDTH - 100, 20, WHITE)
                pygame.display.update()
                clock.tick(FPS)
            
            pygame.display.update()
            clock.tick(FPS)
        


if __name__ == "__main__":
    Pong.start_game()
    pygame.quit()
