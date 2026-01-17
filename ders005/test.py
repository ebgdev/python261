array = [11,0,12,10,-10]


temp_min = array[0]
temp_max = array[0] # 11


for index in range(1,len(array)): # len(array) -> 5, range(5) -> 1,2,3,4
    if array[index] > temp_max:
        temp_max = array[index]
    
    if array[index] < temp_min:
        temp_min = array[index]

print("min:",temp_min)
print("max:",temp_max)