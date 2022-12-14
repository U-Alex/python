# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

pr_list = [False, True]

for x in pr_list:
    for y in pr_list:
        for z in pr_list:
            result = not (x or y or z) == (not x and not y and not z)
            print(f'проверка ¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}  \nрезультат {result}')

