# my_dict = {'ders':"ders21","ogrenciler":['yusuf','berke','meltem']}

# print(my_dict.get('lesson'))
# # print(my_dict['lesson'])
# print("hello from lecture 21")

# -----------------------------

# poped_item = my_dict.pop('ders')
# print(poped_item)
# print(my_dict)

# -----------------------------


d1 = {
    'vw':['bugatii','skoda','leon','bently','porsche'],
    'dimlar':['mercedes benz','smart']
    }
d2 = {
    'fiat':['ferrari','maseratti'],
    'peogeot':['opel','ds']
    }


def merge_dicts(d1,d2):
    
    # d3 = {}
    # d3.update(d1)
    # d3.update(d2)
    # return d3

    # -------------------

    # d1.update(d2)
    # return d1

    # -------------------

    for key,value in d2.items():
        # d1[key] = value. 
        d1.update({key:value})

    return d1

print(merge_dicts(d1,d2))

# --------------------------------------------------

# sinif = {'ogrenci_sayisi':4,'ortalama_yas':24,"ders":"ders21","kurs":"python kursu",'ogrenci_sayisi':7}

# sinif['ortalama_yas'] = 26 # add, update
# sinif.update({'ders':'ders22'}) # add, update
# sinif.update({'konu':'dictonary'}) # add, update

# print(sinif)

# --------------------------------------------------