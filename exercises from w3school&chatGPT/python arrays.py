# В Python немає окремого типу arrays як у Java чи C++, але зазвичай під “масивами” мають на увазі списки (lists).
# Ось 3 вправи на тему array/list:
#
# Вправа 1 — Знайти найбільший елемент масиву
# Завдання:
# Дано масив чисел:
#
# numbers = [12, 5, 43, 7, 29]
# Знайди та виведи найбільше число.
#
# Очікуваний результат:
#
# 43

numbers = [12, 5, 43, 7, 29]
max=numbers[0]
for i in range(1,len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
print(max)

# Вправа 2 — Додати елемент у масив і вивести оновлений список
# Завдання:
# Є список:
#
# fruits = ["apple", "banana", "orange"]
# Додай у список слово "kiwi" і надрукуй результат.
#
# Очікуваний результат:
#
# ["apple", "banana", "orange", "kiwi"]

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)

# Вправа 3 — Порахувати скільки разів елемент зустрічається у масиві
# Завдання:
# Є масив:
#
# colors = ["red", "blue", "red", "green", "red"]
# Порахуй, скільки разів "red" зустрічається у списку.
#
# Очікуваний результат:
#
# 3

colors = ["red", "green", "red", "blue", "red"]
counter = 0
for color in colors:
    if color == "red":
        counter += 1
print(counter)