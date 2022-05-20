# Написать программу, которая запрашивает у пользователя ввод числа. На введенное число она отвечает сообщением,
# целое оно или дробное. Если дробное — необходимо далее выполнить сравнение чисел до и после запятой. Если они
# совпадают, программа должна возвращать значение True, иначе False.


def is_float(value):
    try:
        float(value)
    except ValueError:
        return False
    return True


def main():
    user_input = input('Введите число (целое или дробное) -> ')
    if user_input.isdigit():
        print('Вы ввели целое число')
    elif is_float(user_input):
        try:
            a, b = [int(value) for value in user_input.split('.')]
            print('Вы ввели дробное число')
            print(a == b)
        except ValueError:
            print('Вы ввели некорректное дробное число')
    else:
        print('Вы ввели некорректное число. До Свидания')


if __name__ == '__main__':
    main()
