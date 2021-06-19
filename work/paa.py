from random import randint

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
        r = l1 or l2 or l3
        if r:
            true_clauses += 1
    return true_clauses


def main():
    sat_files = ["SAT1.txt"]
    for sat in sat_files:
        dataset = open(sat).readlines()
        range_literal, range_clause = list(
            map(int, dataset[0].replace(" \n", "").split(" "))
        )
        clauses = []

        for line in dataset[1 : range_clause + 1]:
            clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

        literals = [True if randint(0, 10) % 2 == 0 else False for i in range(range_literal)]
        literals_input = [
            True if num == "1" else False for num in dataset[-1].replace("\n", "")
        ]
        # import ipdb; ipdb.set_trace()
        print(f"---------- {sat} ----------")
        print(f"n = {range_literal} and m = {range_clause}")
        print("Number of true clauses for: ")
        print(f"\tNull Vector: {assignment(literals, clauses)}")
        print(f"\tGiven Vector: {assignment(literals_input, clauses)} \n")

        tabu_list = []
        list_len = 100

def suction():
    pass

main()
