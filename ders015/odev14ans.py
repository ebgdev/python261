# # A )
import math
sayilar = [1, 2, 3, 4, 5, 6]
sayilar_pow_2 = [(lambda x: int(math.pow(x,2)))(x)for x in sayilar]
print(sayilar_pow_2)

# -----------------------------------------

# # # B )
# numbers = (5,10)
# # False for odd
# # True for even

# odd_even = [(lambda x: x%2==0)(x)for x in numbers]
# print(odd_even)

# -----------------------------------------

# # C )
# # İsim Temizleme: Aşağıdaki listeyi, lambda kullanarak tüm isimlerin 
# # baş harfi büyük olacak şekilde güncelleyin:
# isimler = ["ahmet", "ayşe", "mehmet", "zeynep"]

# temiz_isimler = [(lambda x: x.capitalize())(x)for x in isimler]
# print(temiz_isimler)
