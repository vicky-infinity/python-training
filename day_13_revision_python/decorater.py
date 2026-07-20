import time

def decorater(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func_result = func(*args, **kwargs)
        endt = time.time()
        ex_time = endt - start
        print(ex_time)
        return func_result
    return wrapper



@decorater
def fun1():
    time.sleep(3)
    a = 2
    return a

@decorater
def fun2():
    time.sleep(1)
    r = 2
    return r

print(fun1())
print(fun2())