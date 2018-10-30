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

# 继承
class Animal(object):
    def run(self):
        print('Animal is running...')
class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
cat = Cat()
dog.run()
cat.run()

# 多态
class Dog1(Animal):
    def run(self):
        print('Dog is running...')
class Cat1(Animal):
    def run(self):
        print('Cat is running...')

dog1 = Dog1()
cat1 = Cat1()
dog1.run()
cat1.run()

# 当我们定义一个class的时候，我们实际上就定义了一种数据类型。跟str、list等没什么两样。
a = list()  # a是list类型
b = Animal() # b是Animal类型
c = Dog1()  # c是Dog1类型

# 注意，c不仅是Dog1类型，同时也是Animal类型

# 多态的好处
def run_twice(animal):
    animal.run()
run_twice(Animal())
run_twice(Dog())
run_twice(Cat())
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思

# 实际上，python语言是动态语言，不一定需要传入Animal类型，我们只需要保证传入的对象有一个run()方法就可以了，
class Timer(object):
    def run(self):
        print('Start...')
run_twice(Timer())
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。