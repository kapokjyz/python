# 条件判断，是自动化必不可少的部分，根据不同的情况做出不同的选择
age = 20
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# if 判断条件可以简写
# if x:
    # print('True')
# 只要x是非零数值，非空字符串，非空list等，就判断为True，否则为False

# input()函数返回的是str类型
age = input('please enter you age: ')
# 下面这样直接判断就会报错，因为str类型不能直接和整数比较，需要把str转换成整数
# if age >= 70:
age = int(age)
if age >= 70:
    print('old age')

# str类型转换成int类型时，只能是数字形式的字符串，如果是别的则不合法，会报错
