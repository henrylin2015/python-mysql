#!/usr/bin/env python3
# -*- coding: utf-8 -*-
worldlst = list(map(chr, range(ord('a'), ord('z') + 1)))
print("list:", worldlst)


# 问题一，以下的代码输出的将是什么，说出你的答案和解释
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass

print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

# 答案
"""
1 1 1
1 2 1
3 2 3
使你困惑或是惊奇的是关于最后一行的输出 3 2 3 而不是3 2 1。为什么改变了Parent.x的值还会改变Child2.x的值，
但是同时Child1.x的值却没有改变呢？
这个答案的关键是，在Python中，类变量在内部是作为字典处理的。如果一个变量的名字没有在当前类的字典中发现，
将搜索祖先类(比如父类)直到被引用的变量名被找到（如果这个被引用的变量名即每一在自己所在的类和祖先类中找到，会引发一个AttributeError异常）
"""
