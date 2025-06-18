import random
import time

# Parameters
TARGET = "The quick brown fox jumped over the lake"
POP_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 100000
CHARS = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fitness function
def fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET) if i == j)

# Create a random individual
def create_individual():
    return ''.join(random.choice(CHARS) for _ in range(len(TARGET)))

# Crossover: single-point
def crossover(parent1, parent2):
    idx = random.randint(0, len(TARGET) - 1)
    return parent1[:idx] + parent2[idx:]

# Mutation
def mutate(individual):
    return ''.join(
        c if random.random() > MUTATION_RATE else random.choice(CHARS)
        for c in individual
    )

# Initialize population
population = [create_individual() for _ in range(POP_SIZE)]

start_time = time.time()

for generation in range(GENERATIONS):
    population = sorted(population, key=fitness, reverse=True)
    best = population[0]
    print(f"Gen {generation}: {best} (Fitness: {fitness(best)})")
    if best == TARGET:
        break

    # Selection: top 20%
    top = population[:POP_SIZE // 5]
    children = []

    while len(children) < POP_SIZE:
        parent1, parent2 = random.sample(top, 2)
        child = mutate(crossover(parent1, parent2))
        children.append(child)

    population = children

end_time = time.time()

print("\n=== Result ===")
print(f"Best match: {best}")
print(f"Generations: {generation + 1}")
print(f"Time taken: {end_time - start_time:.4f} seconds")
