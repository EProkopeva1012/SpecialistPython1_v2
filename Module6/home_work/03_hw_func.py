# Даны координаты центров двух окружностей (x1; y1) (x2; y2) и и их радиусы  R1 и R2.
# Находится ли одна окружность целиком внутри другой

# TODO: your code here
def find_cerc(x1, y1, x2, y2, r1, r2):
    """
    :param x1: координата х первой точки
    :param y1: координата у1
    :param x2: координата х2
    :param y2: координата у2
    :param r1: радиус окружности 1
    :param r2: радиус окружности 2
    :return: Находится ли одна окружность целиком внутри другой
    """
    return ((x1 - x2)^2 + (y1 - y2)^2)**0.5 + r2 <= r1

res = find_cerc (10, 8, 1, 2, 30, 10)
print(res)
