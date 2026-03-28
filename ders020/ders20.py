# my_dict = {"ogrenci_sayisi":4,"ders":"ders20"}


# print(my_dict[0]) # KeyError
# print(my_dict["ders"])

# print(my_dict.get(0)) # returns the value if the key exists, otherwise retuns none or default value if set.
# print("hello from lecture 20")

# -----------------------------------

# my_dict.update({"ders":"ders21"}) # update
# my_dict.update({"konu":"dictonary"}) # adding new key,value pair.

# print(my_dict)

# -----------------------------------

# poped_item = my_dict.pop("ders") # saved value as poped item.
# print(poped_item)
# print(my_dict)

# my_dict.pop("berke") # KeyError if key dose not exists.
# print(my_dict)


# -----------------------------------

# x = ('key1', 'key2', 'key3')

# print(type(x[0])) # str
# print(type(x))

# thisdict = dict.fromkeys(x)

# print(thisdict)

# -----------------------------------
# find unique items in the my_arr list

# my_arr = ['berke','aynaz','berke','yusuf','berke','yusuf','meltem']
# # output: ['berke','aynaz','yusuf','meltem']


# unique = list(dict.fromkeys(my_arr))
# unique1 = list(set(my_arr))
# print(unique)
# print(unique1)

# -----------------------------------


# students = ['berke','aynaz','yusuf','meltem']
# # .fromkeys(iterable,value) # default_value = None
# students_score = dict.fromkeys(students,0)
# print(students_score)


# -----------------------------------

# # ⚠️ Önemli Tuzak — Mutable Default Value

# # YANLIŞ — tüm key'ler aynı listeyi paylaşır!
# d = dict.fromkeys(["a", "b", "c"], [])
# d["a"].append(1)
# print(d)  # {'a': [1], 'b': [1], 'c': [1]}

# # DOĞRU — her key için ayrı liste
# d = {k: [] for k in ["a", "b", "c"]}
# d["a"].append(1)
# print(d)  # {'a': [1], 'b': [], 'c': []}


# -----------------------------------

# fruits = ['apple','banana','apple','banana','apple','kiwi','orange','apple','orange']

# # output: {'apple':4,'banana':2,'kiwi':1,'orange':2}



# # result = {'apple':2}
# def frequency(lst) -> dict:
#     result = {}
#     for item in lst:
#         if item not in result:
#             result[item] = 1 # create
#         else:
#             result[item] += 1 # update
#     return result

# print(frequency(fruits))


# -----------------------------------

# from collections import Counter
# fruits = ['apple','banana','apple','banana','apple','kiwi','orange','apple','orange']
# counter = (Counter(fruits))
# print(dict(counter))
# print(counter.most_common(3))


# -----------------------------------


adict = {'apple': 4, 'banana': 2, 'kiwi': 1, 'orange': 2, 'mango':1}
# expected output: {4:['apple'],2:['banana','orange'],1:['kiwi','mango']}

def group_by_frequency(adict) -> dict:
    result = {}
    for key,value in adict.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    return result

print(group_by_frequency(adict))


# -----------------------------------