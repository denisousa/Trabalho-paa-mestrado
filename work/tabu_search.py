import random
import time
import copy

nv = 3  # número de vizinhos
tabu_size = 7  # max tamanho da fila tabu


def generate_neighborhood(solution):
    global nv
    neighborhood = []
    while len(neighborhood) < nv:
        neighbor = copy.deepcopy(solution[0])
        random.seed(time.time())
        index1, index2 = random.sample(range(0, len(solution)), k=2)
        neighbor[index1] = not neighbor[index1]
        neighbor[index2] = not neighbor[index2]
        if not [True for i in neighborhood if i[0] == neighbor]:
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


def aspiration(best_solution, best_value, current_value):
    if best_value > current_value:
        return True
    return False


def update_tabu(queue, value):
    global tabu_size
    if len(queue) >= tabu_size:
        queue.pop(0)
    queue.append(sorted(value))
    return queue


def tabu_search(initial_solution, clauses):
    current_solution = copy.deepcopy(initial_solution)
    current_value = assignment(current_solution[0], clauses)
    tabu_queue = []
    count = 0

    while count < 50:
        neighborhood = generate_neighborhood(current_solution)
        neighborhood_values = [
            assignment(neighborhood[i][0], clauses) for i in range(len(neighborhood))
        ]
        max_index = neighborhood_values.index(max(neighborhood_values))
        best_solution = neighborhood[max_index]
        visited = [False for i in range(len(neighborhood_values))]
        while True or visited.count(False) == 0:
            # check if all elements have been visited
            visited[max_index] = True
            if sorted(best_solution[1:3]) in tabu_queue:
                if aspiration(
                    best_solution, neighborhood_values[max_index], current_value
                ):
                    current_solution = best_solution
                    break
                else:
                    neighborhood_values[max_index] = 0
                    max_index = neighborhood_values.index(max(neighborhood_values))
                    best_solution = neighborhood[max_index]
            else:
                current_solution = best_solution
                current_value = neighborhood_values[max_index]
                tabu_queue = update_tabu(tabu_queue, current_solution[1:3])
                break
        count += 1

    return current_solution, current_value


def main():
    sat_file = "instance_files/SAT1.txt"

    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

    initial_solution = ([False for i in range(range_literal)], -1, -1)
    print(tabu_search(initial_solution, clauses))


main()
