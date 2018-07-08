# 函数，有系统内部的函数供我们使用，也可以自定义函数使用
# abs(),求绝对值的系统函数
# 调用abs()函数时，如果参数的类型或者数量不对的话，就会报错
print(abs(-5))
# abs('a')
# abs(1, 2)

# max()函数，可以接收多个参数，并返回最大的那个参数：
print(max(1, 2))
print(max(100,99,98,97))

# 数据类型转换函数
print('123')
print(int('123'))
print(float('12.34'))
print(str(1.2345))
print(str(100))
print(bool(1))
print(bool(''))

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个‘别名’：
a = abs
print(a(-1))

print(hex(255))
print(hex(1000))

# 自己定义一个函数，需要使用def语句，一次写出函数名，括号，括号中的函数和冒号：然后再缩进块中编写函数体，函数的返回值用return语句返回
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

# 如果没有return语句，函数执行完毕后也会返回结构，只是结果为None，return None可以简写为return
# 在python的交互环境中定义函数时，主义python会出现...的提示，函数定义结束后需要按两次回车重新回到>>>提示符下：

# 如果你已经把my_abs()的函数定义保存为abstest.py文件了，那么，可以在该文件的当前目录启动python解释器，用 form abstest import my_abs 来导入my_abs()函数，注意 abstest是文件名（不含.py扩展名）

# 空函数
# 如果想定义一个什么事情也不做的空函数，可以用pass语句：
def nop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没有想好怎么写函数的代码，就可以先放一个pass，让代码运行起来
age = 0
if age >= 18:
    pass
# 缺少pass，代码就会运行错误

# 参数检查
# 调用函数时，如果参数个数不对，python解释器会自动检查出来，并抛出TypeError：
# 但如果参数类型不对，python解释器就无法帮我们检查
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
print(my_abs1(-123))
# print(my_abs1('a'))

# 返回多个值
# 函数可以返回多个值，但其实是一种假象，返回值是一个tuple! 在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，python的函数返回多个值其实就是返回一个tuple，但写起来更加方便
import math
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
r = move(100, 100, 60, math.pi / 6)
print(x, y)
print(r)

# 练习， 接受3个参数，返回一个一元二次方程 ax2(这里是平方)+bx+c 的两个解：
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('bad operand type') 
    if not isinstance(b, (int, float)):
        raise TypeError('bad operand type')
    if not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    d = b*b - 4*a*c
    if d < 0:
        return False

    x1 = 0.0
    x2 = 0.0
    
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / 2*a
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / 2*a
    return x1, x2
n = quadratic(1, 3, -4)
print(n)
m = quadratic(1, 2, 3)
print(m)

