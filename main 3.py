import math

numbers = input('Введите любое число: ')

while not numbers.isdigit():
    numbers = input('Это не число\nВведите любое число: ')

while len(numbers) > 1:
    spisok = [int(i) for i in numbers]
    result = math.prod(spisok)
    print(f'{'*'.join(numbers)} = {result}')
    numbers = str(result)

print()
print(f'Итог: {numbers}')