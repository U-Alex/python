"""Нахождение корней квадратного уравнения"""

import math
from decorators import multi_quad, save_result


@save_result(filename='result.json')
@multi_quad(rows_count=20)
def quad_eq(a: float, b: float, c: float) -> list:
    discr = float(b ** 2 - 4 * a * c)
    if discr < 0 or a == 0:
        return []
    elif discr == 0:
        return [-b / (2 * a)]
    else:
        return [(-b + math.sqrt(discr)) / (2 * a),
                (-b - math.sqrt(discr)) / (2 * a)]


if __name__ == '__main__':
    print(quad_eq(2.2, 8, 2.2))
    print(quad_eq(2, 4, 2))
    print(quad_eq(10, 4, 2))
