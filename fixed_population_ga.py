import random

def create_population(size):
    return [random.randint(0, 31) for _ in range(size)]

def fitness(x):
    return x**2

def genetic_algorithm():
    pop_size = 4
    pop = create_population(pop_size)

    for _ in range(5):
        pop = sorted(pop, key=fitness, reverse=True)
        parents = pop[:2]

        child = (parents[0] + parents[1]) // 2
        child += random.randint(-2, 2)

        pop = parents + [child]

        while len(pop) < pop_size:
            pop.append(random.randint(0, 31))

    best = max(pop, key=fitness)
    print("Best:", best)

genetic_algorithm()