# 迭代器
# 先介绍下，可以直接用于for循环的数据类型有一下几种：
# 1、集合数据类型：list、tuple、dict、set、str等；
# 2、generator：生成器和带 yield 的generator function
# 这些都叫做可迭代对象：Iterable

# 而生成器不但可以作用于 for 循环，还可以被next() 函数不断调用并返回下一个值，直到最后返回 StopIteration 错误表示无法继续返回下一个值了
# 可以被next() 函数调用并不断返回下一个值的对象称为迭代器： Iterator
# 可以使用 isinstance() 判断一个对象是否是 Iterator 对象：
from collections import Iterator
result = isinstance((x for x in range(10)), Iterator)
print(result)
result = isinstance([], Iterator)
print(result)
result = isinstance({}, Iterator)
print(result)
result = isinstance('abc', Iterator)
print(result)

# 为什么list、dict、str等数据不是Iterator？
# 这是因为python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据返回是抛出一个 StopIteration 错误，可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能通过不断的next() 函数实现按需计算下一个数据，所以 Iterator的计算是有惰性的，只有在需要返回下一个数据时，它才会计算。
# Iterator 甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

# Iterable 可以通过 iter() 函数获得一个Iterator 对象。例如：
for x in [1,2,3,4,5]:
    pass
# 实际上完全等价于：
# 首先先获得Iterator对象：
it = iter([1,2,3,4,5])
while True:
    try:
        # 获得下一个值：
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到 StopIteration 就突出循环
        break
