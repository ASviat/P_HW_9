# Задание 2.

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class My_Exeption(Exception):

    def __init__(self, text):
        self.text = text


def enter_number():
    input_data = input('Введите число, на которое будем делить: ')
    return input_data


def exept_it():

    try:
        number = int(enter_number())
        if number == 0:
            raise My_Exeption('Нельзя делить на ноль!')
    except My_Exeption as mr:
        print(mr)
    else:
        print(f'Все ОК, делим на {number}')


exept_it()



