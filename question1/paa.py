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

# def assignment(literals, clauses):
#     true_clauses = 0
#     for clause in clauses:
#         l1 = (
#             literals[abs(clause[0]) - 1]
#             if clause[0] > 0
#             else not literals[abs(clause[0]) - 1]
#         )
#         l2 = (
#             literals[abs(clause[1]) - 1]
#             if clause[1] > 0
#             else not literals[abs(clause[1]) - 1]
#         )
#         l3 = (
#             literals[abs(clause[2]) - 1]
#             if clause[2] > 0
#             else not literals[abs(clause[2]) - 1]
#         )
#         r = l1 or l2 or l3
#         if r:
#             true_clauses += 1
#     return true_clauses

def main():
    sat_files = ["C:\\Users\\adril\\Desktop\\Mestrado\\PAA\\Códigos\\Trabalho-paa-mestrado\\instance_files\\q4.txt"]
    for sat in sat_files:
        dataset = open(sat).readlines()
        range_literal, range_clause = list(
            map(int, dataset[0].replace(" \n", "").split(" "))
        )
        clauses = []

        for line in dataset[1 : range_clause + 1]:
            clauses.append(list(map(int, line.replace(" \n", "").split(" "))))

        literals_input = [True, False, False, False, True, False]
        # literals_input = [
        #     True if num == "1" else False for num in dataset[-1].replace("\n", "")
        # ]

        print(f"---------- {sat} ----------")
        print(f"n = {range_literal} and m = {range_clause}")
        print("Number of true clauses for: ")
        # print(f"\tNull Vector: {assignment(literals_false, clauses)}")
        print(f"\tGiven Vector: {assignment(literals_input, clauses)} \n")


main()
