musteriler = {
    1000000001: {
        'name': 'John',
        'sur_name': 'Doe',
        'age': 17,
        'married': False,
        'payment':40
    },
    1000000002: {
        'name': 'jane',
        'sur_name': 'Smith',
        'age': 18,
        'married': True,
        'payment':100
    },
    1000000003: {
        'name': 'Alice',
        'sur_name': 'Brown',
        'age': 22,
        'married': False,
        'payment':10
    },
    1000000004: {
        'name': 'Bob',
        'sur_name': 'Johnson',
        'age': 45,
        'married': True,
        'payment':140
    },
    1000000005: {
        'name': 'Charlie',
        'sur_name': 'williams',
        'age': 30,
        'married': True,
        'payment':0
    },
    1000000006: {
        'name': 'Eve',
        'sur_name': 'Davis',
        'age': 27,
        'married': False,
        'payment':410
    },
    1000000007: {
        'name': 'Julia',
        'sur_name': 'Miller',
        'age': 40,
        'married': True,
        'payment':100
    },
    1000000008: {
        'name': 'Nancy',
        'sur_name': 'Wilson',
        'age': 35,
        'married': True,
        'payment':130
    },
    1000000009: {
        'name': 'James',
        'sur_name': 'Taylor',
        'age': 21,
        'married': False,
        'payment':4250
    },
    1000000010: {
        'name': 'olivia',
        'sur_name': 'Anderson',
        'age': 38,
        'married': True,
        'payment':4
    }
}

# def find_even_ids_customers(d):
#     result = []
#     for id in d.keys():
#         if id % 2 == 0:
#             result.append(d[id]['name'])
#     return result

# ---------------------------------------

# def find_even_ids_customers(d):
#     result = []
#     for id,info in d.items():
#         if id % 2 == 0:
#             result.append(info['name'])
#     return result
# print(find_even_ids_customers(musteriler))
# ---------------------------------------


# def find_payments_ages(cpay,cage,d):
#     result = []
#     for info in d.values():
#         if info['payment'] > cpay and info['age'] > cage:
#             result.append(info['name'])
#     return result

# print(find_payments_ages(100,18,musteriler))


# -----------------------------------------


# def find_even_ages_surnames(d):
#     result = []
#     for info in d.values():
#         if info['age'] % 2 == 0:
#             result.append(info['sur_name'])
#     return result


# print(find_even_ages_surnames(musteriler))



# -----------------------------------------


def find_names_len(upper_limit,d):
    # upper limitin alitindaki uzunlukta olan musterileri istiyoruz
    result = []


print(find_names_len(5,musteriler))



# ------------------------------------------



# ODEV
# def cal_married_customers_avg_age(d):
#     pass



# ------------------------------------------


# def find_surname_startwith(char,d):
#     result = []
#     for info in d.values():
#         if info['sur_name'][0].upper() == char.upper(): # williams[0] = w
#             # result.append(info['name'] + ' ' + info['sur_name'])
#             result.append(f'{info['name']} {info['sur_name']}')
#     return result


# print(find_surname_startwith('w',musteriler)) # ['Charlie williams','Nancy Wilson']


# --------------------------------
# asagidaki verilen bilgilere uygun bir class yapisi olusturunuz
# ve sonra obje tanimlamalarini yaziniz

data = [
    "Toyota,CH-R,1.6,4,4,SUV",
    "Toyota,Corolla,1.6,4,4,Sedan",
    "Toyota,Yaris,1.4,4,4,Hatch",
    "Toyota,Thunder,2.8,4,4,Truck",
    "Toyota,F-150,1.6,4,4,Truck",
    "Toyota,GT86,2.0,4,4,Coupe",
    "Fiat,Lenea,1.6,4,4,SUV",
    "Fiat,Egea,1.4,4,4,Sedan",
    "kia,Rio,1.4,4,4,Hatch",
    "kia,Mojave,3.5,4,4,SUV",
    "kia,Sportage,1.8,4,4,SUV",
    "kia,Serato,2.0,4,4,SUV"
    ]

# ODEV
class Car:
    pass