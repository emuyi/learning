# 获取当前模块
import sys
import testing

print(sys.modules[__name__])
getattr(testing, 'func')()

# python -m 执行和 python xx.py 的区别 验证下
# getattr, hasattr, setattr, delattr


class A:

    # def __str__(self):
    #     return "A's object"

    def __repr__(self):
        return str(self.__dict__)


a = A()
a.name = 'yj'
if hasattr(a, 'name'):
    print(getattr(a, 'name'))
setattr(A, 'name', 'hahaha')
delattr(a, 'name')
print(a.name)

# __str__  str(obj)或者%s字符串拼接的时候会被调用并返回自定义的结果，如果自己没有定义，则继承object的，
# 返回 对象的内存地址。

print(repr(a))
print('%r--11' % a)
print(str(a))

# __repr__ repr(obj)或者%r字符串拼接的时候会调用且返回自定义的内容，如果没有定义，同样使用object的
# 方法返回
# __repr__ 是 __str__ 的backup 也就是说如果内部没有实现__str__ 那就会走__repr__
# 以上的返回内容的自定义必须是字符串形式！！

# len(obj) 调用内部的__len__() 方法 比如bat是一家公司，len(bat)，在__len__() 返回公司人数
# del obj 调用内部的__del__() 方法， 析构方法【先调用后删除】

# obj() 调用内部的__call__()方法， 如flask的上下文管理机制


