from abc import ABCMeta, abstractmethod
class A(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        print('foo')

class B(A):
    def bar(self):
        print('bar')

    def foo(self):
        print(111)

# 接口类和抽象类都是一种编程规范，Python中没有接口类的概念，因为Python支持多继承，有抽象类的概念--> 对类做封装

b = B()
b.foo()

