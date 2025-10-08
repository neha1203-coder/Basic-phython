# 12. Binary Search (array must be sorted)
def binary_search(arr, key):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid]==key: return mid
        elif arr[mid]<key: low=mid+1
        else: high=mid-1
    return -1

arr = sorted([int(x) for x in input().split()])
key = int(input())
idx = binary_search(arr, key)
print("Found at index" if idx!=-1 else "Not found", idx)
