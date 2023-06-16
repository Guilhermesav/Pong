import numpy
import palheta
import bola
import pygad
from pygad import gann
from pygad.gann import GANN

class RN:
    def __init__(self,num_inputs,num_hidden_lay,tam_output,peso1,peso2):
        self.num_inputs = num_inputs
        self.num_hidden_lay = num_hidden_lay
        self.tam_output = tam_output
        self.peso1 = peso1
        self.peso2 = peso2
            
    def feed_foward(self, input):
        hidden_lay = self.relu(numpy.dot(input, self.peso1))
        tam_output = self.sigmoid(numpy.dot(hidden_lay, self.peso2))
        print(tam_output)
        return tam_output

    def relu(self, x):
        return max(0, x)

    def sigmoid(self, x):
        return 1 / (1 + numpy.exp(-x))