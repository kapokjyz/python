# 列表生成式：即 list comprehensions,是python内置的非常简单却强大的可以用来创建list的生成式
# 如果，要生成list [1,2,3,4,5,6,7,8,9] 可以用list(range(1, 10))
print(list(range(1, 10)))

# 但是，要生成[1*1, 2*2, 3*3,..., 10*10]怎么做呢？
# 方法一：循环
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 但循环太繁琐了，而列表生成式则可以用一行语句代替循环生成上面的list：
L1 = [x * x for x in range(1, 11)]
print(L1)

# 还可以使用两层循环，可以生成全排列
L2 = [m + n for m in 'abc' for n in 'xyz']
print(L2)

# 三层或三层以上的循环就比较少用到了
import os
# os.listdir 可以列出文件和目录
L3 = [d for d in os.listdir('.')]
print(L3)

# 我们知道 for 循环可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x':'a', 'y':'b', 'z':'c'}
for k, v in d.items():
    print(k, ' = ', v)
# 对应的列表生成式也可以使用两个变量来生成list
d = {'x':'a', 'y':'b', 'z':'c'}
L4 = [k + ' = ' + v for k, v in d.items()]
print(L4)

# 可以把list中所有的字符串都变成小写的：
L5 = ['Hello', 'World']
L6  = [s.lower() for s in L5]
print(L6)

# 练习：非字符串类型没有lower()方法，如果list中既有字符串，又有数字，上面的列表生成式就会报错；修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L7 = ['Hello', 18, 'World', 20, 'Apple', None]
L8 = [s.lower() for s in L7 if isinstance(s, str)]
print(L8)
 