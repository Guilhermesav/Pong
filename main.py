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
FPS = 30


def main():
    running = True

    jog1 = Palheta(20, 0, 10, 100, 10, WHITE)
    jog2 = Palheta(WIDTH - 20, 0, 10, 100, 10, WHITE)
    bola = Bola(WIDTH // 2, HEIGHT // 2, 7, 7, WHITE)

    jogadores = [jog1, jog2]

    jog1Score, jog2Score = 0, 0
    jog1YFac, jog2YFac = 0, 0
    while running:

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
            jog1Score += 1
            bola.reset()
        elif ponto == 1:
            jog2Score += 1
            bola.reset()

        jog1.display()
        jog2.display()
        bola.display()
        jog1.drawPlacar("Jogador 1 : ", jog1Score, 100, 20, WHITE)
        jog2.drawPlacar("Jogador 2 : ", jog2Score, WIDTH - 100, 20, WHITE)
        pygame.display.update()
        # Adjusting the frame rate
        clock.tick(FPS)


if __name__ == "__main__":
    main()
    pygame.quit()