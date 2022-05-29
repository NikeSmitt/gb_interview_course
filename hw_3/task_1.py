# Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него. При вызове
# функции в качестве аргумента должно передаваться путь и имя файла с расширением. В функции необходимо реализовать
# поиск имени файла (с расширением), а затем «выделение» имени файла (без расширения). Расширений может быть
# несколько (например testfile.tar.gz).
import os.path
import sys


def get_file_name(file_path: str, file_name: str) -> str:
    full_file_path = os.path.join(file_path, file_name)
    if not os.path.isfile(full_file_path):
        return ''
    
    file_name = os.path.basename(full_file_path)
    return file_name.split('.')[0]


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print(get_file_name(sys.argv[1], sys.argv[2]))
    else:
        print('Введите путь и имя файла')
    