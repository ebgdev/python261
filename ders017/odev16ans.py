# elimizde asagidaki liste olusn:
# tekleri ve ciftleri ayiklayalim.

lst = [i for i in range(1,11)]


evens = list(filter(lambda x: x%2==0,lst))
odds = list(filter(lambda x: x%2==1,lst))


print(f"{evens=}")
print(f"{odds=}")




# --------------------------------