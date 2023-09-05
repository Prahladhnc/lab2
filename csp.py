!pip install python-constraint
from constraint import *


problem = Problem()

# Define the variables and their domains
problem.addVariable('A', range(1, 11))  # A can be 1 to 10
problem.addVariable('B', range(1, 11))  # B can be 1 to 10
problem.addVariable('C', range(1, 11))  # C can be 1 to 10

# Define the constraints
def constraint_func(A, B, C):
    if A + B == C and A * B == 12 and A - B == 4:
        return True
    return False

problem.addConstraint(constraint_func, ('A', 'B', 'C'))

# Find the solutions
solutions = problem.getSolutions()

# Print the solutions
for solution in solutions:
    print(f'A: {solution["A"]}, B: {solution["B"]}, C: {solution["C"]}')
