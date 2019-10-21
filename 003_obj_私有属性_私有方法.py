class User:

    def __init__(self, name, pwd):
        self.name = name
        self.__pwd = pwd


    def get_pwd(self):
        print(self.__dict__)  # 为什么可以，无论是外部存放属性的时候，都是基于，_类名__属性名 : value 这样的方式存储的。
        return self.__pwd


ellen = User('ellen', '123')
# print(ellen.__dict__)
# print(ellen.get_pwd())
# 私有属性，方法 只是为了确保外部无法调用部分的属性和方法，内部可以来回的调用, 且不能继承

#  私有属性，方法 和 property 搭配使用


class Goods:
    __discount = 0.5

    def __init__(self, name, price):
        self.name = name
        self.__price = price

    @property
    def price(self):
        return self.__price * self.__discount

    @price.setter
    def price(self, num):
        self.__price = num

    @price.deleter
    def price(self):
        del self.__price


banana = Goods('banana', 10)
# print(banana.price)

banana.price = 20
print(banana.price)

del banana.price

print(banana.price)