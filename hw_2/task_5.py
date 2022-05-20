# Проверить на практике возможности полиморфизма. Необходимо разделить дочерний класс ItemDiscountReport на два
# класса. Инициализировать классы необязательно. Внутри каждого поместить функцию get_info, которая в первом классе
# будет отвечать за вывод названия товара, а вторая — его цены. Далее реализовать вызов каждой из функции get_info.
from abc import ABC, abstractmethod


class ItemGetInfo(ABC):
    @abstractmethod
    def get_info(self):
        pass


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


class ItemDiscountReportPrice(ItemDiscount, ItemGetInfo):
    
    def get_info(self):
        print(super().get_price())


class ItemDiscountReportTitle(ItemDiscount, ItemGetInfo):
    
    def get_info(self):
        print(super().get_title())
        
        
class ItemDataReporter:
    
    @classmethod
    def report_info(cls, report: ItemGetInfo):
        report.get_info()


if __name__ == '__main__':
    
    ItemDataReporter.report_info(ItemDiscountReportTitle())
    ItemDataReporter.report_info(ItemDiscountReportPrice())
