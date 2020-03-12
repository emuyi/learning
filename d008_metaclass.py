data = {"Schedule":
            {"conferences": [{"serial": 115}],
             "events": [
                 {"serial": 34505,
                  "name": "Why Schools Don´t Use Open Source to Teach Programming",
                  "event_type": "40-minute conference session",
                  "time_start": "2014-07-23 11:30:00",
                  "time_stop": "2014-07-23 12:10:00",
                  "venue_serial": 1462,
                  "description": "Aside from the fact that high school programming...",
                  "website_url": "http://oscon.com/oscon2014/public/schedule/detail/34505",
                  "speakers": [157509],
                  "categories": ["Education"]}
             ],
             "speakers": [
                 {"serial": 157509,
                  "name": "Robert Lefkowitz",
                  "photo": None,
                  "url": "http://sharewave.com/",
                  "position": "CTO",
                  "affiliation": "Sharewave",
                  "twitter": "sharewaveteam",
                  "bio": "Robert ´r0ml´ Lefkowitz is the CTO at Sharewave, a startup..."}
             ],
             "venues": [
                 {"serial": 1462,
                  "name": "F151",
                  "category": "Conference Venues"}
             ]
             }
        }

# todo 1、将上诉数据结构由 data['Schedule']['speakers'][0]['name'] 取值变成 data.Schedule.speaker[0].name (链式取值)
# 相关的模块 AttrDict：以属性的形式访问字典或json等数据类型
# from attrdict import AttrDict
#
# data = AttrDict(data)
# print(data.Schedule.speakers[0].name)
# print(data.Schedule.items())
from collections import abc

class FrozenJson:
    def __init__(self, d):
        self.__data = dict(d)

    def __getattr__(self, item):
        if hasattr(self.__data, item):  # 为了调用原生字典的属性
            return getattr(self.__data, item)  # 返回 属性值
        else:
            return FrozenJson.build(self.__data[item])

    @classmethod
    def build(cls, obj):
        '''处理字典和列表的情况，如果全是字典，就不用build方法'''
        if isinstance(obj, abc.Mapping):
            return cls(obj)       # 如果是字典的话就返回 frozenjson 对象
        elif isinstance(obj, abc.MutableSequence):  # 如果是列表
            return [cls(item) for item in obj]
        else:
            return obj


"""
class FrozenDict:

    def __init__(self, data):
        self.data = dict(data)  # 重新创建一份拷贝不污染源对象

    def __getattr__(self, item):
        if hasattr(self.data, item):   # 保留dict 原有的属性和方法
            return getattr(self.data, item)

        if isinstance(self.data[item], abc.Mapping):
            return FrozenDict(self.data[item])      # 可以递归取值
        elif isinstance(self.data[item], abc.MutableSequence):
            return [FrozenDict(obj) for obj in self.data[item]]
        else:
            return self.data[item]
"""


fz = FrozenJson(data)
print(fz.Schedule.speakers[0].items())  # 所以必须要处理列表这种情况
# 但不支持 字典的原生方法

class B:
    count = 0

    def __getattr__(self, item):
        print(item)
        print(111111)
        return 233


b = B()
print(b.count)
print(b.a)
# ___getattr__方法：对象访问属性时，如果该属性不存在会调用该方法，如果未定义该方法抛出 attribute error




