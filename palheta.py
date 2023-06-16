import pygame
from bola import Bola
import random
import math
import redeneural
pygame.init()
WIDTH, HEIGHT = 800, 600
fonte = pygame.font.Font('freesansbold.ttf', 20)
tela = pygame.display.set_mode((WIDTH, HEIGHT))


class Palheta:
    def __init__(self, color,score,genom_ent, genom_ext):
        self.posx = 20
        self.posy = 300
        self.width = 10
        self.height = 100
        self.speed = 12
        self.color = color
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.score = score
        self.contatos = 0
        self.fitness = 0
        self.genom_ent = genom_ent
        self.genom_ext = genom_ext

    def display(self):
        self.draw = pygame.draw.rect(tela, self.color, pygame.Rect(self.posx, self.posy, self.width, self.height))

    def movimento(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 1
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - (self.height+1)

        self.rect = (self.posx, self.posy, self.width, self.height)

    def drawPlacar(self, text, score, x, y, color):
        text = fonte.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        tela.blit(text, textRect)

    def getRect(self):
        return self.rect
    
   
    #"macete"
    def IA_segue_bola(self,bola):
        if (bola.posy + bola.radius) > (self.posy + self.height):
            if self.posy + self.height < HEIGHT :
                self.movimento(1)
        elif (bola.posy + bola.radius) < (self.posy + self.height) and self.posy > 0:
            self.movimento(-1)

    def segue_bola(self,rede,bola):
        y_pos = self.posy
        bola_posy = bola.posy
        bola_posx = bola.posx
        dist = bola_posx - self.posx
        h_dist = y_pos - bola_posy
        inputs = [y_pos, bola_posy,dist,h_dist,bola_posx]
        output = rede.feed_foward(inputs)[0]
        if output > 0.5: 
            if self.posy + self.height <= HEIGHT:
                self.movimento(-1)
        else: 
            if self.posy > 0:
                self.movimento(1)
            
class PalhetaHumana:
    def __init__(self, color,score,genom_ent, genom_ext):
        self.posx = WIDTH - 20
        self.posy = 300
        self.width = 10
        self.height = 100
        self.speed = 12
        self.color = color
        self.rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        self.score = score
        self.contatos = 0
        self.fitness = 0
        self.genom_ent = genom_ent
        self.genom_ext = genom_ext

    def display(self):
        self.draw = pygame.draw.rect(tela, self.color, pygame.Rect(self.posx, self.posy, self.width, self.height))

    def movimento(self, yFac):
        self.posy = self.posy + self.speed * yFac
        if self.posy <= 0:
            self.posy = 1
        elif self.posy + self.height >= HEIGHT:
            self.posy = HEIGHT - (self.height+1)

        self.rect = (self.posx, self.posy, self.width, self.height)

    def drawPlacar(self, text, score, x, y, color):
        text = fonte.render(text + str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
        tela.blit(text, textRect)

    def getRect(self):
        return self.rect
    
