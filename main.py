try:
    number_one = float(input('Введите первое число: '))
    number_two = float(input('Введите второе число: '))

except ValueError:
    print('\nВведены некорректные данные')
    input('Press ENTER to exit')

else:
    number_one = float(number_one)
    number_two = float(number_two)
    Sum = number_one + number_two
    Diff = number_one - number_two
    Ave = (abs(number_one) + abs(number_two)) / 2

    print('\nСумма этих чисел равна {0}\nРазность этих чисел равна {1}\n'
          'Среднее арифмитическое этих чисел равно {2}'.format(Sum, Diff, Ave))
    input('Press ENTER to exit')
