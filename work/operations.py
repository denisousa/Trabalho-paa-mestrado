def assignment(literals, clauses):
    true_clauses = 0
    for clause in clauses:
        l1 = literals[abs(clause[0])-1] if clause[0] > 0 else not literals[abs(clause[0])-1]
        l2 = literals[abs(clause[1])-1] if clause[1] > 0 else not literals[abs(clause[1])-1]
        l3 = literals[abs(clause[2])-1] if clause[2] > 0 else not literals[abs(clause[2])-1]
        r = l1 and l2 and l3 
        if r: 
            true_clauses += 1
    return true_clauses
