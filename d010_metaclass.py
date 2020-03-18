# todo 元类
"""
元类是制造类的工厂。元类用来生成类。

python 内置的大部分类及用户定义的类默认情况下都是由 type 生成。也就是说
这些类是 type 的实例。不要和继承混了，object 是这些类的父类。

type 和 object 的关系比较神奇，object 是 type 的实例，type却是 object 的子类。另外，type 是自己的实例。

内置其他的元类 如 abc.ABCMeta ,  由 type 生成，具备 type 生成类的功能。collections.Iterable
就是由 ABCMeta 生成。
"""
