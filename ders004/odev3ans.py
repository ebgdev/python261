puanlar = [20, 90, 77, 60, 91, 0, 100, 99]
# isimler = ['damla','berke','aynaz','berat','ayzzzz']

# print(max(isimler))
# print(min(isimler))

temp_min = puanlar[0]
temp_max = puanlar[0]

for puan in puanlar:
    if puan > temp_max:
        temp_max = puan
    
    if puan < temp_min:
        temp_min = puan

print(f"Max: {temp_max}, Min:{temp_min}")