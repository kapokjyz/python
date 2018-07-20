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