# dict,字典，全称dictionary，使用键值对的形式（key--value）存储，具有极快的存储速度。
# dict通过key计算位置的算法是哈希算（hash）
# dict的特点：用空间换取时间，key是不可变对象
# 1、dict内部的存放顺序和key放入的顺序是没有关系的
# 2、查找和插入的速度极快，不会随着key的增加而变慢
# 3、需要占用大量的内存，内存浪费多
# 跟dict相比，list的特点：
# 1、查找和插入的时间随着元素的增加而增加
# 2、占用空间小，浪费内存很少

a = {'michael': 98, 'bob': 97, 'tarcy':96}
print(a)
print(a['michael'])
# 字典能够快速找到的原因是，键组成了索引表，通过索引表可以快速找出值

# 把数据放入dict的方法，1、初始化时写入；2、通过key放入：
a['zeng'] = 100
a['bob'] = 99
print(a)

# 查找的时候，如果键不存，dict就会报错
# print(a['jian'])

# 要避免key不存在的错误，有两种办法
# 方法一： 通过 in 判断key是否存在
b = 'zeng' in a
print('zeng is', b)
c = 'jian' in a
print('jian is', c)
# 方法二： 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
# 注意：返回None的时候，python的交互环境不显示结果
print('zeng is', a.get('zeng'))
print('zeng is', a.get('zeng', -1))
print('jian is', a.get('jian', -1))
print('jian is', a.get('jian'))

# 要删除一个key, 用pop(key)函数，对应的value也会从dict中删除：
print(a.pop('bob'))
print(a)

# set和dict类似，也是一组key的集合，但不存储value，由于key不能重复，所以，在set中，没有重复的key。
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s)
# 传入的参数[1,2,3]是个list，在set内是没有顺序的。而且重复的元素会被自动过滤掉
s = set([1, 1, 2, 3, 4, 3])
print(s)

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(5)
print(s)

# 通过remove(key)方法，可以删除元素
s.remove(1)
print(s)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1,2,3])
s2 = set([3,4,5])
print(s1 & s2)
print(s1 | s2)

