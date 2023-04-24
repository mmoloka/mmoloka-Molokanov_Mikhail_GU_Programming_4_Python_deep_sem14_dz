import doctest

def quadratic_equation(a: int, b: int, c: int):
    """
    >>> quadratic_equation(-4, 28, -49)
    3.5
    >>> quadratic_equation(-6, 0, 54)
    (-3.0, 3.0)
    >>> quadratic_equation(3, -4, 94)
    Traceback (most recent call last):
    ...
    ValueError: Действительных корней нет
    """
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        raise ValueError('Действительных корней нет')
    
if __name__ == '__main__':
    doctest.testmod(verbose=True)
