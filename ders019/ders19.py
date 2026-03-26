# nums = [3,2,7,11,9,4,15,0]
# target = 11
# # [(2,9),(7,4),(11,0)]


# def two_sum_nested_loop(nums,target):
#     result = []
#     for i in range(len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 result.append((nums[i],nums[j]))
#     return result



# def two_sum_dict(nums,target):
#     result = []
#     seen = {2:1}
#     for i in range(len(nums)): # i = 4
#         complement = target - nums[i] # 2 = 11 - 9
#         if complement not in seen:
#             seen[nums[i]] = i
#         else:
#             result.append((complement,nums[i]))
#     return result




# print(f"{two_sum_nested_loop(nums,target)=}")
# print(f"{two_sum_dict(nums,target)=}")


# --------------------------------------------------------------------------

musteriler = {
    1000000001: {
        'name': 'John',
        'sur_name': 'Doe',
        'age': 17,
        'married': False
    },
    1000000002: {
        'name': 'jane',
        'sur_name': 'Smith',
        'age': 18,
        'married': True
    },
    1000000003: {
        'name': 'Alice',
        'sur_name': 'Brown',
        'age': 22,
        'married': False
    },
    1000000004: {
        'name': 'Bob',
        'sur_name': 'Johnson',
        'age': 45,
        'married': True
    },
    1000000005: {
        'name': 'Charlie',
        'sur_name': 'Williams',
        'age': 30,
        'married': True
    },
    1000000006: {
        'name': 'Eve',
        'sur_name': 'Davis',
        'age': 27,
        'married': False
    },
    1000000007: {
        'name': 'Julia',
        'sur_name': 'Miller',
        'age': 40,
        'married': True
    },
    1000000008: {
        'name': 'Nancy',
        'sur_name': 'Wilson',
        'age': 35,
        'married': True
    },
    1000000009: {
        'name': 'James',
        'sur_name': 'Taylor',
        'age': 21,
        'married': False
    },
    1000000010: {
        'name': 'olivia',
        'sur_name': 'Anderson',
        'age': 38,
        'married': True
    }
}


# print(musteriler)

# for key in musteriler:
#     print(key)


# print(list(musteriler.keys()))


# ------------ values only --------------

# for key in musteriler:
#     print(musteriler[key])


# for value in musteriler.values():
#     print(value)


# ---------------------------------------


# def avg_age1(adict):
#     total = 0
#     for value in adict.values():
#         total += value['age']
    
#     return total/len(adict)


# print(avg_age1(musteriler))


# ---------------------------------------


# def find_ages_gt25(adict):
#     upper_bound = 25
#     names = []
#     for value in adict.values():
#         if value['age'] > upper_bound:
#             names.append(value['name'])

#     return names


# print(find_ages_gt25(musteriler))

# --- lambda ---

def find_ages_gt25(adict):
    upper_bound = 25
    names = list(map(lambda x: x['name'],filter(lambda x: x['age'] > upper_bound, adict.values())))
    
    return names


print(find_ages_gt25(musteriler))

# ---------------------------------------


def select_names_start_with(adict,char):
    result = []
    for value in adict.values():
        if value['name'][0].upper() == char.upper():
            result.append(value['name'])

    return result


print(select_names_start_with(musteriler,'j'))


# ---------------------------------------