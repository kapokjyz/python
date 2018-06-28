# tuple类型数据，叫元组，也是一种有序列表，tuple一旦初始化就不能更改。写代码的时候，可以利用其不可变的特性，使代码变得更安全。
a = ('white', 'yellow', 'red')
print(a)
print(a[0])
print(a[1])
print(a[2])
print(a[-1])
print(a[-2])
print(a[-3])

# 定义一个空的tuple
b = ()
print(b)

# 如果要定义一个只有1个元素的tuple，就需要注意了
c = (1)
print(c)
# 这时候定义的就不是tuple，而是 1 这个数，这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义。因此，python规定，上面这种情况，按小括号进行计算

# 定义只有一个元素的tuple，必须加一个逗号,以免误解成数学计算意义上的括号
d = (1,)
print(d)

# tuple中可以包含list，而这个list中的元素是可变的，因为对于tuple而言，它的元素list没有变
e = (1, 2, 3, ['a', 'b', 'c'])
print(e)
e[3][0] = 'engineer'
print(e)