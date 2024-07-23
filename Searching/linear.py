# Linear Search is defined as a sequential search algorithm that starts at one end and goes through each 
# element of a list until the desired element is found, otherwise the search continues till the end of the
# data set.

# 1]BUBBLE SORT       sorted at last
 
# 2]SELECTION SORT   find postion last unsorted and sorted in bigging

# 3]INSERTION SORT   key element   #less time complexity

# QUICK SORT

# MARGE SORT

# HEAP SORT



# a=[2,4,6,3,1,2,9]
# key=int(input("enter a key"))
# n=len(a)
# for i in range(0,n):
#     if a[i]==key:
#         print("exist")
#     else:
#         print("not")


# a=[2,3,7,8,12,13,15]
# n=len(a)
# key=int(input("enter a key"))
# low=0
# high=n-1
# while low<=high:
#     mid=(low+high)//2
#     if a[mid]==key:
#         print("exist")
#         break
#     elif a[mid]<key:
#         low=mid
#     elif a[mid]>key:
#         high=mid-1
#     else:
#         print("not")
# print(a)




def binary(a,low,high,key):
    if low<=high:
        mid=(low+high)//2
    if a[mid]==key:
        return True
    elif a[mid]<key:
        return binary(a,mid+1,high,key)
    
    elif a[mid]>key:
        return binary(a,low,mid-1,key)
    else:
        return False
a=[1,2,3,4,5,67,8,9,10,11,12]
print(binary(a,0,len(a)-1,4))