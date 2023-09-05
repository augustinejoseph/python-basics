# def binarySearch(arr, target):
#     middle = arr[len(arr)//2]
#     if arr(middle) == target:
#         return arr[middle]
#     else:
#         if target < middle:
#             binarySearch(arr[:middle])
#         else:
#             binarySearch(arr[middle:])
    

list_1 = [1,2,3,4,4,3,2,1,3,4,3,2]

def remove_duplicate(list_1):
    for i in range(len(list_1)-1):
        for j in range(i+1, len(list_1)-1):
            if list_1[i] == list_1[j]:
                list_1.pop(j)
    return list_1

result = remove_duplicate(list_1)
print(result)
