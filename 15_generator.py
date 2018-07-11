# 生成器：它是在 for 循环的过程中不断计算出下一个元素，并在适当的条件结束for循环
# 创建一个generator， 有很多方法，第一种：把列表生成式的 [] 改成 () ，就创建了一个generator：
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

