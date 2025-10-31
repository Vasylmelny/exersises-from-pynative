# Вправа 1: Визнач тип даних
#
# Завдання:
# Створи кілька змінних різних типів і виведи їх типи за допомогою функції type().

a = 10          # int
b = 3.14        # float
c = "Python"    # str
d = True        # bool

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Вправа 2: Перетворення типів
#
# Завдання:
# Користувач вводить число як рядок. Перетвори його в число та виконай математичну операцію.

a=input("Enter number: ")
a=int(a)
b=input("Enter number: ")
b=int(b)
sum=a+b
print(sum)

# Вправа 3: Список у дії
#
# Завдання:
# Створи список чисел і обчисли:
#
# суму елементів,
#
# середнє значення,
#
# найбільше та найменше число.

numbers = [4, 7, 2, 9, 5]
sum=0
for i in range (len(numbers)):
    sum+=numbers[i]


print("Список:", numbers)
print("Сума:", sum)
print("Середнє:", sum / len(numbers))
print("Максимум:", max(numbers))
print("Мінімум:", min(numbers))

