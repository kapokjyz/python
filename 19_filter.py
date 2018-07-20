# python 内建的 filter() 函数用于过滤序列;
# fitter() 把传入的函数一次作用与每个元素，然后根据返回值是True 还是 False 决定保留还是丢弃该元素
# 例如：在一个list中，删掉偶数，只保留奇数：
def is_off(n):
    return n % 2 == 1
L = list(filter(is_off, [1,2,3,4,5,6,8,9]))
print(L)

# 求出素数
# 先构造一个从3开始的奇数序列
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
# 再定义一个筛选函数
def _not_divisible(n):
    return lambda x:x % n > 0
# 定义个生成器，不断返回下一个素数：
def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
it1 = primes()
n = 1
for n in range(10):
    print(next(it1))

# 练习：回数，指的是从左向右读和从右向左读都是一样的数，例如12321,909，利用filter() 筛选出回数：
def is_palindrome(n):
    s = str(n)
    for i in range(len(s)):
        if s[i] != s[-i-1]:
            return False        
    return True
        
output = filter(is_palindrome, range(1, 200))
print(list(output))

# 利用切片的方法：
def is_palindrome_1(n):
    s = str(n)
    return s[:] == s[::-1] # [::-1] 这种切片操作表示取整个列表，并倒序显示
output = filter(is_palindrome_1, range(1, 300))
print(list(output))





