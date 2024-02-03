def square(num):
    return num**2


while True:
    num1, num2 = input("Enter Num1, Num2: ").split()

    if num1 == "q" or num1 == "Q" or num2 == "q" or num2 == "Q":
        print("exit")
        break

    num1 = int(num1)
    num2 = int(num2)

    num1_square = square(num1)

    if num1_square % num2 == 0:
        print(f"{num1_square} is exactly divisible by {num2}")
    else:
        print(f"{num1_square} is not exactly divisible by {num2}")

# Quiz 2
square = []
param1 = int(input("enter a range: "))


def func():
    for i in range(1, param1 + 1):
        square.append(i * i)


func()
total = sum(square)
print("list: ", square)
print("Result: ", total)


# other way:
param1 = int(input("enter a range: "))
girdi = input("Lütfen bir dizi elemanlarını boşluk bırakarak girin: ")

orijinal_dizi = [int(eleman) for eleman in girdi.split()]

# Her elemanı 3 ile çarp
yeni_dizi = [eleman * 3 for eleman in orijinal_dizi]

# Sonuçları yazdır
print("Orijinal Dizi:", orijinal_dizi)
print("Çarpılmış Dizi:", yeni_dizi)


def multiply(param1):
    arr = []
    for i in list.split():
        element1 = int(i)
        arr.append(element1)

    result = []
    for j in arr:
        element2 = j * param1
        result.append(element2)

    print("Original Array:", arr)
    print("Multiplication Result: ", result)

    total = 0
    for k in range(1, param1 + 1):
        total += k**2
    return total


param1 = int(input("enter a range: "))
list = input("Please enter elements of an array with spaces: ")

result = multiply(param1)
print("Result", result)


# Hackerrank Q-1
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


# Hackerrank Q-6
def is_leap(year):
    leap = False

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        leap = True

    return leap


year = int(input())
print(is_leap(year))


# Q-?
list = input("dizi gir: ")  # Burası inputtan geleni listeye çeviriyor ["1","2", "3"]
new = []  # en sonda buraya liste gelicek
for i in list.split():  # list elemanlarını tek tek split ile ayırıyoruz
    element = int(i)  # listede,her bir iterasyondan gelen stringi int çeviriyoruz.
    new.append(element)  # gelen int ları new listesinin sonuna ekliyoruz
print(new[0] + new[1])

yeni_dizi = []
for j in new:
    eleman = j * 3
    yeni_dizi.append(eleman)

print(yeni_dizi)


# Hackerrank Q-3
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


# Hackerrank Q-7
n = 3  # Kullanıcıdan alınan değer
my_list = []

# Liste oluşturma
for i in range(1, n + 1):
    my_list.append(str(i))

print(my_list)  # ["1","2","3"]

# Liste elemanlarını birleştirme
new_arr = "".join(my_list)
print(new_arr)  # 123
print(type(new_arr))  # str
