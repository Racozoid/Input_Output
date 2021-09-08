try:
    number_one = float(input('Введите первое число: '))
    number_two = float(input('Введите второе число: '))
    # Ввод чисел
    
except ValueError:

    # Если введен текст, то программа вместо ошибки выдаст,
    # что введены некорректные данные

    print('\nВведены некорректные данные')
    input('Press ENTER to exit')
    
else:
    Sum = number_one + number_two   # Сумма
    Diff = number_one - number_two  # Разность
    Ave = (abs(number_one) + abs(number_two)) / 2   # Среднее арифмитическое
    Prod = number_one * number_two  # Произведенеие
    Quot = number_one / number_two  # Частное

    print('\nСумма этих чисел равна {}\n'
          'Разность этих чисел равна {}\n'
          'Среднее арифмитическое этих чисел равно {}\n'
          'Произведение этих чисел равно {}\n'
          'Частное от деления этич чисел равно {}'.format(Sum, Diff, Ave, Prod, Quot))
    # Вывод
    input('Press ENTER to exit')
