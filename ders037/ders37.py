# # beklenen_cikti: 
# # products = ['icecream','phone','laptop','tv','refragerator','watch']

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# full_path = BASE_DIR / 'products.txt'

# products = []
# with open(full_path,mode='r',encoding='utf8') as f:
#     for line in f:
#         id,title = line.strip('\n').split(',')
#         products.append(title)

# poped_item = products.pop(0)
# print(products)

# ----------------------------------------------

# Evlilerin ortalama yasi nedir ? 49.6

from pathlib import Path
from statistics import mean
BASE_DIR = Path(__file__).resolve().parent
full_path = BASE_DIR / 'customers.txt'

# marrieds_age = []
# with open(full_path,mode='r',encoding='utf8') as f:
#     next(f) # ignoring first line, the header
#     for line in f:
#         customer = line.strip('\n').split(',')
#         if customer[4] == '1':
#             marrieds_age.append(int(customer[3]))

# print(mean(marrieds_age))

# ------------------


# marrieds_age = []
# with open(full_path,mode='r',encoding='utf8') as f:
#     next(f) # ignoring first line, the header
#     for line in f:
#         id,first_name,last_name,age,is_married,balance = line.strip('\n').split(',')
#         if bool(int(is_married)):
#             marrieds_age.append(int(age))

# print(mean(marrieds_age))


# ------------------

# marrieds_age = []
# with open(full_path,mode='r',encoding='utf8') as f:
#     next(f) # ignoring first line, the header
#     for line in f:
#         age,is_married = line.strip('\n').split(',')[3:-1:1]
#         if bool(int(is_married)):
#             marrieds_age.append(int(age))

# print(mean(marrieds_age))


# ---------------------------------------------------------

# En yukesek bakiyeye sahip olan 5 musterinin toplam bakiyesi nedir ?


with open(full_path,mode='r',encoding='utf8') as f:
    result=[]
    next(f)
    for line in f:
        balance=line.strip('\n').split(',')[-1]
        result.append(int(balance))

sorted_payments = sorted(result,reverse=True)
print(sum(sorted_payments[:5]))
# total_payment = 0
# for index in range(5):
#     total_payment += sorted_payments[index]

# print(total_payment)