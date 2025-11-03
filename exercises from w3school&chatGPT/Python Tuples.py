# Вправа 1: Основи роботи з кортежами
#
# Завдання:
# Створи кортеж з 5 довільних чисел.
#
# Виведи перший і останній елемент.
#
# Обчисли суму всіх елементів.
#
# Перевір, чи є число 10 у цьому кортежі.
#
# my_tuple = (2, 5, 8, 3, 2)
# sum=0
# for i in my_tuple:
#     sum = sum + my_tuple[i]
# print(sum)
# bulka=False
# while bulka==False:
# for x in my_tuple:
#     if my_tuple[x]==10:
#         bulka=True
# print(bulka)

numbers = (3, 7, 10, 2, 5)
print(numbers[0]) # перший елемент
print(numbers[-1]) # останній елемент
print(sum(numbers)) # сума
print(10 in numbers) # перевірка наявності

# Вправа 2: Розпаковка кортежів
#
# Завдання:
# Є кортеж, який містить дані про користувача:
#
# user = ("Ivan", "Ivanov", 25)
#
#
# Розпакуй його в змінні name, surname, age
# і виведи речення:
#
# "Мене звати Ivan Ivanov, мені 25 років."
#
user = ("Ivan", "Ivanchuk", 25)
name = user[0]
surname = user[1]
age = user[2]
print(f"My name is {name} {surname}. I have {age} years old.")

# Підказка:
#
# name, surname, age = user
# print(f"Мене звати {name} {surname}, мені {age} років.")

# Вправа 3 — Операції з кортежами
# Завдання:
#
# Створи два кортежі:
#
# a = (1, 2, 3)
# b = (4, 5, 6)
# Об’єднай їх в один кортеж.
#
# Виведи кортеж у зворотному порядку.
#
# Знайди суму всіх елементів.

a = (1, 2, 3)
b = (4, 5, 6)
c = a + b
print("Об'єднаний кортеж:", c)
print("Зворотній порядок:", c[::-1])
print("Сума елементів:", sum(c))