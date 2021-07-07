from random import randint


def assignment(literals, clauses):
    true_clauses = 0
    for clause in clauses:
        literals_result = [
            literals[abs(clause_value) - 1]
            if clause_value > 0
            else not literals[abs(clause_value) - 1]
            for clause_value in clause
        ]
        if True in literals_result:
            true_clauses += 1
    return true_clauses


sat = "C:\\Users\\adril\\Desktop\\Mestrado\\PAA\\Códigos\\Trabalho-paa-mestrado\\instance_files\\q4.txt" # Drica
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
print(f"---------- {sat} ----------")
print(f"n = {range_literal} and m = {range_clause}")
print("Number of true clauses for: ")
print(f"\tNull Vector: {assignment(literals, clauses)}")
print(f"\tGiven Vector: {assignment(literals_input, clauses)} \n")