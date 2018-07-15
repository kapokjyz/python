# python内建了 map() 和 reduce() 函数
# map() 函数接收两个参数，一个是函数，一个是 Iterable ,map 将传入的函数依次作用到序列的每个元素，并把结果作为新的 Iterator 返回。
def f(x):
    return x * x

r = map(f, [1,2,3,4,5,6,7,8,9])
L = list(r)
print(L)

# map() 作为高阶函数，事实上它把运算规则抽象了，它不但可以计算简单的f(x) = x^2(表示平方),还可以计算任意复杂的函数，比如，把这个list的所有数字转换成字符串：
L = list(map(str, [1,2,3,4,5,6]))
print(L)

# reduce 把一个函数作用在一个序列 [x1, x2, x3, ...] 上，这个函数必须接收两个参数，例如：reduce 把结果和序列的下一个与阿奴做累计计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def add(x, y):
    return x + y
s = reduce(add, [1,3,5,7,9])
print(s)

# 使用 map() ，把str转换为int的函数：
def fn(x, y):
    return x * 10 + y
def char2num(s):
    digits = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
    return digits[s]
r = reduce(fn, map(char2num, '13579'))
print(r)
