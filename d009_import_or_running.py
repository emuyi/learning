# todo 正确理解导入时和运行时
'''
import 导入，python run.py 执行
import 首次导入，加载py文件，并编译成pyc文件，如果再次导入，如果pycache中有最新的缓存，不会重新加载，会直接导入缓存
但，无论是导入时还是运行时，解释器都是由上至下执行
1、在没有 __name__==__main__ 限制的时候，导入和执行其实一样
2、导入模块，如果有显示调用的函数，如print() 是会算的

3、导入模块，对于函数，只是记录了函数名，对函数体进行编译，解释器并未执行函数体，但是，对于类，则不是
解释器会运行 类体，记录类的属性和方法。被装饰器修饰的类会先加载，装饰器再被加载，要不装饰器装饰谁去。
4、类装饰器只是对装饰的类有效，他的子类有的时候可能会继承这个特性，也可能不会继承，具体要看子类要怎么定义，
class_four 的 method_y 的重新定义并未继承父类，所以没有触发装饰器，如果要使用 super 调用下父类，装饰器就会被触发
'''

from d009_evalsupport import deco_alpha   # 会全部加载一遍

print('<[1]> evaltime module start')


class ClassOne:

    print('<[2]> ClassOne body')

    def __init__(self):
        print('<[3]> ClassOne.__init__')

    def __del__(self):
        print('<[4]> ClassOne.__del__')

    def method_x(self):
        print('<[5]> ClassOne.method_x')

    class ClassTwo(object):
        print('<[6]> ClassTwo body')


@deco_alpha
class ClassThree:
    print('<[7]> ClassThree body')

    def method_y(self):
        print('<[8]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[9]> ClassFour body')

    def method_y(self):
        # print('<[10]> ClassFour.method_y')
        super().method_y()  # 如果调用父类方法，类装饰器可用


if __name__ == '__main__':
    print('<[11]> ClassOne tests', 30 * '.')
    one = ClassOne()
    one.method_x()
    print('<[12]> ClassThree tests', 30 * '.')
    three = ClassThree()
    three.method_y()
    print('<[13]> ClassFour tests', 30 * '.')
    four = ClassFour()
    four.method_y()
print('<[14]> evaltime module end')