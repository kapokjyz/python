#!/usr/bin/python3.5
# python 本身内置了很多非常有用的模块。
# 例如：通过内建的sys模块，编写一个hello模块
#__author__ = 'micheal zeng'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world")
    elif len(args) == 2:
        print("hello ,%s" % args[1])
    else:
        print("Too many arguments!")
if __name__ == '__main__':
    test()

#作用域，一般分为：公开（public）,非公开（private）;不过这只是从编程习惯上的，python并没有一种方法可以完全限制访问private函数和变量．
#例如：
def _private_1(name):
    return 'hello, %s' % name
def _private_2(name):
    return 'hi, %s' % name
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
