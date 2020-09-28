sayılar = []
i = 0
while i < 5:
    try:
        sayı = int(input("Bir sayı giriniz: "))
    except:
        print("Not Valid Input !!!")
    else:
        i += 1
        sayılar.append(sayı)
    print(i)
büyük = sayılar[0]
for i in sayılar:
    if i > büyük:
        büyük = i
print(sayılar)
print("Girdiğiniz sayılardan en büyüğü : ", büyük)