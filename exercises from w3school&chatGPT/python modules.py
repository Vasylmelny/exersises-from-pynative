# Вправа 1 — Створити власний модуль і використати його
# Завдання:
#
# Створи файл math_utils.py
#
# Додай у нього функцію square(x) → повертає квадрат числа
#
# У головному файлі імпортуй цей модуль і виклич функцію
#
#
# Приклад очікуваного результату:
# 25

import math_utils
print(math_utils.square(5))

# Вправа 2 — Використати модуль random для генерації пароля
# Завдання:
# Напиши програму, яка за допомогою random створює пароль з 8 символів:
#
# великі букви
#
# маленькі букви
#
# цифри
#
#
# Очікуваний результат (приклад):
# A8dP0kZf

import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(8))
    return password

print(generate_password())

# password = ''.join(random.choice(chars) for _ in range(8))
# Символ _ означає: нам не потрібне ім’я змінної.
#
# random.choice(chars)
# Щоразу бере випадковий символ із строки chars.
#
# ''.join(...)
# З'єднує всі символи в одну строку без пробілів.

# Вправа 3 — Робота з модулем datetime
# Завдання:
# Вивести:
#
# поточну дату
#
# поточний час
#
# день тижня
#
# Використай модуль datetime.
# Очікуваний результат (приклад):
# 2025-11-22
# 16:43:10
# Saturday

from datetime import datetime
now = datetime.now()

print(now.date())          # поточна дата
print(now.time())          # поточний час
print(now.strftime("%A"))