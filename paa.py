# Conseguir as devidas atribuições, que gerem o máixmo de cláusulas verdadeiras
# (x ^ ~y ^ z) || (~x ^ y ^ z)
from operations import assignment

sat_files = ['SAT1.txt', 'SAT2.txt', 'SAT3.txt']
for sat in sat_files:
    dataset = open(sat).readlines()
    range_literal, range_clause = list(map(int, dataset[0].replace(' \n', '').split(' ')))
    clauses = []

    for line in dataset[1:range_clause+1]:
        clauses.append(list(map(int, line.replace(' \n', '').split(' '))))

    literals_false = [False for i in range(range_clause)]
    literals_input = [True if num == '1' else False for num in dataset[-1].replace('\n', '')]

    print(sat)
    print(f'literals 0: {assignment(literals_false, clauses)}')
    print(f'literals input: {assignment(literals_input, clauses)} \n')

