# 高阶函数除了可以接收函数作为参数外，还可以把函数作为结果值返回
# 以求和函数作为例子，通常我们是如下定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 当我们不需要立刻求和，而是在后面的代码中，根据需要再进行计算怎么办，这是就可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
L = [1,3,5,7,9]
f = lazy_sum(*L)
L.append(11)
print(L)
print(f())

#  内部函数可以引用外部函数的参数和局部变量，这种称为闭包，这种程序结构具有极大的威力

# 有一个需要注意的是，返回的函数没有立即执行，而是知道调用了f()才执行。
# 例如：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print(f1()) # 输出9
print(f2()) # 输出9
print(f3()) # 输出9
# 上面全部输出9的原因在于，返回的函数并没有立即执行，而是等到3个函数都返回时，它们所引用的变量i,都已经改变成3了，因此最终结果为9

# 返回闭包时，牢记一点，返回函数不要引用任何循环变量，或者后续会发生改变的变量。

def count_1():
    def f():
        def g():
            return i * i
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f4, f5, f6 = count_1()
print(f4())
print(f5())
print(f6())