import random
import time
import copy

nv = 3  # número de vizinhos


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


def main():
    sat_files = ["instance_files/test.txt"]
    for sat in sat_files:
        dataset = open(sat).readlines()
        range_literal, range_clause = list(
            map(int, dataset[0].replace(" \n", "").split(" "))
        )
        clauses = []

        for line in dataset[1 : range_clause + 1]:
            clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

        initial_solution = [False for i in range(range_literal)]

        print(generate_neighborhood(initial_solution))


main()
