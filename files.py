"""
Файлы
Текстовый(закодированные символы) и бинарные(хранят информацию в 1 и 0) файлы

Режимы доступа:

w - write - запись - всё, что было в файле, оно стирается
r - read - чтение - мы считываем всё из файла
a - append - дозаписать - записывает в конец файла
x - запишет в файл информацию, если файла не существовало - создаст файл, если он пустой или его не существует

readline - считывает строчку
for line in file:
    print(line.rstrip())

Контекстный менеджер

enter - вход, exit - выход

csv file - comma separed values - набор данных, разделённые запятой(могут разделяться любим разделителем)

json file - текстовый формат обмена данными, основанный на JavaScript - к
"""
# w+ r+ a+ x+ wb rb ab xb
# file = open("матрица.txt", "r", encoding="windows-1251")
# some_str = file.read()
# file.close()
# lst = some_str.replace('\n'," ").rstrip().split()
# lst = list(map(int, lst))
# print(lst)



# file = open("C:/Users/Егор/Desktop/cтуденты.txt", "r", encoding="UTF-8")
# students = {}
# for line in file:
#     lst = line.rstrip().split()
#     marks = list(map(int, lst[1:]))
#     students[lst[0]] = marks
# print(students)
#
# file_avg = open("C:/Users/Егор/Desktop/cтуденты.txt", "r", encoding="UTF-8")
# for name, marks in students.items():
#    file_avg.write(name + " " + str(sum(marks) / 5) + "\n")
# file_avg.close()



# with open("test_file.txt", "r", encoding="UTF-8") as file:
#     lst = []
#     for line in file:
#         lst.extend(line.rstrip().split())



# max_len = 0
# number = 1
# s = " "
# for id, line in enumerate(lst):
#     if len(line) > max_len:
#         max_len = len(line)
#         s = line
#         number = id + 1
# print(s)
# print(max_len)
# print(number)
# import json
# person = {
#     "name" : "John",
#     "lastname" : "Watson",
#     "age": 24,
# }
# # сериализирует объект
#
# with open("test_json.json", "w", encoding="UTF-8") as file_json:
#     # сериализирует объект
#     json.dump(person, file_json)
#
# with open("test_json.json", "r", encoding="UTF-8") as file_json_read:
#     person2 = json.load(file_json_read)
#
#     print(person2)
