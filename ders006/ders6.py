# my_list = ["car1","car2","car2","car2","car3","car1","car4","car3"]
# to_search = "car2"  # Aranacak değer / Value we want to search
# counter = 0  # Sayacı başlatıyoruz / Initialize counter

# for item in my_list:  # Liste içindeki her elemanı tek tek dolaş / Iterate through each element in the list
#     if item == to_search:  # Eğer eleman aranan değere eşitse / If the item matches the searched value
#         counter += 1 # Sayacı 1 artır / Increase counter by 1
#         # counter = counter + 1  # Uzun yazım şekli / Long version of increment

# print(f"{to_search}:{counter}")  # Sonucu ekrana yazdır / Print the result



# ---------------------------------

# my_list = ["car1","car2","car2","car2","car3","car1","car4","car3","car2"]
# to_search = "car3" # Aranacak elemanı tanımlıyoruz / Declare the value to search

# locations = []  # Bulunan indexleri tutacak boş liste / Empty list to store found indexes

# for index in range(len(my_list)):  # Listenin index numaraları üzerinden dön / Iterate over indexes of the list
#     if my_list[index] == to_search:  # Eğer ilgili indexteki değer aranan değerse / If value at index matches
#         locations.append(index)  # O indexi listeye ekle / Append index to locations list

# print(f"{to_search} locations are: {locations}")  # Bulunan indexleri yazdır / Print found indexes


# ---------------------------------
# # Beklenen cikti: 4
# alist = ['erfan',True,'Toyota','False','3.11',-500,3.14,['a','b','c']]
# counter = 0  # String tipindeki elemanları sayacağız / We will count string type elements

# for item in alist:  # Liste içindeki her elemanı dolaş / Iterate through each item
#     if type(item) == str:  # Eğer elemanın tipi string ise / If item type is string
#         counter += 1  # Sayacı artır / Increase counter
# print(counter)  # Toplam string sayısını yazdır / Print total string count

# ---------------------------------
# 50 ve uzere alan ogrenciler
# scores = [100,49,50,51,70,90,30,20]  # Öğrenci notları / Student scores
# students = ['ahmet','tunahan','yusuf','fatih','sevval','nazli','bahadir','erfan']  # Öğrenci isimleri / Student names


# students_gte_50 = []  # 50 ve üzeri alan öğrenciler / Students who scored >= 50

# for index in range(len(students)):  # Index üzerinden hem isim hem not eşleştirmesi / Iterate using index for matching
#     if scores[index] >= 50:  # Eğer not 50 veya daha büyükse / If score is 50 or greater
#         students_gte_50.append(students[index])  # Öğrenciyi listeye ekle / Add student to result list

# print(students_gte_50)  # Başarılı öğrencileri yazdır / Print successful students

# -----------------------------------
# # puanlari cift / tek oluduguna gore listelemek
# scores = [100,49,50,51,70,90,30,21]
# students = ['ahmet','tunahan','yusuf','fatih','sevval','nazli','bahadir','erfan']

# # tekler
# odd_score_studentst = []  # Tek puan alan öğrenciler / Students with odd scores

# # ciftler
# even_score_studentst = []  # Çift puan alan öğrenciler / Students with even scores

# for index in range(len(scores)):  # Index üzerinden ilerle / Iterate using index
#     if scores[index] % 2 == 0:  # Mod operatörü ile çift kontrolü / Check even using modulo operator
#         even_score_studentst.append(students[index])  # Çift ise ekle / Add if even
#     else:
#         odd_score_studentst.append(students[index])  # Tek ise ekle / Add if odd


# print(f"evens: {even_score_studentst}")  # Çift puanlı öğrenciler / Even score students
# print(f"odds: {odd_score_studentst}")  # Tek puanlı öğrenciler / Odd score students

# -----------------------------------
# i variable her tur/cinsden bir dongude kullabilabilir ve iterasyon demektir
scores = [100,49,50,51,70,90,30,21]

# i : iter, iteration , iterasyon
for i in range(len(scores)):  # Index değerlerini üretir / Generates index values
    print(i)  # Indexleri yazdırır / Prints indexes



for score in scores:  # Listenin elemanları üzerinden direkt döner / Iterates directly over elements
    print(score)  # Her bir notu yazdırır / Prints each score
