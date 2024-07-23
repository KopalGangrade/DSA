# selection sort example


# arr = [9, 7, 3, 1, 8, 4, 12, 6]
# n = len(arr)
# for i in range(n - 1):
#     min_idx = i
#     for j in range(i+1,n):
#         if arr[j] < arr[min_idx]:
#             min_idx = j
#     temp = arr[i]
#     arr[i] = arr[min_idx]
#     arr[min_idx] = temp
# print(arr)



# Selection Sort
# In selection sort we start by finding the minimum value in a given list and move it to a sorted list.
#  Then we repeat the process for each of the remaining elements in the unsorted list. The next 
# element entering the sorted list is compared with the existing elements and placed at its correct 
# position.So, at the end all the elements from the unsorted list are sorted.

# Example
# def selection_sort(input_list):
#    for idx in range(len(input_list)):
#       min_idx = idx
#       for j in range( idx +1, len(input_list)):
#          if input_list[min_idx] > input_list[j]:
#             min_idx = j
#       # Swap the minimum value with the compared value
#       input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]
# l = [19,2,31,45,30,11,121,27]
# selection_sort(l)
# print(l)
# Output
# When the above code is executed, it produces the following result −

# [2, 11, 19, 27, 30, 31, 45, 121]




# Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

# The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 

# How does Selection Sort Algorithm work?
# Lets consider the following array as an example: arr[] = {64, 25, 12, 22, 11}

# First pass:


# For the first position in the sorted array, the whole array is traversed from index 0 to 4 sequentially. The first position where 64 is stored presently, after traversing whole array it is clear that 11 is the lowest value.
# Thus, replace 64 with 11. After one iteration 11, which happens to be the least value in the array, tends to appear in the first position of the sorted list.
# Selection Sort Algorithm | Swapping 1st element with the minimum in array
# Selection Sort Algorithm | Swapping 1st element with the minimum in array

# Second Pass:

# For the second position, where 25 is present, again traverse the rest of the array in a sequential manner.
# After traversing, we found that 12 is the second lowest value in the array and it should appear at the second place in the array, thus swap these values.
# Selection Sort Algorithm | swapping i=1 with the next minimum element
# Selection Sort Algorithm | swapping i=1 with the next minimum element

# Third Pass:

# Now, for third place, where 25 is present again traverse the rest of the array and find the third least value present in the array.
# While traversing, 22 came out to be the third least value and it should appear at the third place in the array, thus swap 22 with element present at third position.
# Selection Sort Algorithm | swapping i=3 with the next minimum element
# Selection Sort Algorithm | swapping i=2 with the next minimum element

# Fourth pass:

# Similarly, for fourth position traverse the rest of the array and find the fourth least element in the array 
# As 25 is the 4th lowest value hence, it will place at the fourth position.
# Selection Sort Algorithm | swapping i=3 with the next minimum element
# Selection Sort Algorithm | swapping i=3 with the next minimum element

# Fifth Pass:

# At last the largest value present in the array automatically get placed at the last position in the array
# The resulted array is the sorted array.
# Selection Sort Algorithm | Required sorted array
# Selection Sort Algorithm | Required sorted array

 
# Below is the implementation of the above approach:


# # Python program for implementation of Selection
# # Sort
# import sys
# A = [64, 25, 12, 22, 11]
 
# # Traverse through all array elements
# for i in range(len(A)):
     
#     # Find the minimum element in remaining
#     # unsorted array
#     min_idx = i
#     for j in range(i+1, len(A)):
#         if A[min_idx] > A[j]:
#             min_idx = j
             
#     # Swap the found minimum element with
#     # the first element       
#     A[i], A[min_idx] = A[min_idx], A[i]
 
# # Driver code to test above
# print ("Sorted array")
# for i in range(len(A)):
#     print("%d" %A[i],end=" , ")
# Output
# Sorted array: 
# 11 12 22 25 64 
# Complexity Analysis of Selection Sort
# Time Complexity: The time complexity of Selection Sort is O(N2) as there are two nested loops:

# One loop to select an element of Array one by one = O(N)
# Another loop to compare that element with every other Array element = O(N)
# Therefore overall complexity = O(N) * O(N) = O(N*N) = O(N2)
# Auxiliary Space: O(1) as the only extra memory used is for temporary variables while swapping two values in Array. The selection sort never makes more than O(N) swaps and can be useful when memory writing is costly. 

# Advantages of Selection Sort Algorithm
# Simple and easy to understand.
# Works well with small datasets.
# Disadvantages of the Selection Sort Algorithm
# Selection sort has a time complexity of O(n^2) in the worst and average case.
# Does not work well on large datasets.
# Does not preserve the relative order of items with equal keys which means it is not stable.
# Frequently Asked Questions on Selection Sort
# Q1. Is Selection Sort Algorithm stable?

# The default implementation of the Selection Sort Algorithm is not stable. However, it can be made stable. Please see the stable Selection Sort for details.

# Q2. Is Selection Sort Algorithm in-place?

# Yes, Selection Sort Algorithm is an in-place algorithm, as it does not require extra space.






s=[1,6,8,4]
n=4
for i in s:
    d=s.count(i)
    print(d)