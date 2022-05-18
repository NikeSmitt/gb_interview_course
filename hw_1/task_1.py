# Вывести таблицу умножения в виде.
# 1 x 1 = 1
# 1 x 2 = 2
# ..
# 1 x 10 = 10
# —
# 2 x 1 = 2
# 2 x 2 = 4
# …
# N x 10 = 10N
#
# Параметр N задается с клавиатуры(или в виде аргумента скрипта, по желанию)
# Между разделами вывести разделитель в виде 5 дефисов

import sys


def task_1(n: int) -> str:
    if n < 1:
        raise ValueError('Введите значение от 1 до 100')
    output = []
    
    for i in range(1, n + 1):
        for j in range(1, 11):
            output.append(f'{i} x {j} = {i * j}')
        output.append('-----')
    output.pop()
    return '\n'.join(output)


if __name__ == '__main__':
    try:
        input_value = int(sys.argv[1])
    except (ValueError, IndexError) as e:
        print(e)
        exit(1)
    
    else:
        
        print(task_1(input_value))
