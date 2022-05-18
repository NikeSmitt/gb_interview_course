# Реализовать функцию print_directory_contents(path). Функция принимает имя директории и выводит ее содержимое,
# включая содержимое всех поддиректории (рекурсивно вызывая саму себя). Использовать os.walk нельзя,
# но можно использовать os.listdir и os.path.isfile
import os


def print_directory_contents(path):
    for name in os.listdir(path):
        inner_path = os.path.join(path, name)
        if os.path.isfile(inner_path):
            print(name)
        else:
            print(f'###### {inner_path} #######')
            print_directory_contents(inner_path)
            
    