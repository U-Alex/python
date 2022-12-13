
num1 = int(input('num1: '))
num2 = int(input('num2: '))

if (num1 ** 2 == num2):
    print(f"{num1} - квадрат {num2}")
elif (num2 ** 2 == num1):
    print(f"{num2} - квадрат {num1}")
else:
    print('ни то, ни другое')

