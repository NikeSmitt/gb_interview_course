# Реализовать возможность переустановки значения цены товара в родительском классе. Проверить, распечатать информацию
# о товаре.


class ItemDiscount:
    
    def __init__(self):
        self._title = 'Валенки'
        self._price = 1990
    
    def get_title(self):
        return self._title
    
    def get_price(self):
        return self._price
    
    def set_price(self, new_price):
        if new_price < 0:
            raise ValueError('Цена должна быть больше 0.')
        self._price = new_price


class ItemDiscountReport(ItemDiscount):
    
    def set_new_price(self, value):
        super().set_price(value)
    
    def get_parent_data(self):
        print(f'{super().get_title()} {super().get_price()}')


if __name__ == '__main__':
    item = ItemDiscount()
    item_report = ItemDiscountReport()

    item_report.get_parent_data()
    item_report.set_price(999)
    item_report.get_parent_data()
