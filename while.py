# range(start,stop,step)
# for number in range(1, 12, 1):
#     if number % 2 == 0:
#         print(number, end=' ')
# count_dish = 0
# answer = input("Input are there dishes(yes/no):")
# while answer == 'yes':
#     print('we take dishes, wash up, dry')
#     answer = input("Input are there dishes(yes/no):")
#     count_dish += 1
# print('we washed up', count_dish)
# if count_dish != 0:
#     print('take a rest after washing dishes')
# else:
#     print('our dishes was washed up by somebody')

#while True - бесконечный цикл

# count_dish = 0
# while True:
#     answer = input("Input are there dishes(yes/no):")
#     if answer == 'no':
#         break
# #break досрочно прерывает цикл
#     print('we take dishes, wash up, dry')
#     count_dish += 1
#     print('we washed up', count_dish)
# if count_dish != 0:
#     print('take a rest after washing dishes')
# else:
#     print('our dishes was washed up by somebody')
# n = int(input())
#begin = 1
# while begin < n:
#    print(begin, end=" ")
#    begin = begin + 1
#print("сycle is finished")
# begin = 1
# n = int(input())
# for i in range(begin, n + 1, 1):
#     print(i, end=" ")

#статистика рождаемости

# stat = int(input())
# count_babies = 0
# while stat > 0:
#     count_babies += stat
#     stat = int(input())
# print(count_babies)

# count_babies = 0
# while True:
#     stat = int(input("Input the number of newborns this day"))
#     if stat == 0:
#         break
#     count_babies += stat
# print("the number of newborns", count_babies)

# count_babies = 0
# count_days = 0
# while True:
#     stat = int(input("Input the number of newborns this day"))
#     if stat == 0:
#         break
#     if stat > 10:
#         continue
#     count_babies += stat
#     count_days += 1
# print(count_babies)
# print(count_days)

# number = int(input())
# while number != 0:
#     n = number % 10
#     print(n)
#     number = number // 10
# number = int(input())
# number = str(number)[::-1]
# number = int(number)
# while number != 0:
#     n = number % 10
#     print(n)
#     number = number // 10
# number = input()
# for n in number:
#     print(n)
# s = "hello"
# s = s.upper()
# print(s)
# s = 'hello world'
# temp = ""
# for ind in range(len(s)):
#     if ind == len(s) - 2:
#         temp += s[ind].upper()
#         continue
#     temp += s[ind]
#     print(ind)
# print(temp)
# задача на поиск гласных
# s = 'hello world'
# temp = ""
# for ind in range(len(s)):
#    gl = 'aeyuioOAEYUIO'
#   if s[ind] not in gl:
#        temp += s[ind]
# print(temp)

#задача на пробелы

# text = "dog    cat    frog     mouse  "
# temp = ""
# for ind in range(len(text)):
#     if text[ind] != " ":
#         temp += text[ind]
#     elif temp != "": # если строка существует - т.е не пустая
#         print(temp)
#         temp = ""
# text = "  dog frog mouse   horse"
# temp = ''
# letter = 'o'
# count = 0
# for ind in range(len(text)):
#     if text[ind] != ' ':
#         temp += text[ind]
#     elif temp:
#         if letter in temp:
#             print(temp)
#             count += 1
#         temp = ''
# print(count)
# name = "John"
# age = 45
# print('name:', name, 'age:', age)
# # форматирование строки
# print

