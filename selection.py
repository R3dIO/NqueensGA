from operator import itemgetter

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