# Write a code to return True if the list’s first and last
# numbers are the same. If the numbers are different, return False.

arr1 = [1,2,3,4,5]
arr2 = [4,5,6,4]

def first_last_same(arr):
    print("Given list:", arr)
    print("First element:", arr[0])
    print("Last element:", arr[-1])
    return arr[0] == arr[-1]

print(first_last_same(arr1))
print(first_last_same(arr2))