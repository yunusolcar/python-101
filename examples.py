# 1 to 100
"""
a = 0
total = 0

while a <= 100:
    total += a
    a += 1
print(total)  # 5050

# Factorial
fact = int(input("enter a number: "))
result = 1

while fact > 0:
    result *= fact
    fact -= 1

print(result)

# enumerate
words = ["a", "b", "c", "d"]
for i in enumerate(words):
    print(i)

# continue
for numbers in range(1, 10):
    if numbers % 2 == 0:
        continue
    print(numbers)  # 1, 3, 5, 7, 9 (int)


# Functions
def say_hi():
    print("hi")


say_hi()  # hi


# example
def square(x):
    return x**2


print(square(5))


# example-2
def fullname(name, surname):
    return "-".join([name, surname])


print(fullname("John", "Doe"))  # "John-Doe"


# example-2 other solution
def fullname2(*argument):
    return "-".join(argument)


print(fullname2("Mustafa", "Kemal", "Atatürk"))


element = []  # Boş bir liste oluştur
total = 1  # 'total' adlı değişkeni sıfıra başlat

for i in range(1, (9 + 1)):
    total = i**2  # 'total' değişkenin karesini alır
    # total += 1  # total değişkenini 1 arttırır
    # total *= 5 # total değişkenini 5 ile çarpar
    element.append(total)  # 'total' değerini 'element' listesine ekle
print(element)


total_odd = []  # Tek sayıların toplamını içeren bir liste oluştur
n = int(input("Bir aralık girin: "))  # Kullanıcıdan bir sayı aralığı al
total = 0  # Toplamı sıfıra başlat

# 1 ile n arasındaki sayılar üzerinde döngü
for i in range(1, n + 1):
    if i % 2 == 1:  # Eğer sayı tekse
        total += i  # Tek sayıyı toplama ekle
        total_odd.append(i)  # Ek olarak gelen tek sayıları listeye ekleyip gösteriyoruz

# Oluşturulan liste 'total_odd' ve toplamı 'total' i ekrana yazdır
print("Tek sayıların toplamı liste şeklinde:", total_odd)
print("Toplam:", total)


n = int(input("Bir aralık girin: "))  # Kullanıcıdan bir sayı aralığı al
total = 0
i = 0
for i in range(1, n, 2):
    total += i
print(total)


#
n, m = input("enter start and end range: ").split()

n = int(n)
m = int(m)

total = 0
for i in range(n, m):
    if i % 7 == 0:
        total += i

print("total: ", total)


# Writing a string in reverse - 1
name = input(" enter your name: ")

name = name[::-1]
print(name)


# Writing a string in reverse - 2
user_name = input("enter your name: ")
reversed_name = ""

for i in user_name:
    reversed_name = i + reversed_name  # jhon   =>  nojh
    # reversed_name = reversed_name + i # jhon => jhon # don't forget
print(reversed_name)


# listing vowel letters - 1
fullname = input("enter your name: ")
vowels = []
count = 0

vowel_letters = "aeıioöuü"

for i in fullname:
    if i in vowel_letters:
        count += 1
        vowels.append(i)
print("Vowel letters: ", vowels)
print(" Total vowels: ", count)


# listing vowel letters - 2
def func(fullname):
    vowel_letters = "aeıioöuü"
    vowels = []

    for i in fullname:
        if i in vowel_letters:
            vowels.append(i)

    count = len(vowels)
    return vowels, count


fullname = input("enter your name: ")
vowels, count = func(fullname)

print("Vowel letters: ", vowels)
print("Total vowels: ", count)


# Fibonacci Numbers
a = 0
b = 1
c = 0

while c < 1000:
    print(b)
    c = a + b
    a = b
    b = c


# Prime Numbers
n = int(input("enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print(f"{n} is not prime number")
        break
else:
    print(f"{n} is prime number")


# Guess the number
import random

def guess(i):
    random_number = random.randint(1, i)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {i}: "))
        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too much")
    print(f"Nice, you have guessed {random_number}")


i = int(input("sayı aralığı gir: "))
guess(i)


# Rock, paper, scissors
import random

def play():
    user = input("r for rock, p for paper, s for scissors. What's your choice?: ")
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return print("Tie")

    if is_win(user, computer):
        return print("You won :) ")

    return print("You lost, computer's choice: ", computer)


# r > s, p > r, s > p
def is_win(player, opponent):
    if (
        (player == "r" and opponent == "s")
        or (player == "p" and opponent == "r")
        or (player == "s" and opponent == "p")
    ):
        return True

play()


# Countdown
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    
    print("Timer completed")

t = int(input("Enter the time in second: "))
countdown(t)


# Password Generator
import random

print("Password Generator")

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$€%^&*().,?"

password_length = int(input("input your password length: "))
print("\n Here is your Password")

passwords = ""
for i in range(password_length):
    passwords += random.choice(chars)
print("\n", passwords)


# QR code in Python
import qrcode

link = "https://www.youtube.com/watch?v=atGCQWspKTE&pp=ygUPbmFoIMOnZWtlbiBhZGFt"

img = qrcode.make(link)
img.save("C:/Users/***/***/***/qr/myQr.png")
"""
