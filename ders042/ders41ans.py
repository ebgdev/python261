# def ornek_fonksiyon(n):
#     # --- 1. SABİT İŞLEMLER (5 İşlem) ---
#     x = 0  # 1. işlem
#     y = 0  # 2. işlem
#     z = 0  # 3. işlem
#     a = 0  # 4. işlem
#     b = 0  # 5. işlem

#     # --- 2. KÜBİK KISIM (3 * n^3 İşlem) ---
#     # Bu iç içe 3 döngü toplam n * n * n = n^3 kez çalışır.
#     # Her adımda 3 işlem yapıldığı için: 3 * n^3
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 x += 1  # 1. işlem
#                 y += 1  # 2. işlem
#                 z += 1  # 3. işlem

#     # --- 3. DOĞRUSAL KISIM (3 * n İşlem) ---
#     # Bu döngü n kez çalışır.
#     # Her adımda 3 işlem yapıldığı için: 3 * n
#     for i in range(n):
#         a += 1  # 1. işlem
#         b += 1  # 2. işlem
#         x += 1  # 3. işlem

#     return x + y + z + a + b



# 3n^3 + 3n + 5


def ornek_fonksiyon(n):
    # --- 1. SABİT İŞLEMLER (5 İşlem) ---
    x = 0  # 1. işlem
    y = 0  # 2. işlem
    z = 0  # 3. işlem
    a = 0  # 4. işlem
    b = 0  # 5. işlem

    # --- 2. KÜBİK KISIM (3 * n^3 İşlem) ---
    # Bu iç içe 3 döngü toplam n * n * n = n^3 kez çalışır.
    # Her adımda 3 işlem yapıldığı için: 3 * n^3
    counter = 0
    for h in range(3):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    counter += 1

    # --- 3. DOĞRUSAL KISIM (3 * n İşlem) ---
    for i in range(n):
        for y in range(3):
            counter += 1

    return x + y + z + a + b
