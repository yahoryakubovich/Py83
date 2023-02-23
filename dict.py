# s = input()
# lst = s.split(' ')
# count = 0
# for elem in lst:
#     if elem[-1] == 'k':
#         count += 1
# print(count)

# s = 'sd kadsfkadsfk  ksdf kasdksad k kfdsak akaf dskkd ask ' + ' '
# temp = ''
# count = 0
# for ind in range(len(s)):
#     if s[ind] != " ":
#         temp += s[ind]
#     elif temp:
#         if temp [-1] == "k":
#             count+= 1
#         temp = ""
# print(count)
# s = 'sd kadsfkadsfk  ksdf kasdksad k kfdsak akaf dskkd ask ' + ' '
# temp = ""
# count = 0
# for ind in range(len(s)):
#     if s[ind] == "k" and s[ind+1] == ' ':
#         count+= 1
# print(count)


# # lst = [int(i) for i in input().split()]
# # lst2 = []
# # if len(lst) == 1:
# #    print(lst)
# else:
#     for i in range(len(lst)):
#         if i == 0:
#             lst2.append(lst[-1] + lst[1])
#         elif i == len(lst) - 1:
#             lst2.append(lst[-2] + lst[0])
#         else:
#             lst2.append(lst[i - 1] + lst[i + 1])
#     print(lst2)


# for ind,elem in enumerate(lst1):
#     print(ind, elem)

# for ind in range(len(lst1)):
#     if lst1[ind] not in lst2:
#         lst2.append(lst1[ind])
# print(len(lst2))

# count = 1
# for ind, elem in enumerate(lst1):
#     if elem < lst1[ind + 1] and ind < len(lst1) - 1:
#         count+= 1
# print(count)
#
# count = 1
# for i in range(len(lst1)-1):
#     if lst1[i] < lst1[i+1]:
#         count += 1
# if lst1[-2] < lst1[-1]:
#     count += 1
# print(count)

# count = 1
# ind = 0
# while ind < len(lst1):
#     if ind == len(lst1)-2:
#         if lst1[ind] < lst1[ind + 1]:
#             count += 1
#         break
#     if lst1[ind] < lst1[ind+1]:
#         count += 1
#     ind += 1
# print(count)

# number = int(input())
# summa = 0
# count = 0
# while number != 0:
#     summa += number
#     count += 1
#     number = int(input())
#     if number > 10:
#         break
# else:
#     print(count)
# print(summa)
# set_1 = set([5,6,2,3,1,2])
# set_1.update([9,7,8])
# for elem in set_1:
#     print(set_1)
#
# set_1 = {1,2,6,7,9}
# set_2 = {2,3,6,7,11}
# # set_1.update(set_2)
# # print(set_1)
# print(set_1.symmetric_difference(set_2))

# lst = [5,2,6,1,2,5,2]
# lst_2 = [5,2,5,1,2,9]
# set1 = set(lst)
# set2 = set(lst_2)
# print(set1.symmetric_difference(set2))

# словари dict (key: value) ассоциативный массив
friend_phones = {"Vasya": 4131231123, "Anna": 12124124124, "pavel": 1241412421}
# for friend in friend_phones:
#     print(friend)
#     выводим ключи
# for friend, phone in friend_phones.items():
#   print(friend,phone)
