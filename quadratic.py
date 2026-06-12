# verison 0.0.1
# Программа для решения квадратных уравнений

def solve(a, b, c):
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        return ((-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a))
    
a = int(input())
b = int(input())
c = int(input())

result = solve(a, b, c)
print(result)
