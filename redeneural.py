import pygad
import pygad.gann
import numpy
import palheta
import bola
jogador = palheta.Palheta()
ball = bola.Bola()
games = []
game_inputs = numpy.array(jogador.posy,ball.posx,ball.posy)
solucoes = ""
num_inputs = game_inputs.shape[1]

for game in games:
    GANN_instance = pygad.gann.GANN(num_solutions=solucoes,
                                num_neurons_input=num_inputs,
                                num_neurons_hidden_layers=[6],
                                num_neurons_output=1,   
                                hidden_activations=["relu"],
                                output_activation="softmax")