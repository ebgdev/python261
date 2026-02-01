# ÖDEV 1 — 

# Elimizde bir öğrenci listesi var:

ogrenciler = [
    "berke",
    "damla",
    "berke",
    "aynaz",
    "berat",
    "berke",
    "damla"
]


# unique_list(liste) fonksiyonunu yazınız

# Bu fonksiyon:
# Liste alacak
# İçindeki tekrar eden isimleri temizleyecek
# Sadece benzersiz isimlerden oluşan yeni bir liste döndürecek
# Orijinal liste değişmeyecek

# Örnek çıktı:
# ["berke", "damla", "aynaz", "berat"]

# ------------------------------------------------------------------------

# ÖDEV 2 — 

ogrenciler = [
    "erfan",
    "berke",
    "damla",
    "berke",
    "aynaz",
    "berat",
    "berke",
    "damla"
]

# bu listedeki ogrencileri original listeye dokunmadan 
# yeni bir listede siralayiniz

# Örnek çıktı:
# orijinal: ['erfan', 'berke', 'damla', 'berke', 'aynaz', 'berat', 'berke', 'damla']
# yeni: ['aynaz', 'berat', 'berke', 'berke', 'berke', 'damla', 'damla', 'erfan']