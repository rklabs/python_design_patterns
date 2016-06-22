# This is an example of Strategy desgin pattern
# Works with both Python2.x and Python3.x
import six
from collections import namedtuple

if six.PY2:
    from abc import ABCMeta, abstractmethod
    MetaClass = ABCMeta
elif six.PY3:
    from abc import ABC, abstractmethod
    MetaClass = ABC

Customer = namedtuple('Customer', 'name fidelity')


class LineItem(object):

    def __init__(self, product, quantity, price):
        self._product = product
        self._quantity = quantity
        self._price = price

    def total(self):
        return self._quantity * self._price


class Order(object):

    def __init__(self, customer, cart, promotion=None):
        self._customer = customer
        self._cart = list(cart)
        self._promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self._cart)
        return self.__total

    def due(self):
        if self._promotion is None:
            discount = 0
        else:
            discount = self._promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())

if six.PY3:
    class Promotion(MetaClass):

        @abstractmethod
        def discount(self, order):
            pass
elif six.PY2:
    class Promotion():
        __metaclass__ = MetaClass

        @abstractmethod
        def discount(self, order):
            pass


class FidelityPromo(Promotion):

    def discount(self, order):
        return order.total() * 0.05 if order._customer.fidelity >= 1000 else 0


class BulkItemPromo(Promotion):

    def discount(self, order):
        discount = 0
        for item in order._cart:
            if item._quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):

    def discount(self, order):
        distinct_items = {item._product for item in order._cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


joe = Customer('John Doe', 0)
ann = Customer('Ann Smith', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermellon', 5, 5.0)]

print(Order(joe, cart, FidelityPromo()))
print(Order(ann, cart, FidelityPromo()))

banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
print(Order(joe, banana_cart, BulkItemPromo()))

long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]
print(Order(joe, long_order, LargeOrderPromo()))
print(Order(joe, cart, LargeOrderPromo()))
