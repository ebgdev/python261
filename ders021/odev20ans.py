# Ürünler ve fiyatları içeren sözlük
urunler = {
    'Laptop': 12000,
    'Tablet': 3500,
    'Telefon': 8000,
    'Kulaklik': 750,
    'Akilli Saat': 2000
}

def fiyat_sirala_azalan(urunler):
    result = []
    first_couple = list(urunler.items())[0]
    result.append(first_couple)

    for urun, fiyat in list(urunler.items())[1:]:
        index = 0
        while index < len(result) and fiyat < result[index][1]:
            index += 1
        result.insert(index, (urun, fiyat))

    return result

print(fiyat_sirala_azalan(urunler))


# def artan_sira(urunler):
#     result = sorted(urunler.items(),key=(lambda x: x[1]),reverse=False)
#     return result

# print(artan_sira(urunler))
