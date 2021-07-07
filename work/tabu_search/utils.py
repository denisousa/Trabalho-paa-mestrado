from configuration import tabu_size


def update_tabu(queue, value):
    global tabu_size
    if len(queue) >= tabu_size:
        queue.pop(0)
    queue.append(sorted(value))
    return queue


def aspiration(best_value, current_value):
    if best_value > current_value:
        return True
    return False


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


def generate_sample(n, solution):
    solution