from scipy.optimize import fsolve

def jacobian_exercise(x,y):
    return [[1, -1, 1],
            [2*x, 2*y]]

def func(x):
    out = [x[0] - x[1] + 1]
    out.append(x[0]**2 + x[1]**2 - 4)
    return out
# sol = fsolve(function_exercise, [1,1], fprime=jacobian_exercise, full_output=1)
# print('solution exercice fsolve:', sol)
def func2(x):
    out = [x[0] * (x[1]) - 4]
    out.append(x[1] * x[0] - x[1] - 5)
    return out
x = [1,1]
x02 = fsolve(func, x)

print(x02)