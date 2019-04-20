import random
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
		individiual = []
		for gene in range(num_queens):
			new_ind = Chromosome(num_queens)
			individiual.append(new_ind)
		population.append(individiual)
	return population

def print_population(population):
	for solution in population:
		for individiual_solution in solution:
			print(str(individiual_solution), end = ' ')
		print() 	

def main():
	population_size = 10 
	num_queens = 5
	population = intial_population(population_size, num_queens)
	print_population(population)		

if __name__ == '__main__':
		main()	