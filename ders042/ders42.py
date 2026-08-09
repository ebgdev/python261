# ✅ O(1) < O(log(n)) < O(n) < O(nlog(n)) < O(n^2),O(n^3),,, < O(2^n) < O(n!) ❌
# binary search icin liste sirali olmak zorunda.

lst = [11,34,45,56,62,73,87,98]
def binary_search(lst,target):
    counter = 0
    left = 0
    right = len(lst) - 1 # 9
    mid = 0
    
    while left <= right:
        mid = (left + right)//2  # 4
        if target > lst[mid]:
            left = mid + 1
            counter += 1
        elif target < lst[mid]:
            right = mid - 1
            counter += 1
        else:
            return mid,counter
    return None,counter

# print(binary_search(lst,87))
print(binary_search(lst,98))
# print(binary_search(lst,34))
print(binary_search(lst,56))
# print(binary_search(lst,250))

# her defasinda liste uzunlugunu ikiye bolmek

# best case: O(1)
# worst case: log(n)