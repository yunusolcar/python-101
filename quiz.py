"""
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
"""


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
