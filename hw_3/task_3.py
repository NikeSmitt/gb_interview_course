# Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
# Необходимо написать функцию, создающую из данных ключей и значений словарь. Если ключу не хватает значения,
# в словаре для него должно сохраняться значение None. Если есть значения, которым не хватило ключей, их необходимо
# отбросить.


def task_3(keys: list, values: list) -> dict:
    output = {}
    keys_copy = keys[:]
    values_copy = values[:]
    difference = len(keys) - len(values)
    if difference > 0:
        values_copy.extend([None] * difference)
    
    for key, value in zip(keys_copy, values_copy):
        output[key] = value
    
    return output


if __name__ == '__main__':
    print(task_3([1, 2, 3], ['a', 'b', 'c']))
    print(task_3([1, 2, 3], ['a', 'b']))
    print(task_3([1, 2], ['a', 'b', 'c']))
    print(task_3([1, 2], []))
    print(task_3([], ['a', 'b']))
