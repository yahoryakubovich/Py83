# взаимно простые числа = числа с НОД = 1 (4, 5); (12, 29); (15, 16)
# n, m = map(int, input("enter 'n, m': ").split())
# for numb in range(2, m+1):
#     temp_numb = numb
#     temp_n = n
#     while temp_numb != 0 and temp_n != 0:
#         if temp_numb > temp_n:
#             temp_numb =- temp_n
#         else:
#             temp_n =- temp_numb
#     if temp_n + temp_numb == 1:
#         print(f"{numb} is simple with {n}")
# turple(кортежи)
#       -5     -4   -3  -2     -1
#       0      1    2    3     4
# tup = ("str", 54, True, 5.23, 54)
# print(tup[1:4])
# кортеж неизменяем, если мы хотим преобразование кортеж, берём срез кортеза и создаём новую переменную
# нельзя изменить элемент кортежа
# можно перебрать кортеж по элементам

#найти максимальное значение кортежа

# tup = (5, 6, 1, 10, 18)
# max_el = tup[0]
# for element in tup:
#     if element > max_el:
#         max_el = element
# print(max_el)

# list (список) = изменяемые = mutable
# в список можно загружать любые элементы, зачастую элементы имеют один тип данных, в списке существует индексация
# lst = [5, 2.42, "hello", True, (6,1,2), [5,2,9]]
# tup = (5, 2.42, "hello", True, (6,1,2), [5,2,9])
# lst[0] = 1
# print(lst)
# lst += (5, 2, 6)
# lst += "hello"
# print(lst)

# элементы распаковаются

# lst = [5, 2.42, "hello", True, (6,1,2), [5,2,9]]
# lst.append([2,4,5])
# print(lst)
# lst.insert(1, 5) - указываем индекс позиции
# print(lst)

# lst = [5, 2.42, "hello", True, (6,1,2), [5,2,9]]
# lst.remove(5) - удаляет первый который найдёт
# print(lst)
# while 5 in lst:
#     lst.remove(5)
#     print(lst)
# lst = [5, 2.42, "hello", True, (6,1,2), [5,2,9]]
# lst.pop() если указать индекс - удалит по индексу
# # print(lst)

# проверка
# if 15 in lst:
#   lst.remove(15)
# del lst[2:5] - может удалять срез, последовательность элементов

# print(lst[1:5])

# lst.clear() - делает список пустым

# print(lst.index(5, 0, 7)) - первое вхождение

# print(lst.count(52)) - поиск количества вхождений

# lst.extend([5,2,5])
# lst += [5,2,5]
# print(lst)

# lst2 = lst.copy()
# lst2 = lst[:] - полноповерхностный срез
# lst = list(stroka) - делаем список из строки
# lst = []
# n = int(input("enter count of elem: "))
# for i in range(n):
#     elem = int(input())
#     lst.append(elem)
# print(lst)
# list comprehension - генератор сборщик списков
#1 [что хотим добавить for из чего хотим добавить in итерабельный объект]
# lst = [numb for numb in range(1, 11)])
# lst.append(6)
# lst = [numb.upper for numb in "hello world"]
#2 [что хотим добавить for из чего хотим добавить in итерабельный объект if условие верно]
# lst = [numb for numb in range(1,11) if numb**2 % 3 == 0]
# print([symb for symb in "Hello" if symb in "AEYUIOaeyuo"])
#3 [что хотим добавить if = true else что хотим добавить for  из чего хотим добавить in итерабельном объектe]
# print([numb if numb % 2 == 0 else numb ** 2 for numb in range(1, 11)])
# print([int(input()) for i in range (5)])
# print([int(i) for i in input().split()])
# s = "hello world i am Piter Parker"
# lst = s.split()
# lst2 = [elem for elem in lst if elem[0].islower()]
# s = " ".join(lst2)
# print(s)
s = "hellp wrold"
s = s.is




