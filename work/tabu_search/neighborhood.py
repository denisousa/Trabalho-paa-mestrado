from math import factorial
from disturbances import disturb_solution, disturb_solution_diversed


def calculate_len_of_neighbors(n):
    nv = factorial(n) / (factorial(2) * factorial(n - 2))
    if nv > 1000:
        return 1000
    return nv


def generate_neighborhood(solution, range_literal):
    nv = calculate_len_of_neighbors(range_literal)
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, index1, index2 = disturb_solution(solution)
        complete_solution = (troubled_solution, index1, index2)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

    return neighborhood


def generate_diversification(solution, range_literal):
    nv = calculate_len_of_neighbors(range_literal)
    neighborhood = []
    while len(neighborhood) < nv:
        troubled_solution, index1, index2, index3, index4 = disturb_solution_diversed(
            solution
        )
        complete_solution = (troubled_solution, index1, index2, index3, index4)
        if complete_solution not in neighborhood:
            neighborhood.append(complete_solution)

    return neighborhood
