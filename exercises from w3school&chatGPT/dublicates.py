# видалення дублікатів зі списку
# 1 case

arr = [2, 3, 5, 2, 85, 2, 3]
arr1 = list(set(arr))
print(arr1)

# 2 case

arr = [2, 3, 5, 2, 85, 2, 3]
arr2 = []
for i in arr:
    while (i not in arr2):
        arr2.append(i)
print(arr2)

# 3 case

arr = [2, 3, 5, 2, 85, 2, 3]
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[j] == arr[i]:
            arr.pop(j)
        else:
            j += 1
    i += 1

print(arr)

# 4 case

arr = [2, 3, 5, 2, 85, 2, 3]
arr = list(dict.fromkeys(arr))
print(arr)
