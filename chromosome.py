import random
from operator import itemgetter

class Chromosome:

	def __init__(self, n):
		self.x = random.randint(1, n)
		self.y = random.randint(1, n)
		self.leftDiagonal()
		self.rightDiagonal(n)

	def leftDiagonal(self):
		self.l = self.x + self.y

	def rightDiagonal(self, n):
		self.r = n + self.x - self.y

	def __str__(self):
		return ("[(X: {self.x} Y: {self.y}),(L: {self.l} R: {self.r})]".format(self = self))

def intial_population(population_size, num_queens):
	population = []
	for chromo in range(population_size):
		individual = []
		for gene in range(num_queens):
			new_ind = Chromosome(num_queens)
			individual.append(new_ind)
		individual = fitness(individual)
		population.append(individual)
	return population

def fitness(individual):
	conflicts = 0
	for i in range(len(individual)):
		for j in range(i):
			if (individual[i].x == individual[j].x):
				conflicts += 1
			if (individual[i].y == individual[j].y):
				conflicts += 1
			if ( abs(individual[i].x - individual[j].x)	== abs(individual[i].y - individual[j].y) ):
				conflicts += 1
	individual.append(conflicts)
	return individual
	#print(individual[j], end=" ")

def assign_fitness(population):
	for index in range(len(population)):
		population[index] = fitness(population[index])
	return population

def selection_roulette_wheel(population, pool_size):
	cumulative_fitness = 0
	norm_population = []
	mating_pool = []
	for index in range(len(population)):
		cumulative_fitness = cumulative_fitness + population[index][-1]

	for index in range(len(population)):
		fitness =  (population[index][-1]/cumulative_fitness)
		if index == 0 :
			norm_population.append( fitness )
		else :
			norm_population.append( fitness + norm_population[index-1])

	for index in range(pool_size):
		pointer = random.uniform(0,1) #;print(pointer) ;print(norm_population)
		for itr in range(len(norm_population)):
			if pointer > norm_population[itr-1] and pointer < norm_population[itr] :
				mating_pool.append(population[itr])
				break # ;print( mating_pool)
	return mating_pool

def selection(population,pool_size):
	ordered_population = sorted(population, key=itemgetter(-1))
	ordered_population = ordered_population[:pool_size]
	return ordered_population
	# print_population(ordered_population)

def crossover(mating_pool,num_queens,pool_size,population_size):
	population = []
	while len(population) != population_size:
		kid = []
		father = random.randint(0,pool_size-1)
		mother = random.randint(0,pool_size-1)
		kpoint = random.randint(0,num_queens)
		kid =  mating_pool[father][0:kpoint]
		kid.extend(mating_pool[mother][kpoint:-1])
		population.append(kid)
	return	population

def print_population(population):
	for solution in population:
		for individual_solution in solution:
			print(str(individual_solution), end = ' ')
		print()

def main():
	population_size = 12
	num_queens = 5
	pool_size = 6
	population = intial_population(population_size, num_queens)
	mating_pool = selection(population, pool_size)
	next_gen = assign_fitness(crossover(mating_pool,num_queens,pool_size,population_size))
	print('population');print_population(population);print('\nmating pool');print_population(mating_pool);print('\nnext gen');print_population(next_gen)

if __name__ == '__main__':
		main()