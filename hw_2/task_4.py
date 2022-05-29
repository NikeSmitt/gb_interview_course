# Реализовать расчет цены товара со скидкой. Величина скидки должна передаваться в качестве аргумента в дочерний
# класс. Выполнить перегрузку методов конструктора дочернего класса (метод __init__, в который должна передаваться
# переменная — скидка), и перегрузку метода __str__ дочернего класса. В этом методе должна пересчитываться цена и
# возвращаться результат — цена товара со скидкой. Чтобы все работало корректно, не забудьте инициализировать
# дочерний и родительский классы (вторая и третья строка после объявления дочернего класса).


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
    
    def __init__(self, discount):
        super().__init__()
        self.discount = discount
    
    def set_new_price(self, value):
        super().set_price(value)
    
    def get_parent_data(self):
        print(f'{super().get_title()} {super().get_price()}')
        
    def __str__(self):
        discount_price = super().get_price() - (super().get_price() * self.discount)
        return f'{discount_price:.2f}'


if __name__ == '__main__':
    item_report = ItemDiscountReport(0.13)
    print(item_report)
    