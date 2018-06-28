# 循环的使用

# for x in y 就是把y中的每个元素一次代入变量x，然后执行
color = ['white', 'black', 'blue']
for n in color:
    print(n)

sum = 0
for x in [1,2,3,4,5]:
    sum = sum + x
print(sum)

# range()函数可以生成一个整数序列，然后可以通过list()函数生成一个list列表，比如rang(5),生成的序列是 0--4
print(list(range(5)))

sum = 0
for x in range(101):
    sum = sum + x
print(sum)


# while x: 只要x为真，就不断循环执行，反之停止
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

# break语句会提前结束循环
# continue语句会跳过本次循环
