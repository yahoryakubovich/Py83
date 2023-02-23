# numb1, numb2, numb3 = map(int, input ().split())
# counter = numb1
# if numb1 > numb2:
#     counter = numb1
# if numb2 > numb3:
#     counter = numb2
# if numb3 > numb1:
    # counter = numb3
# print(counter)
# a = int(input())
# if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
#     print("Високосный")
# else:
#     print("Не високосный")
# str_1 = input()
# print(str_1[::-1]
# s = input()
# print(s == s[::-1])
# как найти второе вхождение?
# first = str_1.find('f')
# print(str_1.find('f',first + 1))
# циклы (повторение)
# цикл с параметром (цикл перебора объектов) - for - вы знаете число повторений
# цикл с условием (цикл выполняется до тех пор пока истина) - вы моете посуду до тех пор пока нет посуды
# for (для, от) x(переменная) - отвечает за перебор чего либо in (итерируемый объект)
# for elem in range(1, 10, 1):
#     print(elem)
# for elem_1 in range(1, 5): - if step == 1 мы можем это не указывать
#     print(elem_1)
# for elem_2 in range(5):
#     print(elem_2)
# for elem in range(15, 0, -1):
#     print(type(elem),end=" ")
# s = "hello world"
# перебор по элементам
# for symb in s:
#    print(symb)
# перебор строки по индексам
# s = input()
# length = len(s)
# for ind in range(len(s)):
#     print(s[ind])
# animals = ['fox', 'dog', 'cat', 'frog']
#
# for animal in animals:
#     print(animal)
# for numb in range(1, 101):
#     if numb % 5 == 0:
#         print(numb, end=" ")
# number = int(input())
# for numb in range(1, number + 1): - чтобы включить конечное число, а т.е себя
#    if number % numb == 0:
#        print(numb, end=" ")