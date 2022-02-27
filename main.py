# print("Hello")
#
# fname = 'Matvei'
# lname = 'Skrigalovski'
#
# print(fname , lname)
#
# input('Нажмите Enter')

# a = input('Введите свое имя: ')
# b = int(input('ведите ваш возраст: '))
#
# print(type(a)
# print(type(b)

# print("\ta")

# print('''"Тут что-то не так, не будь я д'Артаньян"-подумал он."''')

# in
# True=0 False=1
# s = 10, 20, 30
# x = 5
# print(x in s)

# list (список) -> [], изменяемый
# tuple (кортеж) ->, неизменяемый"""

# string = "Всем привет, я люблю python!"
#
# print(f'Исходная фраза: {string}')

# print(f'\nКогда я кричу: {string.upper()}')
#
# print(f'\nКогда я кричу: {string.lower()}')
#
# print(f'\nС заглавных букв: {string.title()}')
#
# print(f'\nС заменой: {string.replace("ЛЮБЛЮ", "ОБОЖАЮ")}')
#
# input('Введите Enter для завершения')

# string = 'matvei', 'skrigalovski', 20
# # print(string[0])
# # print(string[1])
# # print(string[2])
#
#
# print(string[-1])
# print(string[-2])
# print(string[-3])


string = 'matvei'
print(string[0:3+1])
print(string[-1])

string = 'Сидел барсук в своей норе и ел картошочку пюре'
a = '!'
c = 'ре'

print(len(string))
print(string + a)

if c in string:
    print('ре есть!')
else:
    print(f'{c} нет!')


"""Цикл for функция range"""

# numbers = 1, 2, 3, 4
#
# for i in numbers:
#     print(i)

# for i in range(1, 2):
#     print(i)

# numbers = 2, 4, 6, 8, 10
#
# for i in numbers:
#     print(i)
#
# Start = int(input('Введите начальное число последовательности:'))
# Stop = int(input('Введите конечное число последовательности:'))
#
# for number in range(Stop, Start, -1):
#     if number % 5 == 0:
#         if number % 10 == 0:
#             continue
#         print(number)

#
# string = 'Пртивет Андрей!'
#
# for i in  string:
#     print(i)

# for i in range(0, 7):
#     if i == 3 or i == 6:
#         continue
#     print(i)

# start = int(input('Введдите начало последовательности:'))
# stop = int(input('Введдите конец последовательности:'))
#
# otr = 0
# pol = 0
#
# for number in range(start, stop):
#     if number < 0:
#         otr += number
#     else:
#         pol += number
#
# print(f'Сумма положительных чисел: {pol}')
# print(f'Сумма отрецательных чисел: {otr}')

# a = 10
# b = 20
#
# c = (a+b)//2
# print(c)


# start = int(input('Введдите начало последовательности:'))
# stop = int(input('Введдите конец последовательности:'))
#
# quantity = 0
# sum_of_number = 0
#
# for number in range(start, stop):
#     sum_of_number += number
#     quantity += 1
# final = sum_of_number // quantity
# print(f'Среднее фрифметическое последовательности от {start} до {stop}:{final}')

# number_of_string = 1
#
# for i in range(1, 6):
#     print(f'Строка {number_of_string} 0')
#     number_of_string += 1
#
# n = int(input('Введите число: '))
#
# for i in range(1, n+1):
#     if n > 7:
#         break
#     if i == 1:
#         print('Красный')
#     if i == 2:
#         print('Оранжевый')
#     if i == 3:
#         print('Желтый')
#     if i == 4:
#         print('Зеленый')
#     if i == 5:
#         print('Голубой')
#     if i == 6:
#         print('Синий')
#     if i == 7:
#         print('Фиолетовый')
#
#     if n > 7 or n < 1:
#         print('Радуга состоит только из 7 цветов')


a = int(input('Введите натуральное число: '))

# if a == 4:
#     print(f'{4} * 1 = {4 * 1}')
#     print(f'{4} * 2 = {4 * 2}')
#     print(f'{4} * 3 = {4 * 3}')
#     print(f'{4} * 4 = {4 * 4}')
#     print(f'{4} * 5 = {4 * 5}')
#     print(f'{4} * 6 = {4 * 6}')
#     print(f'{4} * 7 = {4 * 7}')
#     print(f'{4} * 8 = {4 * 8}')
#     print(f'{4} * 9 = {4 * 9}')
#     print(f'{4} * 10 = {4 * 10}')


# for i in range(1, 11):
#     print(f'{a} * {i} = {n * i}')
#
# a = [[0, 1],
#
# for i in a:
#     print(i)
#     for j in a:
#         print(j)
names = ['Artem', 'Nikita', 'Steve', 'Jhon']
surnames = ['Troshkin', 'Ivanov', 'Ivanov', 'Petrov']

print(names * surnames)


# names[2] = 'vlad'
# print(names)

names.append('Irina')
print(names)

names.remove('Jhon')
print(names)

del names[0]

names.pop()
print(names)



if 'Nikita' in names:
    print('Никита на месте!')
if 'Ann' not in names:
    print('Анна отсутствует!')


index = names.index(20)
print(index)


list_2 = [i for i in range(1, 10)]

print(list_2)


list_3 = [1, 5, 4, 2, 8, 7]
# list_3.sort()
# print(list_3)

list_4 = [int(number) for number in input().split()]
print(list_4)


list_5 = [i for i in range(800)]


if 777 in list_5:
    var = True
    print(var)
else:
    var = False
    print(var)
