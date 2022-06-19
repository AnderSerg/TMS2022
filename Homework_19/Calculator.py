def add(args):
    var_sum = 0
    for val1 in args:
        var_sum += val1
    return var_sum


def multiply(a, b):
    return a*b


def subtract(a, b):
    return a-b


def divide(a, b):
    if b != 0:
        return a/b

