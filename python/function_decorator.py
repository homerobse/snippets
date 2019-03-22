# a good tutorial https://realpython.com/primer-on-python-decorators/

def func_decorator(func):
    def func_wrapper(*args, **kwargs):
        print('do this before')
        res = func(*args, **kwargs)
        print('do this after') # or check this example https://stackoverflow.com/a/38453402/1273751
        return res

    return func_wrapper

@func_decorator
def f(x):
    return 3*x

print(f(2))

def func_decorator_with_param(y):
    def func_decorator(func):
        def func_wrapper(*args, **kwargs):
            print('do this before. Param: ', str(y))
            res = func(*args, **kwargs)
            print('do this after') # or check this example https://stackoverflow.com/a/38453402/1273751
            return res
        return func_wrapper
    return func_decorator

@func_decorator_with_param(13)
def g(x):
    return 3*x

print(g(5))