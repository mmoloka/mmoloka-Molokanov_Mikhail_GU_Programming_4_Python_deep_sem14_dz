from quadratic_equation import quadratic_equation
import pytest


def test_1():
        assert quadratic_equation(-4, 28, -49) == 3.5

def test_2():
    assert quadratic_equation(-6, 0, 54) == (-3.0, 3.0)

def test_3():
    with pytest.raises( ValueError, match='Действительных корней нет'):
         quadratic_equation(3, -4, 94)

if __name__ == '__main__':
 pytest.main(['-v'])         