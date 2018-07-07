# 切片： slice
# 取出一个list的前3个元素
L = ['a', 'b', 'c', 'd', 'e', 'f']
print(L[0:3])
# L[0:3]表示从索引0开始，知道索引3为止，但不包括索引3，即索引0,1,2

#L[1:4]同理
print(L[1:4])

# 如果第一个索引是0，还可以省略
print(L[:3])

# python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片
print(L[-2:])
print(L[-2:-1])
# 记住倒数的第一个元素的索引是-1

# 创建0--99的数列
L = list(range(100))
# 前10个数，每两个取一个
print(L[:10:2])
# 所有的数每5个取一个
print(L[::5])

# L[:]表示整个list
M = L[:]
print(M)

# tuple也是一种list，唯一的区别就是tuple不可变，因此，tuple也可以用切片操作，知识操作的结果仍是tuple
M = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(M[::2])
# 其他操作同理

# 字符串'xxx' 也可以看成是一种list，每个元素就是一个字符，因此，字符串也可以用切片操作，只是操作结果仍是字符串：
S = 'abcdefghigklmnopqrstuvwxyz'
print(S[:3])
print(S[::2])

# 练习：利用切片操作，试下一个trim()函数，去除字符串首尾的空格
def trim(s):
    if s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    else:
        print(s)

trim('  123456   ')
trim('  abcdef ')