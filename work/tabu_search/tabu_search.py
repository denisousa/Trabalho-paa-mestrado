import time
import copy
from configuration import sat_file, nmax
from neighborhood import generate_diversification, generate_neighborhood
from utils import update_tabu, aspiration, assignment
from random import choice


def tabu_search(initial_solution, clauses, range_literal):
    global nmax
    current_solution = copy.deepcopy(initial_solution)
    current_value = assignment(current_solution[0], clauses)
    tabu_queue = []
    count = 1
    count_repetitive_solution = 0
    previous_value = 0
    M = 1

    while (count - M) < nmax:
    # while 100:
        neighborhood = (
            generate_neighborhood(current_solution, range_literal)
            if count_repetitive_solution < 50
            else generate_diversification(current_solution, range_literal)
        )
        neighborhood_values = [
            assignment(neighborhood[i][0], clauses) for i in range(len(neighborhood))
        ]
        max_index = neighborhood_values.index(
            max(neighborhood_values)
        )  # Index do melhor vizinho
        best_solution = neighborhood[max_index]
        if (max(neighborhood_values)) == len(clauses):
            current_solution = best_solution
            previous_value = current_value
            current_value = max(neighborhood_values)
            break

        while True:
            # check if all elements have been visited
            open("log.txt", "a").write(
                f"count: {count} | max_neighborhood_values: {max(neighborhood_values)} \n"
            )
            if sorted(best_solution[1:3]) in tabu_queue:
                ## TODO: change logic for accept
                if aspiration(max(neighborhood_values), current_value):
                    current_solution = best_solution
                    previous_value = current_value
                    current_value = max(neighborhood_values)
                    M = count
                    break
                else:
                    neighborhood_values[max_index] = 0
                    max_index = neighborhood_values.index(max(neighborhood_values))
                    best_solution = neighborhood[max_index]
            else:
                current_solution = best_solution
                previous_value = current_value
                current_value = max(neighborhood_values)
                tabu_queue = update_tabu(tabu_queue, best_solution[1:3])
                M = count
                break

        if current_value == previous_value:
            count_repetitive_solution += 1
        else:
            count_repetitive_solution = 0
        count += 1

    return current_solution[0], current_value


def main():
    open("log.txt", "w").write("")
    ini = time.time()
    dataset = open(sat_file).readlines()
    range_literal, range_clause = list(
        map(int, dataset[0].replace(" \n", "").split(" "))
    )
    clauses = []

    for line in dataset[1 : range_clause + 1]:
        clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

    initial_solution = ([choice([True, False]) for _ in range(range_literal)], -1, -1)
    print(tabu_search(initial_solution, clauses, range_literal))
    end = time.time()
    print(f"time: {end - ini}")


main()
