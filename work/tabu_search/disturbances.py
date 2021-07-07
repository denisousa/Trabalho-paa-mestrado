import random
import time
import copy


def disturb_solution(solution): # REFATOR
    solution_copy = copy.deepcopy(solution[0])
    random.seed(time.time())
    index1, index2 = sorted(random.sample(range(0, len(solution[0])), k=2)) # FIX
    solution_copy[index1] = not solution_copy[index1]
    solution_copy[index2] = not solution_copy[index2]
    return solution_copy, index1, index2

def disturb_solution_sample(solution, n):
    solution_copy = copy.deepcopy(solution[0])
    random.seed(time.time())
    indexes = sorted(random.sample(range(0, len(solution[0])), k=n))
    for index in indexes:
        solution_copy[index] = not solution_copy[index]
    return solution_copy, indexes

def disturb_solution_diversed(solution): # REFATOR
    solution_copy = copy.deepcopy(solution[0])
    random.seed(time.time())
    index1, index2, index3, index4 = sorted(random.sample(range(0, len(solution[0])), k=4)) # FIX
    solution_copy[index1] = not solution_copy[index1]
    solution_copy[index2] = not solution_copy[index2]
    solution_copy[index3] = not solution_copy[index3]
    solution_copy[index4] = not solution_copy[index4]
    return solution_copy, index1, index2, index3, index4