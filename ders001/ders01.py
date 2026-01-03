# ==============================
# 1) Veri Tipleri / Data Types
# ==============================

# TR: Tam sayı (integer) -> ondalık kısmı olmayan sayılar
# EN: Integer -> whole numbers without a decimal part
x = 3
print(type(x))  # <class 'int'>

# TR: Ondalıklı sayı (float) -> kayar noktalı sayılar
# EN: Float -> floating-point numbers (with a decimal part)
y = 3.14
print(type(y))  # <class 'float'>

# TR: Metin (string) -> karakter dizisi
# EN: String -> sequence of characters (text)
name = "erfan"
print(type(name))  # <class 'str'>

# TR: Boolean -> Mantıksal değerler: True / False
# EN: Boolean -> Logical values: True / False
is_active = True
print(type(is_active))  # <class 'bool'>

# TR: None -> "değer yok / boş" anlamına gelir (NoneType)
# EN: None -> represents "no value" (NoneType)
value = None
print(type(value))  # <class 'NoneType'>


# ==============================
# 2) Operatörler / Operators
# ==============================

# TR: Matematiksel operatörler
# EN: Arithmetic operators
a = 10
b = 5

print(a + b)  # TR: Toplama / EN: Addition
print(a - b)  # TR: Çıkarma / EN: Subtraction
print(a * b)  # TR: Çarpma / EN: Multiplication
print(a / b)  # TR: Bölme (sonuç float) / EN: Division (result is float)

# TR: Üs alma (b üzeri a -> 5^10)
# EN: Exponentiation (b to the power of a -> 5^10)
print(b ** a)

# TR: Normal bölme float verir
# EN: Normal division returns float
print(5 / 4)   # 1.25

# TR: Tam bölme (floor division) aşağı yuvarlar
# EN: Floor division rounds down
print(9 // 4)  # 2


# ==============================
# 3) Karşılaştırma / Comparison
# ==============================

# TR: '==' eşit mi? (değeri karşılaştırır)
# EN: '==' checks equality (compares values)
print(3 == "3")   # False (int ile str farklı)
print(3 == 3.0)   # True (int ve float değer olarak eşit)

# TR/EN: Bu ifadelerin tipi bool olur
print(type(3 == "3"))   # <class 'bool'>
print(type(3 == 3.0))   # <class 'bool'>

# TR: Büyük-küçük karşılaştırmaları
# EN: Greater/less comparisons
print(a >= b)
print(a <= b)

# TR: '!=' eşit değil mi?
# EN: '!=' not equal?
print(3 != "3")  # True

# TR: not -> tersine çevirir
# EN: not -> negates a boolean
print(not True)   # False
print(not False)  # True


# ==========================================
# 4) Birleştirme / Concatenation (String)
# ==========================================

# TR: String'leri + ile birleştirebilirsin
# EN: You can concatenate strings using +
first_name = "erfan"
surname = "bahcivan"
print(first_name + " " + surname)

# TR: String + int yapamazsın -> TypeError
# EN: You cannot add a string and an int -> TypeError
# print(first_name + 10)  # HATA / ERROR

# TR: Ama sayılar kendi aralarında toplanabilir (int + float = float)
# EN: Numbers can be added (int + float = float)
print(13 + 3.14)  # 16.14

# TR: Eğer sayıyı string ile birleştirmek istiyorsan str() kullan
# EN: If you want to join a number with a string, use str()
print(first_name + " " + str(10))


# ==============================
# 5) if - else Bloğu / if - else
# ==============================

# TR: if koşulu doğruysa içeri girer, değilse else çalışır
# EN: if runs when condition is True, otherwise else runs
login_name = "erfan"

if login_name == "erfan":
    print("Merhaba, sisteme hoş geldiniz!")  # TR message
else:
    print("Maalesef sisteme giriş yapamazsınız!")  # TR message
