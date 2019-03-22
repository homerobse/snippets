def f(func, x):
    return func(x)+1

func = lambda x: 3*x

print f(func, 3)

assert f(func, 3) is 10, "3*(3)+1 should be equal to 10"
