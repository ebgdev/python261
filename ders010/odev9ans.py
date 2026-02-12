# ODEV1: Sayı Bulma Oyunu (Haklı Sistem)
# Açıklama
# Program, 1–50 arasında rastgele bir sayı üretir.
# Kullanıcının 5 tahmin hakkı vardır.
# Doğru tahmin → oyun biter
# Yanlış tahmin → yönlendirme yapılır
# Haklar bittiğinde → doğru sayı gösterilir




# Cevap:

import random

def find_the_number_game():
    target = random.randint(1, 50)
    condition = False
    attempt = 1
    max_attempt = 5
    print(target)
    while (attempt <= max_attempt):
        p_num = int(input(f"Predict a Number --{attempt}--: "))
        if p_num == target:
            print("Congrats...")
            condition = True
            return
        elif p_num < target:
            print("Predict a bigger number")
        else:
            print("Predict a smaller number")
        attempt += 1

    if not condition:
        return f"The real number was : {target}"


print(find_the_number_game())
