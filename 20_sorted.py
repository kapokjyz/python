# sorted() 可以对list进行排序：默认情况
L = sorted([36,5,-12,9,-33])
print(L)
# sorted() 是一个高阶函数，可以接收一个 key 函数来实现自定义的排序， 例如按绝对值大小排序：
L = sorted([36,5,-12,9,-33], key = abs)
print(L)
# key指定的函数将作用于list的每一个元素上，并根据函数返回结果进行排序。

# 对字符串的排序：默认情况下，是按照ascii的大小比较的。
L = sorted(['bob', 'Zendg', 'zzzz', 'jjjjj'])
print(L)
# 我们可以忽略大小写进行排序:实际的实现方法就是全部变成大写或者小写的，然后再进行比较。
L = sorted(['bob', 'Zendg', 'zzzz', 'jjjjj'], key = str.lower)
print(L)

# 进行反向排序的话，不必改动key函数，可以传入第三个参数 reverse = True
L = sorted(['bob', 'Zendg', 'zzzz', 'jjjjj'], key = str.lower, reverse = True)
print(L)

# 练习：一组tuple表示学生名字和成绩，使用sorted() 对上述列表分别按名字排序：
L = [('bob', 75), ('adam', 98), ('lisa', 88)]
def by_name(t):
    return t[0]
L1 = sorted(L, key = by_name)
print(L1)
def by_grade(t):
    return t[1]
L2 = sorted(L, key = by_grade)
print(L2)