#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

# 面向对象最重要的概念就是类（class）和实例（instance）
class Student(object):
    pass
# class后面紧接着就是类名，即Student，类名通常都是大些开头的单词，紧接着是(object),表示该类是从那个类继承下来的．如果没有合适的继承，就使用object类，这是所有类都会继承的类．

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去，通过定义一个特殊的__init__方法，在创建实例的时候，就把name,score等属性绑定上去：
class Student_1(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
zeng = Student_1('zj', 99)
print(zeng.name,zeng.score)
# 注意：__init__　方法的第一个参数永远都是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self．

# 数据封装 --> 类的方法
class Student_2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print("%s: %s" % (self.name, self.score))
zeng = Student_2('zl', 100)
zeng.print_score()

