import random

def create_population(size):
    return [random.randint(0, 31) for _ in range(size)]

def fitness(x):
    return x**2

def genetic_algorithm():
    pop_size = 10
    max_value = 31
    pop = create_population(pop_size)

    best_overall = max(pop, key=fitness)

    for generation in range(50):
        pop = sorted(pop, key=fitness, reverse=True)
        parents = pop[:2]

        child = (parents[0] + parents[1]) // 2
        child += random.randint(-5, 5)

        pop = parents + [child]

        while len(pop) < pop_size:
            pop.append(random.randint(0, max_value))

        current_best = max(pop, key=fitness)
        if fitness(current_best) > fitness(best_overall):
            best_overall = current_best

        # 🎯 early stop
        if best_overall == max_value:
            print("Optimal found early!")
            break

    print("Final Best:", best_overall)
    print("Fitness:", fitness(best_overall))

genetic_algorithm()