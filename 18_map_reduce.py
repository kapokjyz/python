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

# 整理成一个str2int 的函数就是：
DIGITS = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
def str2int(s):
    def fn_1(x, y):
        return x * 10 + y
    def char2num_1(s):
        return DIGITS[s]
    return reduce(fn_1, map(char2num_1, s))

print(str2int('123456'))
# 还可以用 lambda 函数进一步优化：
def char2num_2(s):
    return DIGITS[s]
def str2int_1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num_2, s))
print(str2int_1('6879'))

# 练习 1 ：把不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    str = name
    return str.capitalize()
L1 = ['adam', 'LISA', 'barI']
L2 = list(map(normalize, L1))
print(L2)

# 练习2 ：编写一个prod() 函数，可以接收一个list 并利用reduce()求积：
def prod(L):
    def pr(x, y):
        return x * y
    return reduce(pr, L)
r = prod([1,2,3,4])
print(r)

# 练习 3：利用 map 和 reduce 编写一个str2float 函数，把字符串'123.456' 转换成浮点数 123.456：
def str2float(s):
    # find()返回查找的字符串的位置值
    i = s.find('.')
    g = (x for x in s if x != '.')
    def fn_2(x, y):
        return x * 10 + y
    def char2num_2(s):
        return DIGITS[s]
    r =reduce(fn_2, map(char2num_2, g))
    print(r)
    n = 1
    for j in range(len(s) - i - 1):
        n = n * 10
    return r/n
r1 = str2float('123.456')
print(r1)
r2 = str2float('123.456789')
print(r2)

