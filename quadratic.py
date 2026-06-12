# verison 1.0.1
# Программа для решения квадратных уравнений

def solution(a: float, b: float, c: float):
    """
    Решает квадратное уравнение через дискриминант.
    
    Args:
        a [float]: старший коэффициент квадратного трёхчлена.
        b [float]: коэффициент перед x в квадратном трёхчлене.
        c [float]: свободный коэффициент.

    Return:
        [None]: отсутствие корней.
        [tuple]: два корня.
        [float]: один корень.
    """

    discriminant = b ** 2 - (4 * a * c)
    if discriminant > 0:
        x_1 = (-b + discriminant ** 0.5) / (2 * a)
        x_2 = (-b - discriminant ** 0.5) / (2 * a)
        return (x_1, x_2)
    elif discriminant == 0:
        x = -b / (2 * a)
        return x
    else:
        return None
    

def output(a: float, b: float, c: float) -> str:
    """
    Улучшает отображение корней.
    
    Args:
        a [float]: старший коэффициент квадратного трёхчлена.
        b [float]: коэффициент перед x в квадратном трёхчлене.
        c [float]: свободный коэффициент.

    Return:
        str: описание результата 
    """

    result = solution(a, b, c)
    if result is None:
        return "Нет корней"
    elif isinstance(result, tuple):
        return f"Два корня: {result[0]} и {result[1]}"
    else:
        return f"Один корень: {result}"


def main() -> None:
    """
    Главная функция программы.
    """

    print("Введите коэффициенты в формате \na b c")
    coefficients = input().split()
    a, b, c =  float(coefficients[0]), float(coefficients[1]), float(coefficients[2])
    if a != 0:
        print(output(a, b, c))
    else:
        print("a не может быть равным 0")


main()
