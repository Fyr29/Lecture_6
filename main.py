import string

user_input = input('Напишите две буквы: ')
result = 'Непредвидимая ошибка'
symbol = string.punctuation + string.digits + ' '

while True:

    if any(i in user_input for i in symbol):
        for i in string.punctuation + string.digits + ' ':
            user_input = user_input.replace(i, '')

    if any(i not in string.ascii_letters for i in user_input):
        user_input = input('Вы ввели неизвестные символы\nВведите две буквы: ')
        continue

    if len(user_input) > 2:
        user_input = input('Вы ввели больше двух букв\nВведите две буквы: ')
        continue

    if len(user_input) < 2:
        user_input = input('Вы ввели меньше двух букв\nВведите две буквы: ')
        continue

    if len(user_input) == 2:
        start, stop = user_input
        start_in = string.ascii_letters.index(start)
        stop_in = string.ascii_letters.index(stop)

    if start_in <= stop_in:
        result = string.ascii_letters[start_in : stop_in + 1]
        break

    else:
        if stop_in == 0:
            stop_in += 1
            result = string.ascii_letters[start_in : stop_in - 1: -1] + 'a'
            break

        else:
            result = string.ascii_letters[start_in: stop_in - 1: -1]
            break

print(f'Ваши буквы: {start} - {stop}\n{result}')