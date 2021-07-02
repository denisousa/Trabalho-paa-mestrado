import random
import time
import copy
import os

nv = 100  # número de vizinhos
tabu_size = 7  # max tamanho da fila tabu
nmax = 5000

def disturb_solution(solution): # REFATOR
    solution_copy = copy.deepcopy(solution[0])
    random.seed(time.time())
    index1, index2 = sorted(random.sample(range(0, len(solution[0])), k=2)) # FIX
    solution_copy[index1] = not solution_copy[index1]
    solution_copy[index2] = not solution_copy[index2]
    return solution_copy, index1, index2

def generate_neighborhood(solution):
    global nv
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, index1, index2 = disturb_solution(solution)
        complete_solution = (troubled_solution, index1, index2)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

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


def aspiration(best_value, current_value):
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

    while count < 5000:
        neighborhood = generate_neighborhood(current_solution)
        neighborhood_values = [
            assignment(neighborhood[i][0], clauses) for i in range(len(neighborhood))
        ]
        max_index = neighborhood_values.index(max(neighborhood_values)) # Index do melhor vizinho
        best_solution = neighborhood[max_index]
        while True:
            # check if all elements have been visited
            #open('log.txt', 'a').write(f'neighborhood_values: {neighborhood_values} | count: {count} \n')
            if sorted(best_solution[1:3]) in tabu_queue:
                ## TODO: change logic for accept
                if aspiration(max(neighborhood_values), current_value):
                    current_solution = best_solution
                    ### current_value
                    break
                else:
                    neighborhood_values[max_index] = 0
                    max_index = neighborhood_values.index(max(neighborhood_values))
                    best_solution = neighborhood[max_index]
            else:
                current_value = max(neighborhood_values)
                tabu_queue = update_tabu(tabu_queue, best_solution[1:3])
                break
        count += 1

    return current_solution, current_value


def main():
    open('log.txt', 'w').write('')
    ini = time.time()
    sat_file = os.path.abspath(f'{os.getcwd()}\\instance_files\\SAT1.txt')

    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

    initial_solution = ([False for _ in range(range_literal)], -1, -1) # Pq -1 -1
    print(tabu_search(initial_solution, clauses))
    end = time.time()
    print(f'time: {end - ini}')

main()
