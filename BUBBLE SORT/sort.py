



# bubble sort.


arr = [9, 7, 3, 1, 8, 4, 12, 6]
n = len(arr)
for i in range(n - 1):
    for j in range(n-i-1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
print(arr)



# selection sort


arr = [9, 7, 3, 1, 8, 4, 12, 6]
n = len(arr)
for i in range(n - 1):
    min_idx = i
    for j in range(i+1,n):
        if arr[j] < arr[min_idx]:
            min_idx = j
    temp = arr[i]
    arr[i] = arr[min_idx]
    arr[min_idx] = temp
print(arr)


# insertion sort 



list1=[6,2,1,9,4]
n=len(list1)
for i in range(1,n):
    key=list1[i]
    j=i-1
    while j>=0 and key<list1[j]:
        list1[j+1]=list1[j]
        j=j-1
    list1[j+1]=key
print(list1)
