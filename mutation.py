import numpy as np
import random
from operator import itemgetter

def mutation(population, num_queens, population_size, mutation_rate):
	mutant = np.argmax(list(map(itemgetter(-1), population)))
	for gene in range(len(population[mutant])-1):
	 for ngene in range(gene,len(population[mutant])-1):
	 	if (population[mutant][gene].x == population[mutant][ngene].x):
	 		powers = gene
	 		direction = 'H'
	 		break;break
	 	elif (population[mutant][gene].y == population[mutant][ngene].y):
	 		powers = gene
	 		direction = 'V'
	 		break;break
	mutation_prob = random.uniform(0,1)
	if (mutation_prob < mutation_rate):
		individual = population[mutant][powers]
		mutate(individual, num_queens, direction)
		return True
	return False

def mutate(individual, num_queens, direction):
	if (direction == 'H') and (individual.x < num_queens):
		individual.x += 1
	elif (direction == 'V') and (individual.y < num_queens):
		individual.y += 1
