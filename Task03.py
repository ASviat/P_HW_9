# Задание 3.

# Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.

# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
# список только числами.

# Класс-исключение должен контролировать типы данных элементов списка.

class My_Exeption(Exception):

    def __init__(self, text):
        self.text = text


my_list = []

for i in range(0, 5):

    try:
        number = input('Введите число: ')
        if number.isdigit() != True:
            raise My_Exeption('Только числа!')
    except My_Exeption as me:
        print(me)
    else:
        my_list.append(number)

print(my_list)
