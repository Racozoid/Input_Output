try:
    number_one = float(input('Введите первое число: '))
    number_two = float(input('Введите второе число: '))
    #Ввод чисел
    
except ValueError:

    """Если введен текст, то программа вместо ошибки выдаст,
    что введены некорректные данные"""

    print('\nВведены некорректные данные')
    input('Press ENTER to exit')
    
else:
    Sum = number_one + number_two   #Сумма
    Diff = number_one - number_two  #Разность
    Ave = (abs(number_one) + abs(number_two)) / 2   #Среднее арифмитическое

    print('\nСумма этих чисел равна {0}\nРазность этих чисел равна {1}\n'
          'Среднее арифмитическое этих чисел равно {2}'.format(Sum, Diff, Ave))
    #Вывод
    input('Press ENTER to exit')
