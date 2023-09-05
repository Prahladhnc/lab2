def negate_clause(clause):
    negated_clause=[]
    for literal in clause:
        if literal.startswith('~'):
            negated_clause.append(literal[1:])  
        else:
            negated_clause.append('~' + literal)
    return negated_clause

def resolution(clause1, clause2):
    for literal in clause1:
        if literal in negate_clause(clause2):
            complementary_literal = negate_clause([literal])[0]
            new_clause = [l for l in (clause1 + clause2) if l != literal and l != complementary_literal]
            return new_clause
    return None  

    

clause1 = ['A', 'B']
clause2 = ['~A', 'C']

resolvent = resolution(clause1, clause2)
if resolvent:
    print("Resolvent:", resolvent)
else:
    print("No resolvent found.")
