# Инкапсулировать оба параметра (название и цену) товара родительского класса. Убедиться, что при сохранении текущей
# логики работы программы будет сгенерирована ошибка выполнения. Усовершенствовать родительский класс таким образом,
# чтобы получить доступ к защищенным переменным. Результат выполнения заданий 1 и 2 должен быть идентичным.


class ItemDiscount:
    
    def __init__(self):
        self._title = 'Валенки'
        self._price = 1990
        
    def get_title(self):
        return self._title
    
    def get_price(self):
        return self._price


class ItemDiscountReport(ItemDiscount):
    
    def get_parent_data(self):
        print(f'{super().get_title()} {super().get_price()}')


if __name__ == '__main__':
    item = ItemDiscount()
    item_report = ItemDiscountReport()
    item_report.get_parent_data()
    