import pygame

pygame.init()
WIDTH, HEIGHT = 800, 600
fonte = pygame.font.Font('freesansbold.ttf', 20)
tela = pygame.display.set_mode((WIDTH, HEIGHT))


class Palheta:
    def __init__(self, posx, posy, width, height, speed, color):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.rect = pygame.Rect(posx, posy, width, height)
        self.draw = pygame.draw.rect(tela, self.color, self.rect)

    def display(self):
        self.draw = pygame.draw.rect(tela, self.color, self.rect)

    def movimento(self, yFac):
        self.posy = self.posy + self.speed * yFac
        print(self.posy, self.posx, self.speed, "print")
        if self.posy <= 0:
            self.posy = 0
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - self.height

        self.rect = (self.posx, self.posy, self.width, self.height)

    def drawPlacar(self, text, score, x, y, color):
        text = fonte.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        tela.blit(text, textRect)

    def getRect(self):
        return self.rect
