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
class DictA(dict):

    def __missing__(self, key):
        return 'hello'


d = DictA()
print(d['a'])