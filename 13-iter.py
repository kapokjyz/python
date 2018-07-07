# 迭代：如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（iteration）

# 迭代通过 for...in 来完成的
# 可迭代对象：字符串、list、tuple、dict、
str = '123456'
for s in str:
    print(s)

# 因为dict存储不是按照list的方式顺序排列的，所以，迭代出的结果顺序可能是不一样的
# 默认情况下，dict迭代的是key
d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key)

# 如果要迭代value，可以用：
for value in d.values():
    print(value)

# 如果要同时迭代key和value，可以用：
for k, v in d.items():
    print(k, v)

#使用for循环的时候，只要作用于一个可迭代对象，for循环就可以正常运行，而不会关心对像究竟是list还是其他数据类型。
# 通过collections 模块的Iterable类型判断对像是否是一个可迭代对象
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1,2,3], Iterable))
print(isinstance(123, Iterable))

# 如果要对list实现类似Java那样的下标循环的话，可以使用python内置的 enumerate 函数可以把一个list变成 索引--元素对，这样就可以再for循环中同时迭代索引和元素本身：
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# for 循环里面同时引用两个变量，在python里面是很常见的
for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)

# 练习：使用迭代查找一个list中最小和最大值，并返回一个tuple
def FindMixAndMax(L):
    if L == []:
        print('The list is empty')
        return (None, None)
    else:
        min = L[0]
        max = L[0]
        for x in L[1:]:
            if min > x:
                min = x
            elif max < x:
                max = x
        return (min, max)

T = FindMixAndMax([1, 0, 2, 6, 10])
print(T)
T = FindMixAndMax([])
print(T)

