import pygad
import numpy
import random
from palheta import Palheta
from bola import Bola

score = random.randint(0,100)
#bola_posx = Bola.posx
#bola_posy = Bola.posy
#jog_posy = Palheta.posy
#jog_posx = Palheta.posx
function_inputs = [score]
def fitness_func(ga_instance, solution, solution_idx):
    fitness = function_inputs
    return fitness

def montarAlgoritmoGenetico(num_generations,
                              num_parents_mating,
                              sol_per_pop,num_genes,
                              init_range_low,
                              init_range_high,
                              parent_selection_type,
                              keep_parents,
                              crossover_type,
                              mutation_type,
                              mutation_percent_genes):
    fitness_function = fitness_func

    num_generations = 100
    num_parents_mating = 4
    sol_per_pop = 8
    num_genes = len(function_inputs)

    init_range_low = -2
    init_range_high = 5

    parent_selection_type = "sss"
    keep_parents = 1

    crossover_type = "single_point"

    mutation_type = "random"
    mutation_percent_genes = 10

    ga_instance = pygad.GA(num_generations=num_generations,
                        num_parents_mating=num_parents_mating,
                        fitness_func=fitness_function,
                        sol_per_pop=sol_per_pop,
                        num_genes=num_genes,
                        init_range_low=init_range_low,
                        init_range_high=init_range_high,
                        parent_selection_type=parent_selection_type,
                        keep_parents=keep_parents,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        mutation_percent_genes=mutation_percent_genes)

    ga_instance.run()


montarAlgoritmoGenetico(100,4,8,1,-2,5,"sss",1,"single_point","random",10)