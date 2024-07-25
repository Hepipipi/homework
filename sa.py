print('start doing homework')


def my_decorator(func):
    def start(num):
        print('start')
        res = func(num)
        print(num + 2)  # Печатаем значение num + 2
        print('end')
        return res  # Возвращаем результат функции
    return start

num1 = int(input('enter any num '))

@my_decorator
def example(num1):
    return num1

example(num1)



def helloworld(a):
    a = input('enter any word')
    print(a)

helloworld('print')





















