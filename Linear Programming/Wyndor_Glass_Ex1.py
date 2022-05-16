# REFERENCE Book : F. Hillier, Lieberman
# INTRODUCTION TO OPERATIONS RESEARCH, 10th Ed.
# Wyndor Glass Co exemple


"""Linear Optimaization exemple."""


# [START program]

# Step1: import OR-Tools for lP
from ortools.linear_solver import pywraplp


def Wyndor_Example():

    # Step2 : Declare a Solver
    # Create a Linear solver with the GLOP Backend
    solver = pywraplp.Solver.CreateSolver('GLOP')

    # Step3 : Declare Variables
    # x1 => x, x2 => y
    x = solver.NumVar(0, solver.infinity(), 'x')
    y = solver.NumVar(0, solver.infinity(), 'y')

    # Step4 : Define the Constraints and print them
    solver.Add(x <= 4)
    solver.Add(2*y <= 12)
    solver.Add(3*x + 5*y <= 18)

    print('Number of constraints = ', solver.NumConstraints())

    # Step5 : Define the Objective function Z
    solver.Maximize(3*x + 5*y)

    # Step6 : Invoke the Solver
    status = solver.Solve()

    # Step7 : Display the results
    if status == pywraplp.Solver.OPTIMAL:
        print('Solution :')
        print('Objective value = ', solver.Objective().Value())
        print('x =', x.solution_value())
        print('y =', y.solution_value())

    else:
        print('The problem does not have an optimal solution.')

    # Advanced Usage
    print('\nAvanced Usage')
    print('Problem solved in %f milliseconds' % solver.wall_time())
    print('Problem solved in %d iteractions' % solver.iterations())


Wyndor_Example()
# [END program]
