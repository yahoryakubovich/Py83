# temp / buf - временная переменная из которой можно поменять значения местами
# var1 = 1
# var2 = 4
# print(var1, var2)
# temp = var1
# var1 = var2
# var2 = temp
# print(var1, var2)

# или другой вариант в одну строчку
# var1, var2 = var2, var1
# print(var1,var2)
# логические выражения, за них отвечает boolean
# >(больше) - строгое равенство >=(больше или равно) - нестрогое равенство <(меньше) <= (меньше или равно) != (не равно) ==(равно)
# var1 = 0
# var2 = 0
# print(var1 is var2)
# and(и) - требует, чтобы два значения были верны, or(или) not(не) xor(одно или)
# print(5 == 5 and 6 != 6)
# print(5 == 5 and 6 > 13)
# print(5 == 7 or 6 > 13)
# print(5 == 7 or 6 < 13)
# print(not (5 == 7) or 6 > 13)
# print(15 % 2 == 0)
# print(18 % 2 == 0)
# number = int(input())
# if number > 0:
# #     print("positive")
# #     print(number + 2)
# # #   number += 2 - короткий вариант записи
# #     if 10 <= number and number < 100:
# #         print("двузначное")
# #     else:
# #         print("недвузначное")
# # elif number == 0:
# #     print("zero")
# # else:
# #     print("negative")
# #     print(number - 2)
# # print("end program")
# season = input('enter season of year ')
# if season == 'winter':
#     print('winter is here')
# elif season == 'autumn':
#     print('autumn is here')
# elif season == 'spring':
#     print('spring is here')
# elif season == 'summer':
#     print('summer is here')
# else:
#     print('unknown')
# a, b, c = map(int, input('enter lines of triangle: ').split())
#if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
#    if a == b == c
#       print('разносторонний')
#    elif a == b or a == c or b == c: # отсекается первым if
#        print('равнобедреннный')
#    else:
#        print('разносторонний')
#else:
#    print('не существуеt')
# строки str
#some_string = '''
#я учу пайтон
#ы
#'''
#print(some_string)
# /n - перенос курсора \t - табуляция \a - перенос курсора в начало строки
# name = 'joHn'
# name = name.capitalize()
# print(name)
# name = "akfasasf"
# print(name.islower()) - проверяет ли все буквы в нижнем регистре
# print(name.isdigit()) - проверяет все ли символы - цифры
# name = "john"
# print(name.title())
# age = "123jfs"
# if age.isdigit():
#    age = int(age)
#   print(age)
# else:
#    print('age is not a digit')
# slice (cрез) str[start:end:step] / str[start:end] - шаг по умолчанию единица str[::step]
# name = "john"
# print(name[:2] + name[5:8]
# name1 = "John"
# name2 = "Jit"
# print(name1 < name2)
# name = "John Watson"
# str1 = name[:4]
# str2 = name[5:]
# name2 = str2 + " " + str1
# print(name2)
# str = "192.168.0.1"
# print(str.replace(".", ' '))
# print(int(str[0:3]) + int(str[4:7]) + int(str[8]) + int(str[10]))





