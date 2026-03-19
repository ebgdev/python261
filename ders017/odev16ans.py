# elimizde asagidaki liste olusn:
# tekleri ve ciftleri ayiklayalim.

lst = [i for i in range(1,11)]


evens = list(filter(lambda x: x%2==0,lst))
odds = list(filter(lambda x: x%2==1,lst))


print(f"{evens=}")
print(f"{odds=}")




# --------------------------------

matrix1 = [[1, 2, 12],[4, 5, 16],[3, 8, 9]]


matrix2 = [[11, 8, 7],[6, 50, 4],[3, 2, 13]]

# ipucu: Once bos bir 3x3 result matrix'i acariz
# verileri guncelleyip buraya yazmamiz gerek.
result = [[0,0,0],[0,0,0],[0,0,0]]


for i in range(len(matrix1)): # i: 0,1,2, matrix1[i] = 1,2,12
    for j in range(len(matrix1[i])): # j: 0,1,2 - 0,1,2 - 0,1,2
        result[i][j] =  matrix1[i][j] + matrix2[i][j]


print(result)