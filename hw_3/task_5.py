# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке часть строковых значений (
# выбирается случайно) заменить на значения типа 345example (в обратном порядке, число и строка). Реализовать функцию
# поиска определенных подстрок в файле по следующим условиям: вывод первого вхождения, вывод всех вхождений.
# Реализовать функцию замену всех найденных подстрок на новое значение и вывод измененных строк.

import os.path
import random
import argparse


def main():
    parser = argparse.ArgumentParser(description='Генерация и поиск')
    parser.add_argument('file_path', type=str, help='Путь к файлу')
    parser.add_argument('-f', '--find', type=str, help='Поиск в файле первое вхождение')
    parser.add_argument('-fa', '--find_all', type=str, help='Поиск в файле все вхождения')
    parser.add_argument('-r', '--replace', type=str, help='Замена найденных подстрок', nargs=2)
    args = parser.parse_args()
    file_path = args.file_path
    
    if not any([args.find, args.find_all, args.replace]):
        f_1(file_path)
        
    elif args.find:
        print(find(file_path, args.find))
    elif args.find_all:
        print(find(file_path, args.find_all, True))
    elif args.replace:
        replace(file_path, args.replace[0], args.replace[1])
        


def f_1(file_path):
    
    if os.path.exists(file_path):
        print('Такой файл уже существует')
        return
    
    count = 10
    texts = ['data' for _ in range(count)]
    numbers = [random.randint(100, 200) for _ in range(count)]
    data_to_save = []
    for text, num in zip(texts, numbers):
        if random.randint(0, 1):
            data_to_save.append(f'{text}{num}')
        else:
            data_to_save.append(f'{num}{text}')
    
    save_data(file_path, data_to_save)
    print_data(read_file(file_path))


def save_data(file_path, data: list):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines('\n'.join(data))


def print_data(data):
    print('\n'.join(data))


def read_file(file_path) -> list:
    if not os.path.exists(file_path):
        raise FileExistsError('Такого файла не существует')
    try:
        with open(file_path, encoding='utf-8') as f:
            return f.read().split('\n')
    except FileNotFoundError as e:
        print(e)


def find(file_path, target, find_all=False):
    data = read_file(file_path)
    
    output = []
    if find_all:
        for i, sub_str in enumerate(data):
            if sub_str == target:
                output.append(i)
    else:
        try:
            output.append(data.index(target))
        except ValueError:
            pass
    return output


def replace(file_path, target, target_replace):
    found = find(file_path, target, True)
    file_data = read_file(file_path)
    for i in found:
        file_data[i] = target_replace
    save_data(file_path, file_data)
    print(found)
    print_data(read_file(file_path))


if __name__ == '__main__':
    main()
