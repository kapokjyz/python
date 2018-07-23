# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2018.07.23')
f = now
f()

# 函数对象有一个 __name__ 属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)

# 假设我们要增强 now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）
# 本质上，decorator就是一个返回函数的高阶函数，所以，我们要定义一个能打印日志的 decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' %func.__name__)
        return func(*args, **kw)
    return wrapper
# 上面的log函数，因为它是一个decorator，所以接收一个函数作为参数，并返回一个函数。我们借助python语法 @ , 把decorator置于定义处
@log
def now_1():
    print('2018-07-23')
now_1()
# 调用 now_1() 函数，不仅会运行 now_1() 本身，还会运行 now_1() 函数前打印一行日志

# 如果decorator 本身需要传入参数，那就需要编写一个返回decorator 的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log_1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s()' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator
@log_1('zengjian')
def now_2():
    print('2018-07-23 19:15:00')
now_2()

# 和两层嵌套的decorator 相比，3层嵌套的效果是这样的：
# now = log_2('zengjian')(now_2)
# 解释下上面的一行：首先执行 log_2('zengjian'),返回的是decorator 函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数
print(now_2.__name__)