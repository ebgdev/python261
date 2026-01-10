# sehir = "samsun"

# if sehir == "samsun":
#     print("55")
#     sehir = "ankara"
# if sehir == "ankara":
#     print("06")
#     sehir = "istanbul"
# elif sehir == "istanbul":
#     print(34)
#     sehir = "tokat"
# else:
#     print("sehir bulunamadi")

# print(sehir)

# ---------------------------------------
# # mat 4
# # fizik 3
# # kimya 2

# mat_credit = 4
# fizik_credit = 3
# kimya_credit = 2

# mat_score = float(input("enter your math score: "))
# fizik_score = float(input("enter your fizik score: "))
# kimya_score = float(input("enter your kimya score: "))


# avg = (mat_score*mat_credit + fizik_score*fizik_credit + kimya_score*kimya_credit)/9

# # print(f"") --> print format (yani bir kac format ile cikti alacagiz)

# if avg >= 50:
#     # print("tebrikler ",avg, "ile gectiniz")
#     print(f"tebrikler {round(avg,2)} ile gecttiniz")
# else:
#     # print("maalesef ",avg, "ile kaldiniz")
#     print(f"maalesef {round(avg,2)} ile kaldiniz")


# ---------------------------------------

# Donguler, Loops
# TR: Döngüler tekrar eden işlemleri otomatik yapar.
# EN: Loops automate repetitive tasks by repeating a block of code.

# ---------------
# name = "erfan bahcivan"

# # print(name[0])
# # print(name[2])
# # print(name[4])
# # TR: String indexleme ile belirli karakteri alıyoruz (0'dan başlar).
# # EN: String indexing lets us pick a specific character (starts at 0).

# # print(name[-1])
# # print(name[-2])
# # TR: Negatif index sondan sayar (-1 en son karakter).
# # EN: Negative indexing counts from the end (-1 is the last char).

# ---------------
# # char degiskeni surekli olarak degisiyor , sart saglandigi surece.
# # TR: Döngü her turda "char" değişkenine yeni bir karakter atar.
# # EN: On each iteration, the loop assigns a new character to "char".
# # bosluga : white space character 
# # TR: Boşluk da bir karakterdir (white space).
# # EN: A space is also a character (white space).
# name = "erfan bahcivan"
# # Dongu 1. for loop, for dongusu
# # TR: for döngüsü, bir koleksiyonun (string/list vb.) elemanlarını tek tek dolaşır.
# # EN: a for-loop iterates through each element of a collection (string/list, etc.).
# for char in name: # char: n
#     # TR: "name" içindeki her karakter sırayla "char" olur.
#     # EN: each character in "name" becomes "char" one by one.
#     print(char)

# print("-------------")
# print(char)
# TR: Döngü bittikten sonra "char" en son karakterde kalır.
# EN: After the loop ends, "char" keeps the last value it received.

# ---------------------------------------
# Listeler
# TR: Liste, birden fazla değeri tek değişkende tutar (sıralı, index'li).
# EN: A list stores multiple values in one variable (ordered, indexed).

class_names = ['berat','damla','berke','aynaz','taha','muhammet']
# print(class_names)
# print(type(class_names))
# print(class_names[-2])
# TR: class_names[-2] sondan ikinci elemanı verir.
# EN: class_names[-2] gives the second item from the end.

for name in class_names:
    # TR: Liste içindeki her isim sırayla "name" değişkenine gelir.
    # EN: Each name in the list is assigned to "name" one by one.
    print(name,"python seviyor.")
    # print(f"{name} python serviyor.")
    # TR: f-string ile daha temiz formatlı yazdırma yapılabilir.
    # EN: f-strings can format output more cleanly.

print("----------------")

for char in class_names[0]:
    # TR: class_names[0] ilk isimdir (ör: 'berat'); bu döngü o ismin harflerini gezer.
    # EN: class_names[0] is the first name (e.g., 'berat'); this loop iterates over its letters.
    print(char)

print("----------------")

# length --> uzunluk
# TR: len(...) uzunluğu verir (string için karakter sayısı).
# EN: len(...) returns length (for strings: number of characters).
for name in class_names:
    # print(name,len(name))
    # TR: İsim ve uzunluğunu yan yana yazdırabiliriz.
    # EN: We can print the name and its length together.
    print(f"{name} is consist of {len(name)} characters")
    # TR: f-string içinde {len(name)} hesaplanıp yazdırılır.
    # EN: Inside the f-string, {len(name)} is computed and inserted.

# ---------------------------------------

numbers = [11,13,22,33,23,44,55,88]
# TR: numbers listesi sayılardan oluşuyor.
# EN: numbers is a list of integers.

for num in numbers:
    # TR: num, listedeki her sayıyı sırayla temsil eder.
    # EN: num represents each number in the list, one at a time.
    if num % 2 == 0:
        # TR: % (mod) kalan operatörüdür; 2'ye bölümden kalan 0 ise sayı çifttir.
        # EN: % (modulo) gives remainder; remainder 0 when dividing by 2 means even.
        print(f"number:{num} is even.")
    else:
        # TR: Kalan 0 değilse sayı tektir.
        # EN: If remainder is not 0, the number is odd.
        print(f"number:{num} is odd.")
