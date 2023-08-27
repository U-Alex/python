""" Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
    Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
    Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
    Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.
"""

def user_input():
    ok = False
    while not ok:
        try:
            nums = input('Введите длины сторон треугольника a, b, c (через запятую): ').split(',')
            if len(nums) == 3:
                result = [int(item) for item in nums]
                if result[0] > 0 and result[1] > 0 and result[2] > 0:
                    ok = True
                else:
                    raise Exception("отрицательные числа или 0")

        except Exception as error :
            print(error)
    return result

a, b, c = user_input()

if (a + b <= c) or (b + c <= a) or (c + a <= b):
    result = "не существует!"
elif (a == b) and (b == c):
    result = "равносторонний"
elif a == b or b == c or c == a:
    result = "равнобедренный"
else:
    result = "разносторонний"

print(f"треугольник со сторонами: {a}, {b}, {c} - {result} ")

