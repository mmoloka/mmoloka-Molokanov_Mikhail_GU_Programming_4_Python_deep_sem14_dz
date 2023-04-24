# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях.
# Напишите к ним тесты. 2-5 тестов на задачу в трёх вариантах:
# ○ doctest,
# ○ unittest,
# ○ pytest.

def quadratic_equation(a: int, b: int, c: int):
    d = b ** 2 - 4 * a * c
    if d == 0:
        return -b / (2 * a)
    elif d > 0:
        return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
    else:
        raise ValueError('Действительных корней нет')
    
if __name__ == '__main__':
    print(quadratic_equation(-4, 28, -49))  
    print(quadratic_equation(-6, 0, 54))
    print(quadratic_equation(3, -4, 94)) 