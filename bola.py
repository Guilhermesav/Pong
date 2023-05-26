import pygame
WIDTH, HEIGHT = 800, 600

tela = pygame.display.set_mode((WIDTH,HEIGHT))
class Bola:
    def __init__(self, posx, posy, radius, speed, color):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.speed = speed
        self.color = color
        self.xFac = 1
        self.yFac = -1
        self.ball = pygame.draw.circle(tela, self.color, (self.posx, self.posy), self.radius)
        self.contato = 1

    def display(self):
        self.ball = pygame.draw.circle(tela, self.color, (self.posx, self.posy), self.radius)

    def update(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac
  
        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
        if self.posx <= 0 and self.contato:
            self.contato = 0
            return 1
        elif self.posx >= WIDTH and self.contato:
            self.contato = 0
            return -1
        else:
            return 0
        
    def updateTreino(self):
        self.posx += self.speed*self.xFac
        self.posy += self.speed*self.yFac

        if self.posy <= 0 or self.posy >= HEIGHT:
            self.yFac *= -1
        if self.posx <= 0 and self.contato:
            self.contato = 0
            return 1
        elif self.posx >= WIDTH and self.contato:
            self.contato = 0
            return -1
        else:
            return 0
        
    def reset(self):
        self.posx = WIDTH//2
        self.posy = HEIGHT//2
        self.xFac *= -1
        self.contato = 1
        
    def resetTreino(self):
        self.xFac *= -1
        self.contato = 1

    def colisao(self):
        self.xFac *= -1    
    
    def getRect(self):
        return self.ball