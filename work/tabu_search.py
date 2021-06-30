import random
import time
import copy

nv = 3  # número de vizinhos
tabu_size = 7  # max tamanho da fila tabu


def generate_neighborhood(solution):
    global nv
    neighborhood = []
    while len(neighborhood) < nv:
        neighbor = copy.deepcopy(solution)
        random.seed(time.time())
        index1, index2 = random.sample(range(0, len(solution)), k=2)
        neighbor[index1] = not neighbor[index1]
        neighbor[index2] = not neighbor[index2]
        if neighbor not in neighborhood:
            neighborhood.append((neighbor, index1, index2))

    return neighborhood


def assignment(literals, clauses):
    true_clauses = 0
    for clause in clauses:
        l1 = (
            literals[abs(clause[0]) - 1]
            if clause[0] > 0
            else not literals[abs(clause[0]) - 1]
        )
        l2 = (
            literals[abs(clause[1]) - 1]
            if clause[1] > 0
            else not literals[abs(clause[1]) - 1]
        )
        l3 = (
            literals[abs(clause[2]) - 1]
            if clause[2] > 0
            else not literals[abs(clause[2]) - 1]
        )
        r = l1 and l2 and l3
        if r:
            true_clauses += 1
    return true_clauses


def aspiration(current_value):
    pass


def update_tabu(queue, value):
    global tabu_size
    if len(queue) >= tabu_size:
        queue.pop(0)
    return queue.append(value)


def tabu_search(initial_solution, clauses):
    current_solution = copy.deepcopy(initial_solution)
    current_value = assignment(current_solution, clauses)
    tabu_queue = []

    neighborhood = generate_neighborhood(current_solution)
    for neighbor in neighborhood:
        neighbor_value = assignment(neighbor[0], clauses)
        if neighbor_value > current_value:
            current_solution = neighbor[0]
            current_value = neighbor_value
            tabu_queue = update_tabu(tabu_queue, neighbor[1:3])

    return current_solution, current_value


def main():
    sat_file = "instance_files/test.txt"

    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

    initial_solution = [False for i in range(range_literal)]
    print(tabu_search(initial_solution, clauses))


main()
