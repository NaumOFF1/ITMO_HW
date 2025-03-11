def task_8(num_float: float):
    if num_float > 0:
        print('Положительное число')
    elif num_float == 0:
        print('Ноль')
    else:
        print('Число отрицательное')


def kurs(number_kurs: int):
    if number_kurs in range(1,5):
        print('Бакалавр')
    elif number_kurs in range(5,7):
        print('Магистр')
    elif number_kurs in range(7,10):
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

kurs(4)