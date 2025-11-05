# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.

def first_last_same(lis):
    print("Given list:", lis)
    print(lis[0]==lis[-1])

numbers_x = [10, 20, 30, 40, 24]
first_last_same(numbers_x)

# def first_last_same(numberList):
#     print("Given list:", numberList)
#
#     first_num = numberList[0]
#     last_num = numberList[-1]
#
#     if first_num == last_num:
#         return True
#     else:
#         return False
#
# numbers_x = [10, 20, 30, 40, 10]
# print("result is", first_last_same(numbers_x))
