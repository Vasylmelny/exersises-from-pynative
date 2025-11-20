# Write a Python code to display numbers from a list divisible by 5

list1 = [2, 3 , 45, 60, 199, 100, 0, 67]

def div5(list):
    lst = []
    for num in list:
        if num % 5 == 0:
            lst.append(num)
    return lst

print(div5(list1))