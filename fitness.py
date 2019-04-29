
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