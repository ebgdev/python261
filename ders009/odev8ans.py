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



def unique_list(liste):
    unique_lst = []
    for name in liste:
        if name not in unique_lst:
            unique_lst.append(name)
    return unique_lst


print(unique_list(ogrenciler))

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



def liste_sirala(liste):
    yeni_liste = liste.copy()
    yeni_liste.sort()
    return(f"yeni_liste: {yeni_liste}"),(f"original liste: {liste}")


print(liste_sirala(ogrenciler))

