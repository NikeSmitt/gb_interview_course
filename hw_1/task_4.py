# Написать программу «Банковский депозит».
# Клиент банка делает депозит на определенный срок.
#
# В зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 и более года — 5 % годовых).
# 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых, 2 и более года – 6.5 % годовых).
# 100000–1000000 руб (6 месяцев — 7 % годовых, год — 8 % годовых, 2 и более года — 7.5 % годовых).


def deposit(amount, period):
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
    return result


if __name__ == '__main__':
    
    period = 2
    amount = 1000
    dep = deposit(amount, period)
    print(f'Ваш вклад после {period} месяца(ев): {dep:.2f}')