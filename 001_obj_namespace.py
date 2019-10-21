# 类和对象分别各自为一个命名空间
# obj.name = 'muyi'  对象可以使用.进行属性赋值
# 类属性要由类来修改  ！ 最好不用对象去修改类属性

class A:
    count = 0
    def __init__(self):
        A.count += 1
        # self.count += 1


a = A()
b = A()
c = A()
print(a.count)
print(A.count)

# 组合 一个类的属性值是另一个对象
# demo 人狗大战
class Person:

    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp
        self.money = 0

    def attack(self, dog):
        dog.hp -= self.aggr

    def get_weapon(self, weapon):
        if self.money > 0:
            self.money -= weapon.price
            self.aggr += weapon.aggr


class Dog:

    def __init__(self, name, aggr, hp):
        self.name = name
        self.aggr = aggr
        self.hp = hp

    def bite(self, person):
        person.hp -= self.aggr

class Gear:

    def __init__(self, name, aggr, skill, price):
        self.name = name
        self.aggr = aggr
        self.skill = skill
        self.price = price




p = Person('ellen', 100, 200)
d = Dog('doudou', 200, 50)
w = Gear('小刀', 100, 3, 250)

d.bite(p)
print(p.hp)
p.money = 300
p.get_weapon(w)
print(p.aggr)
p.attack(d)
print(d.hp)
# 面向对象最好玩地方之一

# 10-09 工作 paramiko 模块学习
# 192.168.0.105
# import paramiko
#
# client = paramiko.SSHClient()
# # 自动添加策略，不添加 非konw_hosts 里的ip 无法链接
# client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
# client.connect(hostname='192.168.1.105', port=22, username='root',
#                password='123')

# 面向对象 继承
# class A:
#     def __init__(self, name):
#         self.name = name
#
#     # def __del__(self):
#     #     print('yyy')
#
#     def __enter__(self):
#         print('connect to xxx.xxx')
#
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('close the socket')
#
# class B(A):
#
#     def __init__(self, name, sex):
#         A.__init__(self, name)
#         self.sex = sex
#
#
#     def self_introduce(self):
#         print('Hi everyone I am %s and I am a %s' % (self.name, self.sex))
#
#
# ellen = B('ellen', 'girl')
#
# with ellen:
#     print('exec the test case')
#
# a = True
# ### testing ###
# class C:
#
#     def  run_cmd(self, method_xx, method_yy, **kwargs):
#         if a :
#             print(kwargs)
#             method_xx(kwargs)
#         else:
#             method_yy(kwargs)
#
#
#     def  xx_a(self, a=None):
#         print(a)
#
#
#     def yy_a(self, a=None):
#         print(a)
#
#     def  xx_b(self, a=None, b=None):
#         print(a, b)
#
#     def yy_b(self, a=None, b=None):
#         print(a, b)

# c = C()
#
# c.run_cmd(c.xx_a, c.yy_a, a=1)
# c.run_cmd(c.xx_b, c.yy_b, 1, 2)
# 可以实现但是没必要， 失去可读性了， 简洁可读，服务用户
# super关键字


class A:

    def func(self):
        print('a')


class B(A):

    def func(self):
        super().func()
        print('b')


class C(A):

    def func(self):
        super().func()
        print('c')


class D(B, C):

    def func(self):
        super().func()
        print('d')


d = D()
# d.func()   # 新式类的继承方式是广度优先， 根据的是算法节点找的








