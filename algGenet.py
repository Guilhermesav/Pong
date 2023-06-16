import pygad
import numpy
import pygame
import random
from palheta import Palheta
from bola import Bola
from redeneural import RN
WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
tela = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

class AlgGenet():
    def __init__(self):
        self.palhetas = []

    def criar_pop(self,tam_pop):
        for x in range(tam_pop):
            palheta = Palheta(20, 0, 10, 100, 7, WHITE,0,numpy.random.uniform(-1,1,3),numpy.random.uniform(-1,1,1))
            self.palhetas.append(palheta)
             
    def select_pais(self):
        parents = []
        total = 0
        for x in range(len(self.palhetas)):
            total += self.palhetas[x].fitness
        fitness_normalizado = [self.palhetas[x].fitness/total for x in range(len(self.palhetas))]

        cumulative_fitness = []
        start = 0
        for norm_value in fitness_normalizado:
            start+=norm_value
            cumulative_fitness.append(start)

        population_size = len(self.palhetas)

        for count in range(population_size):
            random_number = random.uniform(0, 1)
            individual_number = 0
            for score in cumulative_fitness:
                if(random_number<=score):
                    parents.append(self.palhetas[individual_number])
                    break
            individual_number+=1
        return parents
    
    def crossover(self,pai,mae):
        filho_ent = numpy.mean([pai.genom_ent,mae.genom_ent],axis=0)
        filho_ext = numpy.mean([pai.genom_ext,mae.genom_ext],axis=0)
        palheta = Palheta(20, 0, 10, 100, 7, WHITE,0,filho_ent,filho_ext)
        return palheta
    
    def mutacao(self, palheta):
        palheta.genom_ent = numpy.random.uniform(-1,1,3)
        palheta.genom_ext = numpy.random.uniform(-1,1,1)    
        
    def jogo(self,bola,geracao):
        reserva = self.palhetas.copy()
        for palheta in self.palhetas:
            rn = RN(3,6,1,palheta.genom_ent,palheta.genom_ext)
            while True:
                pygame.display.update()
                tela.fill(BLACK)
                palheta.display()
                bola.display()
                palheta.drawPlacar("Fitness: ", palheta.fitness, 100, 20, WHITE)
                palheta.drawPlacar("Geração: ", geracao, 300, 20, WHITE)
                palheta.drawPlacar("Individuo:  ", self.palhetas.index(palheta), 500, 20, WHITE)
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                for jogador in self.palhetas:
                    if pygame.Rect.colliderect(bola.getRect(), jogador.getRect()):
                        palheta.fitness += 500
                        bola.colisao()
                
              
                palheta.segue_bola(rn,bola)

                ponto = bola.updateTreino()

                if ponto == -1: #direita
                    bola.resetTreino()
                elif ponto == 1: #esquerda
                    reserva.remove(palheta)
                    bola.reset()
                    break

                pygame.display.update()
                clock.tick(FPS)
                palheta.fitness +=1
            
        
    def treino(self):
       bola = Bola(WIDTH // 2, HEIGHT // 2, 7, 10, WHITE)
       self.criar_pop(20)
       for x in range(50):
           self.jogo(bola,x)
           new_gen = []
           top_percentual = int((20 * len(self.palhetas))/100)
           self.palhetas.sort(key=lambda palheta: palheta.fitness,reverse= True)
           new_gen = self.palhetas[:top_percentual]
           while len(new_gen) < len(self.palhetas):
               pais = self.select_pais()
               filho = self.crossover(pais[0],pais[1])
               if random.random() < 0.5:
                  self.mutacao(filho)
               new_gen.append(filho)
           self.palhetas = new_gen
       print(self.palhetas)

if __name__ == "__main__":
    game = AlgGenet()
    game.treino()    
    pygame.quit()
