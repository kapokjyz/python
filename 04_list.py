# 列表类型list，list是一种有序的集合，可以随时添加和删除其中的元素
a = ['bob','tracy','mich']
print(a)
print(len(a))
# 可以通过索引来访问list中的元素，索引从0开始
print(a[0])
print(a[1])
print(a[2])

# 索引还可以是用负数来表示，索引 -1 表示最后一个元素，-2 表示倒数第二个元素
print(a[-1])
print(a[-2])
print(a[-3])

# 添加元素到list列表的末尾
a.append('zeng')
print(a)

# 添加元素到指定位置
a.insert(2, 'jian')
print(a)

# 删除list末尾的元素
a.pop()
print(a)

# 删除list指定位置的元素、
a.pop(2)
print(a)

# list里面的元素可以是可以直接赋值
a[0] = 'zeng'
a[1] = 'jian'
print(a)

# list里面的元素可以是不同类型的数据
b = ['apple', 123, 456]
print(b)

# list里面的元素可以是另一个list
c = ['white', [111, 222, 333], 'black']
print(c)
print('c len = %d' %len(c))
#取出222
print(c[1][1])