# Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл. Если
# файл с таким именем уже существует, выводим соответствующее сообщение и завершаем работу. Необходимо открыть файл и
# создать два списка: с текстовой и числовой информацией. Для создания списков использовать генераторы. Применить к
# спискам функцию zip(). Результат выполнения этой функции должен быть обработан и записан в файл таким
# образом, чтобы каждая строка файла содержала текстовое и числовое значение (например example345). Вызвать вторую
# функцию. В нее должна передаваться ссылка на созданный файл. Во второй функции необходимо реализовать открытие
# файла и простой, построчный вывод содержимого.
import os.path
import random
import sys


def main():
    if len(sys.argv) > 1:
        file = sys.argv[1]
        
        if os.path.exists(file):
            print(f'Файл с именем {file} уже существует')
            return
        
        f_1(file)
        f_2(file)
    else:
        print('Введите имя файла')


def f_1(file_name='task_4.txt'):
    count = 10
    text = ['data' for _ in range(count)]
    numbers = [random.randint(100, 200) for _ in range(count)]
    data = list(zip(text, numbers))
    
    with open(file_name, 'w', encoding='utf-8') as f:
        data_to_save = list(map(lambda t: f'{t[0]}{t[1]}', data))
        f.writelines('\n'.join(data_to_save))


def f_2(file_path):
    try:
        with open(file_path, encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)


if __name__ == '__main__':
    main()
