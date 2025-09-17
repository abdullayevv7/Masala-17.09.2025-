##1-Masala: Foydalanuvchidan son qabul qilib, uning musbat yoki manfiy ekanligini aniqlang va natijani chiqaring.

son = float(input("Iltimos, biror son kiriting: ")) # foydalanuvchidan son qabul qilish

if son > 0: # agar son 0 dan katta bo'lsa
    print(f"{son} - musbat son") # son musbat ekanligini chiqarish

elif son == 0: # agar son 0 ga teng bo'lsa
    print(f"{son} - son nolga teng") # son nolga teng ekanligini chiqarish

else: # aks holda
    print(f"{son} - manfiy son") # son manfiy ekanligini chiqarish


##2-Masala: Foydalanuvchidan tug'ilgan yilini qabul qilib, uning yoshini hisoblang va natijani chiqarib bering.

hozirgi_yil = 2025

tugilgan_yil = int(input("Tug'ilgan yilingizni kiriting: "))

yil = hozirgi_yil - tugilgan_yil

print(f"Siz hozir {yil}yoshdasiz!")