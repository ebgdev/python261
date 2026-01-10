mat_score = float(input("enter your math score: "))
fizik_score = float(input("enter your fizik score: "))
kimya_score = float(input("enter your kimya score: "))


avg = (mat_score + fizik_score + kimya_score)/3

# print(f"") --> print format (yani bir kac format ile cikti alacagiz)

if avg >= 50:
    # print("tebrikler ",avg, "ile gectiniz")
    print(f"tebrikler {round(avg,2)} ile gecttiniz")
else:
    # print("maalesef ",avg, "ile kaldiniz")
    print(f"maalesef {round(avg,2)} ile kaldiniz")