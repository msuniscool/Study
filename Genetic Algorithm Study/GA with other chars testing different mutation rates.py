import random
import time
import string

# === CONFIG ===
TARGET = "Ax&L24!(asdf) 67JJg04!*"
POP_SIZE = 100
MUTATION_RATE = 0.01
GENERATIONS = 1000000
RUNS = 10

# More space characters to improve evolution toward spaces
CHARS = string.printable[:-6] + "          "

def fitness(individual):
    # Closer characters get partial credit
    return -sum(abs(ord(i) - ord(j)) for i, j in zip(individual, TARGET))

def create_individual():
    return ''.join(random.choice(CHARS) for _ in range(len(TARGET)))

def crossover(parent1, parent2):
    idx = random.randint(0, len(TARGET) - 1)
    return parent1[:idx] + parent2[idx:]

def mutate(individual):
    return ''.join(
        c if random.random() > MUTATION_RATE else random.choice(CHARS)
        for c in individual
    )

# === Run multiple simulations ===
generation_counts = []
time_durations = []

for run in range(RUNS):
    print(f"\n=== RUN {run + 1} ===")
    population = [create_individual() for _ in range(POP_SIZE)]
    start_time = time.time()

    for generation in range(GENERATIONS):
        population = sorted(population, key=fitness, reverse=True)
        best = population[0]
        print(f"Gen {generation}: {best} (Fitness: {fitness(best)})")
        if best == TARGET:
            break

        top = population[:POP_SIZE // 5]
        children = []
        while len(children) < POP_SIZE:
            parent1, parent2 = random.sample(top, 2)
            child = mutate(crossover(parent1, parent2))
            children.append(child)

        population = children

    end_time = time.time()
    duration = end_time - start_time

    generation_counts.append(generation + 1)
    time_durations.append(duration)

    print(f"Finished in {generation + 1} generations and {duration:.4f} seconds.")

# === Final Report ===
avg_gen = sum(generation_counts) / RUNS
avg_time = sum(time_durations) / RUNS

print("\n=== Summary over 10 runs ===")
for i in range(RUNS):
    print(f"Run {i + 1}: {generation_counts[i]} generations, {time_durations[i]:.4f} seconds")

print(f"\nAverage generations: {avg_gen:.2f}")
print(f"Average time: {avg_time:.4f} seconds")
