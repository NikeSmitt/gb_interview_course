# Усовершенствовать программу «Банковский депозит». Третьим аргументом в функцию должна передаваться фиксированная
# ежемесячная сумма пополнения вклада. Считаем, что клиент вносит средства в последний день


def deposit(amount, period, increment=0):
    
    if amount < 1000 or period < 1:
        raise ValueError('Введены некорректные данные')
    datas = [
        (0.05, 0.06, 0.05),
        (0.06, 0.07, 0.065),
        (0.07, 0.08, 0.075),
    ]
    result = amount
    
    if 1000 <= amount < 10000:
        percents = datas[0]
    elif 10000 <= amount <= 100_000:
        percents = datas[1]
    else:
        percents = datas[2]
    
    if period <= 6:
        percent = percents[0]
    elif 7 < period <= 24:
        percent = percents[1]
    else:
        percent = percents[2]
    
    print(f'Ваш процент по вкладу = {percent * 100}%')
    
    for _ in range(period):
        result = (result * percent / 12) + result
        result += increment
    return result


if __name__ == '__main__':
    my_period = 2
    my_amount = 1000
    inc = 100
    dep = deposit(my_amount, my_period, inc)
    print(f'Ваш вклад после {my_period} месяца(ев): {dep:.2f}')
