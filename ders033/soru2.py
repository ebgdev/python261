# soru2:
# DESIRED OUTPUT
# ['D', 'NC', 'ZMP']

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# file_name = BASE_DIR / 'soru2.txt'


def soru2(filename):
    result=[]
    with open(filename) as f:
        for line in f:
            row=''
            for i in range(1,len(line),4): # start:1,stop:listenin sonu,step:4
                row+=line[i]
            result.append(row.stript())
    return result


file_name = "soru2.txt"
print(soru2(filename=file_name))

# --------------------------------------------------
# alias: takma isim
with open(file_name) as f:
    result = [line[1::4].strip() for line in f]

print(result)