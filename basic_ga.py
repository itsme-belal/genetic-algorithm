import random

def genetic_algorithm():
    pop = [random.randint(0, 31) for _ in range(4)]

    for _ in range(5):
        pop = sorted(pop, key=lambda x: x**2, reverse=True)
        parents = pop[:2]

        child = (parents[0] + parents[1]) // 2
        child = child + random.randint(-2, 2)

        pop = parents + [child]

    best = max(pop, key=lambda x: x**2)
    print("Best:", best)

genetic_algorithm()