# todo 元类
import abc
"""
元类是制造类的工厂。元类用来生成类。

python 内置的大部分类及用户定义的类默认情况下都是由 type 生成。也就是说
这些类是 type 的实例。不要和继承混了，object 是这些类的父类。

type 和 object 的关系比较神奇，object 是 type 的实例，type却是 object 的子类。另外，type 是自己的实例。

内置其他的元类 如 abc.ABCMeta ,  由 type 生成，具备 type 生成类的功能。collections.Iterable
就是由 ABCMeta 生成。
"""


# 基于元类 及 描述符的 字段校验功能
class Validation:

    def __set__(self, instance, value):
        value = self.validate(instance, value)
        instance.__dict__[self.storage_name] = value

    @abc.abstractmethod
    def validate(self, instance, value):
        pass


class Quantity(Validation):

    def validate(self, instance, value):
        if value <= 0:
            raise ValueError('value must be > 0')
        return value


class NonBlank(Validation):

    def validate(self, instance, value):
        value = value.strip()
        if len(value) == 0:
            raise ValueError('value must not be blank')
        return value


class GoodMeta(type):

    def __new__(mcs, name, bases, attrs):
        for key, attr in attrs.items():
            if isinstance(attr, Validation):
                attr.storage_name = key
        return super().__new__(mcs, name, bases, attrs)


class FruitVeg(metaclass=GoodMeta):
    pass


class Fruit(FruitVeg):

    name = NonBlank()
    price = Quantity()
    weight = Quantity()

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def total(self):
        return self.price * self.weight


# banana = Fruit('banana', 10, 3)
# banana.name = ''
# todo 类的常用方法
"""
cls.mro(): 返回类继承顺序列表
cls.__bases__: 返回直接父类组成的元组
cls.__subclasses(): 返回直接子类组成的列表
"""


class A:
    pass


class B(A):
    pass


class C(B):
    pass


class D(C, B, A):
    pass


print(D.__bases__)
print(C.__bases__)
print(A.__subclasses__())
