# functions
# Алладин -> лампа -> Джин -> исполнял 3 желания -> возвращался в лампу
# global_mainspace - главная область - эта та область где мы писали код в данный момент
# Функция = Лампа -> Джин
# реализация функции = исполнял 3 желания
# функция - это инструкция или набор команд который будет выполнена
# def show_lst():
#     for elem in lst:
#         print(elem)
#
# lst = [4, 2, 5, 1, 2, 52]
#
# show_lst()
# def pancakes():
#     print("Взять ингредиенты (соль, мука, яйца, молоко")
#     print("Мешаем")
#     for i in range(5):
#         print(f"порция {i + 1} готова")
#         fried()
# def fried():
#     print("Берём смесь и наливаем на сковородку")
#     print("ждём 5 минут")
#     print("перевернём")
#     print("ждём 2 минуты")
#     print("Выложить на тарелку и смазать маслом")
#
#
# pancakes()
# def register(name, age):
#     print(f"Greeting {name} {age}")
# register(name = "Oleg", age = 25)
# global scope
# Если тип данных переменной неизменяемый - мы не можем изменить её в локальной области
# name = "Vova"
# def greeting(name: str, age: int):
    # процедура - функция которая ничего не возвращает
    # local scope
    # name = "John"
    # print(f"Hello World {name}, {age}")
# greeting('John', 28)
# неизменяемые данные передаются в функции по значению unmutable
# изменяемые данные передаются в функции по ссылке mutable
# people = ['Karl', 'Vasya', 'Petya']
# def workers():
#     people.append('Anna')
#     print(people)
# workers()
# *args - позиционные аргументы, можно называть любой переменной, главное, чтобы была звёздочка
# balance=100 - аргументы переданные по ключи
# **kwargs - key word arguments - аргументы которые мы принимаем в виде ключевых слов (ключ - слово)
# def workers(date, *args, balance, balance_many=1000, **kwargs):
#     print(date)
#     print(balance)
#     print(args)
#     print(kwargs)
#     print(balance_many)
# workers('06.07.2021', 'Vasya','Petya','Anna', balance=100, balance1 = 421, balance2 = 412, balance3 = 411, balance_many= 998)
# def fun(*args, **kwargs):

# анонимные функции

# fun = lambda x, y: x+y


# def fun_2(x,y):
#     return x+y
#
# print(fun_2(2,1))
# print(fun(5,2))
# def chet(number):
#     return not number % 2
#
# lst = [5,2,6,1,7,8]
# lst.sort(key=chet,reverse=True)
# print(lst)

# lambda возвращает значение без return

# lst = [5,2,6,1,7,8]
# lst.sort(key=lambda numb: not numb % 2)
# print(lst)

# kr = lambda x: True if x % 3 == 0 else False
# lst = ["John", "Mar", "Jack", "Willy"]
# lst.sort(key=lambda x: len(x))
# print(lst)

# kr = lambda x: True if x % 3 == 0 else False
# lst = ["John", "Mar", "Jack", "Willy"]
# lst.sort(key=lambda x: x[-1])
# print(lst)

# map

# balance = {"John": 231, "Mark": 199, "Anna": 120}
# for name in map(lambda name: balance[name] + 20 if balance[name] < 200 else balance[name], balance):
#     print(name, balance[name])

# filter
# lst = [5, 2, 6, 1, 6, 7, 1]
# lst_2 = list(filter(lambda x: not x % 2, lst))
# print(lst_2)



# lst = [5, 2, 6, 1, 6, 7, 1]
# lst_2 = list(filter(lambda x: not x % 2, lst))
# words = ["hello", "world", "price", "gold"]
# words2 = list(filter(lambda w: len([sym for sym in w if sym in "aeyuio"]) == 2, words))
# print(words2)

# В функцию можно передать функцию

# x = 2
# def fun():
#    global x
#    x += 3
#    print(x)
# fun()
# print(x)
# global local nonlocal built-in

# def fun(numb):
#     numb += 1
#     def wrapper():
#         nonlocal numb
#         numb += 1
#         print(numb)
#     wrapper()
# fun(42)

#  сlosure

# def person(name):
#     def wrapper():
#         print(name.capitalize())
#     return wrapper
# p = person("Оледжик")
# p()
# p()
# p()
# def counter(x):
#     def wrapper(a): # запоминаем верхнюю строчку
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper

# c = counter(0)
# c(1)
# c(1)
# c(1)
# c(1)

# def counter(x):
#     def wrapper(a): # запоминаем верхнюю строчку
#         nonlocal x
#         x += a
#         print(x)
#     return wrapper
#
# c = counter(0)
# c(1)
# c(1)
# c(1)
# c(1)
# def counter_2(x):
#     return x + 1
#
# print(counter_2(1))
# print(counter_2(1))
# print(counter_2(1))
# print(counter_2(1))

# декоратор - это функция, которая принимает функцию, её же модернизирует и возвращает

# def greeting(name: str):
#     return "Hello " + name
#
# def decorator(fun):
#     def wrapper(name:str):
#         if name.capitalize() == name:
#             return fun(name)
#         else:
#             return 'hello ' + name.capitalize()
#     return wrapper
# decor_gr = decorator(greeting)
# print(decor_gr('peter'))
# users = {"John": 1000,"Jack": 1500, "Anna": 900}
# def balance(**kwargs):
#     for name, salary in kwargs.items():
#         if salary < 1000:
#             kwargs[name] += 100
#     return kwargs
# users = balance(**users)
# print(users)




