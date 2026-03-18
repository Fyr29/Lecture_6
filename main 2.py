while True:
    user_second = input('Введите секунды числом: ')

    if user_second == "":
        user_second = int(0)
        break

    if user_second.isdigit():
        user_second = int(user_second)
        break

    else:
        print('Вы ввели не верные данные')
        continue

day = user_second // 86400
hour =  user_second % 86400 // 3600
minute = user_second % 86400 % 3600 // 60
second = user_second % 60

print(f'{day} дней {hour:02}:{minute:02}:{second:02}')