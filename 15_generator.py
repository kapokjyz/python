# 生成器：它是在 for 循环的过程中不断计算出下一个元素，并在适当的条件结束for循环
# 创建一个generator， 有很多方法
# 第一种：把列表生成式的 [] 改成 () ，就创建了一个generator：
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
# print(g) 输出<generator object <genexpr> at 0x03738F00>
# 我们可以直接打印出list的每一个元素，但是我们怎么打印出generator 的每一个元素呢，如果一个一个的打印出来，可以通过next()函数获得generator的下一个返回值
print(next(g))
print(next(g))
print(next(g))

# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，知道计算到最后一个元素，没有更多元素时，会抛出 StopIteration 的错误。
# 不断使用next()也是比较麻烦的，可以使用for循环来迭代它，generator 也是可迭代对象
for n in g:
    print(n)

# 案例：斐波拉契数列，用列表生成式写不出来，但是用函数把他打印出来却很容易
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
fib(5)
# 上面的赋值语句：a, b = b, a + b ;相当于：
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

# fib()函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似 generator
# 把fib()函数变成 generator ，只需要将print(b) 改成 yield b 就可以了：
def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
# 包含了 yield 关键字的函数，是一个generator 
f = fib1(5)
print(f)
print(next(f))
for n in f:
    print(n)
# 记住，函数是顺序执行，遇到return或者最后一行就返回，而变成 generator 的函数，在每次调用next()的时候，遇到yield 语句返回，再次执行的时候从上次返回 yield 语句出执行

# 调用 generator 时，发现拿不到 generator 的return语句返回值；如果想要拿到返回值，必须捕获 StopIteration 错误（再取完所有的值后再继续取值就报这个错），返回值包含再 StopIteration 的 value 中。

g = fib1(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break

# 练习：输出杨辉三角
def triangles(lines):
    n, m, a, b = 0, 0, 0, 1
    L = [1]
    while n < lines:
        yield L
        L =[1] + [L[i] + L[i+1] for i in range(len(L)-1)] + [1] 
        n = n + 1
g = triangles(5)
for n in g:
    print(n)        
