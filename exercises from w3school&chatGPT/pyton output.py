# Вправа 1: Персональне привітання
#
# Завдання:
# Запитай у користувача його ім’я та стать і привітай його по-особливому.

name = input("Як тебе звати? ")
gender = input("Are you man or woman? ")

if gender == "man":
    print(f"Привіт, {name}! You are handsome")
elif gender == "woman":
    print(f"Привіт, {name}! You are beautiful")
else:
    print(f"Привіт, {name}! Putin khujlo!")

# Вправа 2: Перевірка числа
#
# Завдання:
# Користувач вводить число. Програма визначає, чи воно додатнє, від’ємне чи нуль.

num=float(input("Enter number:"))
if num>0:
  print("positive")
elif num<0:
  print("negative")
else:
  print("zero")

# Вправа 3: Таблиця множення
#
# Завдання:
# Введи число n, і програма має вивести таблицю множення для нього від 1 до 10.

n = int(input("Введи число: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
