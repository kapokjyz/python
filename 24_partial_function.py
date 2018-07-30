# python的 functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）
# 例如：int() 函数可以把字符串转换成整数，当仅传入字符串时，int()函数默认按十进制进行转换
int('12345')  # 转换后的结果为: 12345

# 但int() 函数还提供额外的 base 参数，默认值为10， 如果传入base参数，就可以做 N 进制转换：
print(int('12345', base = 8))  # 转换后的结果为: 5349
print(int('12345', base = 16)) # 转换后的结果为：74565

# 向上面一样每次都要传入两个参数，还是比较麻烦的，可以这样：
# def int8(x, base = 8):
#     return int(x, base)
# def int16(x, base = 16):
#     return int(x, base)
# print(int8('12345'))
# print(int16('12345'))

# def int2(x, base = 2):
#     return int(x, base)
# print(int2('1000000'))

# functools.partial 就是帮助我们创建一个偏函数的，不需要我们自己定义int2() ，可以直接使用下面的代码创建一个新的函数int2：
import functools
int2 = functools.partial(int, base = 2)
print(int2('1000000'))

# 简单总结，functools.partial 的作用就是，把一个函数的某些参数给固定住（也就是默认值），返回一个新的函数，调用这个新函数会更简单。
# 上面的 int2 函数也可以在函数调用时传入其他的值
print(int2('1000000', base = 10))

# !!! 最后，创建骗函数时，实际上可以接收函数对象，*args和**kw这3个参数
# 例如：
int2 = functools.partial(int, base = 2)
# 实际上固定了 int() 函数的关键字参数base, 也就是
int2('1000000')
# 相当于：
kw = {'base': 2}
print(int('1000000', **kw))