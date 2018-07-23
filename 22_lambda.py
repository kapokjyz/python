# 当我们在传入函数时，有些时候，不需要显示的定义函数，直接传入匿名函数更方便。
lambda x: x * x
# 上面这个匿名函数就是：
def f(x):
    return x * x
# 匿名函数有一个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数复制给一个变量，然后再利用变量来调用该函数
f = lambda x:x * x
print(f(4))

# 同样，可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y
r = build(4, 5)
print(r())

L  = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)