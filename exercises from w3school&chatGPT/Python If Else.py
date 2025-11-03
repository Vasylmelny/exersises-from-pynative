# Вправа 1: Перевірка парності числа
# Завдання:
# Напиши програму, яка перевіряє, чи число є парним.
# I written the program, which tests dividing nuber by 3

a=int(input("Enter your number:"))
if a%3==0:
    print("Wow!Divided!")
else:
    print("No, that's not divided")

# Вправа 2: Визначення більшого числа
# Завдання:
# Запитай у користувача два числа і виведи, яке більше.

a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
if a>b:
    print("First number is greater than second number")
elif a<b:
    print("Second number is greater than first number")
elif a==b:
    print("Second number is equal to first number")
else:
    print("Are you stupid? Enter numbers correctly")

#  Вправа 3: Перевірка оцінки
# Завдання:
# Користувач вводить оцінку (від 0 до 100).
# Програма повинна вивести, який це рівень:
#
# 90–100 → "Відмінно"
#
# 70–89 → "Добре"
#
# 50–69 → "Задовільно"
#
# Менше 50 → "Незадовільно"

mark = int(input("Enter your mark:"))
if mark < 100 and mark >= 90:
    print("Gratefull")
elif mark < 90 and mark > 69:
    print("Good")
elif mark < 70 and mark > 49:
    print("Not bad")
elif mark < 50 :
    print("Bad")
else:
    print("Mistake")