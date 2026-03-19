# def is_unique(lst) -> bool:
#     return len(set(lst)) == len(lst)


# print(is_unique([1,1,2,3,2])) # False
# print(is_unique([1,11,12,13,21])) # True


# -----------------------------------

# set_a = {'meltem','berke','yusuf','aynaz'}

# set_a.add('berke')
# set_a.add('erfan')


# # set_a.remove('erfan') # removes if the item exist, else KeyError.
# # set_a.discard('erfan') # removes if the item exist, else no error occured.
# # set_a.discard('yusuf')


# # poped_item = set_a.pop() # pops a random item from set.
# # print(poped_item)


# set_b = {'yusuf','berke'}

# print(set_a.issuperset(set_b)) # ust kume
# print(set_b.issubset(set_a)) # alt kume

# fs = frozenset(set_a) # immutable set, degistirilmeyen kume
# print(set_a)



# ----------------------------------- dict part2 ------------------------------

# nums = [2,7,11,9,15]
# target = 11
# # [0,3]

# # -----------------

# nums1 = [3,1]
# target1 = 6

# def twoSum(nums,trgt):
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == trgt:
#                 return [i, j]

# print(twoSum(nums,target))
# print(twoSum(nums1,target1))


#  ------------------------------ range hatirlatma ------------------------


# lst = [11,12,13,14,15,16,17,18,19,20]
# # range(start(inclusive), stop(exclusive), [step])
# new_list = []
# for i in range(len(lst)-1,-1,-1):
#     new_list.append(lst[i])


# print(new_list)


# --------------------------------------------------------------------------


nums = [2,7,11,9,15]
target = 11
# [0,3]

# -----------------

nums1 = [3,1]
target1 = 6

def twoSum(nums,target):
    seen = {}
    for i in range(len(nums)):
        complement = target - nums[i] # 11 - 9 --> complement 2
        if complement not in seen:
            seen[nums[i]]=i
        else:
            return [seen[complement],i]



print(twoSum(nums,target))
print(twoSum(nums1,target1))