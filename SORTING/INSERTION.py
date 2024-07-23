

# Insertion sort works best in a nearl sorted array.
# used in in-built sort()function.

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





# Insertion Sort
# Insertion sort involves finding the right place for a given element in a sorted list. So in beginning we compare the first two elements and sort them by comparing them. Then we pick the third element and find its proper position among the previous two sorted elements. This way we gradually go on adding more elements to the already sorted list by putting them in their proper position.

# Example
# def insertion_sort(InputList):
#    for i in range(1, len(InputList)):
#       j = i-1
#       nxt_element = InputList[i]
# # Compare the current element with next one
#    while (InputList[j] > nxt_element) and (j >= 0):
#       InputList[j+1] = InputList[j]
#       j=j-1
#    InputList[j+1] = nxt_element
# list = [19,2,31,45,30,11,121,27]
# insertion_sort(list)
# print(list)
# Output
# When the above code is executed, it produces the following result −

# [19, 2, 31, 45, 30, 11, 27, 121]
