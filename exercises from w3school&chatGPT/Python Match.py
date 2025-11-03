# Вправа 1: День тижня за номером
# Завдання:
# Користувач вводить число від 1 до 7.
# Виведи, який це день тижня.
from unittest import case

day = int(input("Введи число від 1 до 7: "))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Невірне число!")

# Вправа 2: Проста калькуляція
# Завдання:
# Користувач вводить оператор (+, -, *, /), а потім два числа.
# Виконай обчислення.
#
op = input("Введи операцію (+, -, *, /): ")
a = float(input("Введи перше число: "))
b = float(input("Введи друге число: "))
match op:
    case "+":
        print(a+b)
    case "-":
        print(a-b)
    case "*":
        print(a*b)
    case "/":
        if b != 0:
            print(a/b)
        else:
            print("Ділення на нуль!")
    case _:
        print("Bad input")

# Вправа 3: Класифікація тварини
# Завдання:
# Користувач вводить назву тварини.
# Програма визначає її тип: ссавець, птах або інше.

animal = input("Введи тварину: ").lower()

match animal:
    case "кіт" | "собака" | "корова":
        print("Це ссавець")
    case "голуб" | "сова" | "курка":
        print("Це птах")
    case _:
        print("Невідомий тип тварини")