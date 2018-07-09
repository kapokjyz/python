# python函数的参数非常的灵活，除了正常定义的必选参数外，还可以使用默认参数，可变参数和关键字参数

# 位置参数（必选参数 ）
# def a(x):
#     return x * x
# print(a(5))

# def a(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(a(5, 3))

# 上面的a(x, n)函数定义的没有问题，但是，旧的调用代码失效了，原因是我们增加了一个参数，导致旧的代码因为确实一个参数而无法正常调用：

# 默认参数
def a(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(a(5))
print(a(5, 3))

# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数；也可以不按顺序提供部分默认参数，但得要把参数名写上：
def enroll(name, gender, age = 6, city = 'shenzhen'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll('zeng', 'M', 7)
enroll('jian', 'F', city='jiujiang')
enroll('meiniu', 'F')

# 默认参数有个坑：
def add_end(L = []):
    L.append('end')
    return L

# 当正常调用的时候，结果似乎是对的：
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

# 当使用默认参数调用时，一开始结果也是对的：
print(add_end())  #输出 ['end']

# 当再次使用默认参数调用时，结果就不对了
print(add_end())  #输出 ['end', 'end']
# 原因是：python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了

# 要修改上面的例子，我们可以用None这个不变的对象来实现
def add_end1(L = None):
    if L == None:
        L = []
    L.append('end')
    return L
print(add_end1())
print(add_end1())
print(add_end1([100, 99, 98]))

# 可变参数：在python函数中，可以定义可变参数，顾名思义，就是传入的参数个数是可变的

# 案例：给定一组数字a, b, c...，计算各个数的平方的和。
def calc(num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum
# 调用的时候需要先组装一个list或者tuple
print(calc([1,2,3]))
print(calc([1,2,3,4]))

# 如果利用可变参数的话，调用函数的方式可以简化成：
def calc1(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum
print(calc1(1,2,3))
print(calc1(1,2,3,4))
# 可以传入0个参数
print(calc1())

# 如果已经有一个list或者tuple，要调用一个可变参数时，可以这样做：
num = [1,2,3]
print(calc1(*num))
# *num表示把num这个list的所有元素作为可变参数传进去

# 关键字参数：可变参数允许你传入0个或任意个参数，这个可变参数在函数调用时自动组装为一个tuple，而关键字参数允许你传入0个或任意个含有参数名的参数，这些关键字参数在函数内部自动组装为一个dict：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('zeng', 25, city = 'jiangxi')
person('jian', 100, gender = 'M', job = 'engineer')
# 关键字参数它的作用，在于能够拓展函数的功能，比如，在person函数里，我们保证能接收到name和age这两个参数，但是如果调用者愿意提供更多的参数，我们也能够收到。例如：一个用户注册的功能，除了用户名和年龄是必填选项外，其他的都是可选项，利用关键字参数来定义函数就可以满足注册的需求
# 同上可变参数，如果已经有一个字典了，可以这样简化调用：
extra = {'city': 'jiangxi', 'job': 'engineer'}
person('tony', 28, **extra)
# **extra表示把extra这个dict的所有key-value用关键字参数传入到哈数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

# 命名关键字参数





