"""Homework for 12.05.2022"""

var = lambda x=int(input('введите число\n')): print('чётное') if x % 2 == 0 else print('нечётное')
var()

print()

array = [1, 2, 3, 4]
array = list(map(lambda x: str(x), array))
print(array)

print()

word = ("cat", "rewire", "level", "book", "stats", "list")
palindromes = tuple(filter(lambda word: word == word[::-1], word))
print("Слова палиндромы: ", tuple(palindromes))

print()


def benchmark(func):
    import time

    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end - start))

    return wrapper


@benchmark
def test_func():
    a = int(input("Введите число\n"))
    while a < 1000:
        a += 1
        print(a)


@benchmark
def test_func_1():
    x = 0
    while x != 99:
        x = int(input("Введите число 99\n"))


test_func_1()

print()

test_func()

print()
