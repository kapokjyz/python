# unicode编码标准，通常是用2个字节表示一个字符（非常偏僻的字符，就需要用到4个字符）
# UTF-8编码，是可变长的编码；UTF-8编码把一个Unicode字符根据不同的数字大小编码成 1-6 个字节，常用的英文字母就编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节。如果文本包含很多英文字符，使用UTF-8就可以节省空间；

# ord() 函数获取字符的整数表示
# chr() 函数把编码转换为对应的字符
print(ord('a'))
print(ord('中'))
print(chr(98))
print(chr(25991))

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
# Python对bytes类型的数据用带b前缀的单引号或双引号表示
x = b'abc'
print(x)

# encode()函数可以更改 str 的编码方式
x = 'ABC'.encode('ascii')
print(x)
x = '中文'.encode('utf-8')
print(x)
# 含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# x = '中文'.encode('ascii')

# decode()；反过来，如果我们从网络或者磁盘上读取了字节流，那么读取到的数据就是bytes（字节），要把bytes变为str（字符串），就需要用到decode()方法：
x = b'ABC'.decode('ascii')
print(x)
x = b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
print(x)
# 如果bytes中包含不能解码的字节，decode()函数会报错
# x = b'\xe4\xb8\xad\xe6\x96\xff'.decode('utf-8')
# print(x)

# len()函数可以计算str包含了多少个字符
print(len('abc'))   # 结果为3
print(len('中文'))   # 结果为2
# len()函数计算的str的字符数，如果换成bytes，len()函数就是计算的字节数。
print(len(b'abc'))  #结果为3
x = len('中文'.encode('utf-8'))
print(x)  #结果为6
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))  #结果为6