# python函数的参数非常的灵活，除了正常定义的必选参数外，还可以使用默认参数，可变参数和关键字参数

# 位置参数（必选参数 ）
# def a(x):
#     return x * x
# print(a(5))

# def a(x, n):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
# print(a(5, 3))

# 上面的a(x, n)函数定义的没有问题，但是，旧的调用代码失效了，原因是我们增加了一个参数，导致旧的代码因为确实一个参数而无法正常调用：

# 默认参数
def a(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(a(5))
print(a(5, 3))


