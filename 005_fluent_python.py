"""序列"""
"""特性： 切片"""

# 切片赋值
l = list(range(10))
l[2:5] = [20, 30]
# l >> [0, 1, 20, 30, 5, 6, 7, 8, 9]
l[3:6] = [100]
# l >> [0, 1, 20, 100, 7, 8, 9]

"""特性： 序列拼接"""
# 拼接 +
# 重复并拼接 ×

# 如果想初始化一个嵌套列表，可以考虑列表推导式
lst = [['_'] * 3 for i in range(3)]
weird_board = [['_'] * 3] * 3  # 但是这样是有问题的，比如你修改下两个列表的[2][1]的值试下
# >> lst : [['_', '_', '_'], ['_', '_', '_'], ['_', 'X', '_']]
# >> weird_board: [['_', 'X', '_'], ['_', 'X', '_'], ['_', 'X', '_']]

# 区别在哪里?
'''
# lst 的生成方式相当与 
lst = []
for i in range(3):
    lst.append(['_'] * 3)
# weird_board 的生成方式
weird_board = []
row = ['_'] * 3
for i in range(3):
    weird_board.append(row)
等于说append的是同一个对象
'''

"""特性： 序列的增量赋值"""
# += 、×= ...
# += 实际是调用了__iadd__方法， 如果对像有__iadd__方法的话，直接调用，如果没有， 则调用__add__方法，这意味着重新赋值
# 可变序列一般都有__iadd__方法，
l = [1, 2, 3]
print(id(l))  # 139697246068808
l += [4, 5]   # l.extend([4, 5])
print(id(l))  # 139697246068808

t = (1, 2)
print(id(t))  # 139697244810312
t += (4, 5)
print(t)
print(id(t))  # 139697244872120

# 例子
t = (1, 2, [30, 40])
# t[2] += [50, 60]  # 这个问题已经被捕捉了
t[2].extend((50, 60))

"""特性： 排序"""
# list.sort 和 sorted()
# list.sort 就地排序，直接对原列表排序
# sorted() 会返回排好序的列表
# 都有两个关键字参数reverse 和 key ---> 函数 如len
l = ['aaa', 'bbbbb', 'cccccccc']
l.sort(key=len, reverse=True)  # 会按照元素长度降序排序


# 字典特性 setdefault  defaultdict  __missing__
# __missing__ dict 中并没有实现，但是如果继承字典类中实现了__missing__ 方法，那么__getitem__ k 不存在的时候会自动触发 __missing__ 方法
# 和 default 一样只对 __getitem__ 调用方式有用
# k in dict.keys() 查找速度在py3中其实不慢，dict.keys() 是一个视图对象
class DictA(dict):

    def __missing__(self, key):
        return 'hello'


d = DictA()
print(d['a'])


# example
class UserDict(dict):

    def __missing__(self, key):
        print(11111111)
        # __getitem__调起来的key
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    # def get(self, key, default=None):
    #
    #     try:
    #         return self[str(key)]
    #     except KeyError:
    #         return default


dd = UserDict([(1, 2), ('2', 3)])
# print(dd['3'])
print(dd.get(3, 4))


# collections.OrderDict  Counter  UserDict
# OrderDict 有序字典
# Counter 计数器

from collections import Counter

ct = Counter(['a', 1, 2, 3, 123123, 3, 4, 3, 2, 1, 123123])
print(ct)  # >>> Counter({3: 3, 1: 2, 2: 2, 123123: 2, 'a': 1, 4: 1})
print(ct.most_common(2))

# UserDict  纯python实现的dict 常用来被继承用【自定义dict的时候继承它】
# types.MappingProxyType 不可变映射类型，只读，不可更改，但它是动态的

from types import MappingProxyType
d = {'a': 1}
d_proxy = MappingProxyType(d)
print(d_proxy, type(d_proxy))
print(d_proxy['a'])
# d_proxy['b'] = 2 # mappingproxy' object does not support item assignment
d['b'] = 2
print(d_proxy)

# 集合  set中的元素 不可变且唯一 但集合本身是可变的 且无序的
# frozenset 不可变集合
# 集合的 交 并 补 运算， 创建空集用set()
# 如果可能，推荐使用{1， 2， 3}的形式创建集合，比 set([1, 2, 3]) 要快 因为针对{}这种方式，python有一个build_set 的字节吗来创建集合
# 但是 frozenset 只能用 frozenset的形式

# 集合推导式


# 集合和字典的特性 散列表
# 如果 要在 100万的双精度浮点数中查找 1000个元素，集合和字典 要比列表快的多。没有散列表来支持in运算符

"""
散列表算法：
为 了 获 取 my_dict[search_key] 背 后 的 值,Python 首 先 会 调 用 hash(search_key) 来 计 算
search_key 的散列值,把这个值最低的几位数字当作偏移量,在散列表里查找表元(具
体取几位,得看当前散列表的大小)。若找到的表元是空的,则抛出 KeyError 异常。若不
是空的,则表元里会有一对 found_key:found_value 。这时候 Python 会检验 search_key ==
found_key 是否为真,如果它们相等的话,就会返回 found_value 。
如果 search_key 和 found_key 不匹配的话,这种情况称为散列冲突，为了解决散列冲突,算法会在散列值中另外再取几位,然后
用特殊的方法处理一下,把新得到的数字再当作索引来寻找表元。

一个可散列的对象必须满足以下要求。
(1) 支持 hash() 函数,并且通过 __hash__() 方法所得到的散列值是不变的。
(2) 支持通过 __eq__() 方法来检测相等性。
(3) 若 a == b 为真,则 hash(a) == hash(b) 也为真。

散列又叫hash，可以将一个任意长度的输入压缩到某一固定长度摘要消息的函数
hash(1123123123123121312312333333333333333333333333)
"""
# 但字典是散列表，所以吃内存。数量比较的大的 记录 可以使用元祖 和 命名元祖来存。
# 字典键查询速度非常快，典型的用空间来时间，内存开销很大，但是访问速度很快。
# 字典键的次序取决于添加顺序
# 往字典里添加新键可能会改变已有键的顺序


# 首先对字典迭代,以得出需要添加的内容,把这些内容放在一个新字典里;迭代
# 结束之后再对原有字典进行更新。  todo 需要一个场景，列表遇见过，字典还没遇见过

dd = dict.fromkeys(list(range(100)))

for i in dd:
    if  i > 50 and i < 100:
        dd[i] = 'hahaha'
print(dd)


################## 文本和字节 ######################

# 把码位转化成字节的过程就叫编码








