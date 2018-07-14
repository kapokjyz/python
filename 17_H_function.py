# 高阶函数
# 变量可以指向函数
# 我们先定义一个函数
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# 正常调用这个函数：
print(my_abs1(-100))  # 打印出100
# 如果只写abs函数本身
print(my_abs1)  # 打印出 <function my_abs1 at 0x0385DD68> 
# 可见 my_abs1(-100) 是函数调用，而 my_abs1 是函数本身
# 要获得函数调用结果：
x = my_abs1(-99)
print(x)
# 但是，如果把函数本身赋值给变量呢？
f = my_abs1
print(f)  # 打印出 <function my_abs1 at 0x0385DD68>
# 结论：函数本身也是可以赋值给变量的，即：变量可以指向函数

print(f(-10))

# 函数名也是变量
# 函数名其实就是指向函数的变量，对于 my_abs1() 这个函数，完全可以把函数名 my_abs1 看成变量，它指向一个可以计算绝对值的函数！

# 如果把 my_abs1 指向其他对象，会有什么情况发生呢？
my_abs1 = 10
# my_abs1(-99)  不能打印出99，会返回错误
# my_abs1 指向10之后，就无法通过 my_abs1(10) 调用该函数了，因为 my_abs1这个变量不再指向求绝对值的函数了，而是指向一个整数 10
# 实际代码不能这样写，这里只是表明函数名也是变量
# 如果更改的是系统函数，如 abs 函数；要恢复的话，需要重启 python 交互环境
# 注：系统函数abs,实际上定义在 import builtins 模块中，要让修改 abs 变量的指向在其他模块也生效，要用 import builtins; builtins.abs = 10

# 传入函数
# 既然变量可以指向函数，函数的参数就可以接收变量，那么一个函数就可以接收另一个函数作为参数，这个函数就称之为高阶函数
# 例如：
def add(x, y, f):
    return f(x) + f(y)
r = add(-5, 6, abs)
print(r)

# 小结：把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
