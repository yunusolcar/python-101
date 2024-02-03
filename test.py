# list = input("dizi gir: ")  # Burası inputtan geleni listeye çeviriyor ["1","2", "3"]
# new = []  # en sonda buraya liste gelicek
# for i in list.split():  # list elemanlarını tek tek split ile ayırıyoruz
#     element = int(i)  # listede,her bir iterasyondan gelen stringi int çeviriyoruz.
#     new.append(element)  # gelen int ları new listesinin sonuna ekliyoruz
# print(new[0] + new[1])

# yeni_dizi = []
# for j in new:
#     eleman = j * 3
#     yeni_dizi.append(eleman)

# print(yeni_dizi)
# Hackerrank Q-2
n = 25

if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and (6 <= n <= 20):
    print("Weird")
elif n > 20 and n % 2 == 0:
    print("Not Weird")
else:
    print(":/")
