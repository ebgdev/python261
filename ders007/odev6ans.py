# --------------------------------------------------
# 1. BÖLÜM

products = ["laptop","mouse","keyboard","mouse","monitor","mouse","laptop"]

# Soru 1: "mouse" kaç defa geçiyor?

counter = 0

for item in products:
    if item == "mouse":
        counter += 1

print("Mouse sayısı:", counter)


# Soru 2: "laptop" geçen indexleri bul

locations = []

for index in range(len(products)):
    if products[index] == "laptop":
        locations.append(index)

print("Laptop indexleri:", locations)


# --------------------------------------------------
# 2. BÖLÜM

scores = [85, 42, 90, 67, 30, 100, 55, 48]
students = ["Ali","Veli","Ayse","Fatma","Can","Zeynep","Emre","Ece"]

# Soru 1: 60 ve üzeri alanlar

passed_students = []

for i in range(len(scores)):
    if scores[i] >= 60:
        passed_students.append(students[i])

print("Geçen öğrenciler:", passed_students)


# Soru 2: 50 altı alanlar

failed_students = []

for i in range(len(scores)):
    if scores[i] < 50:
        failed_students.append(students[i])

print("Kalan öğrenciler:", failed_students)


# Soru 3: Kaç tane çift not var?

even_counter = 0

for score in scores:
    if score % 2 == 0:
        even_counter += 1

print("Çift not sayısı:", even_counter)
