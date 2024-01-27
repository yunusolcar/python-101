x = "selam"
print(x + " sd4")

# Data Objects:
# 1- Scalar
# 2 - Non-scalar


# Data Types
# Integer
# 1 - 2  - 3 - 4 - 5

# Float
# 2.5 - 10.2   Not: 2.0 da floattır.

# Boolean
# True - false


# type
type(2.3)  # yazarak hangi type  da olduğunu öğrenebiliriz

# type casting
# float olan sayıyı integere çevirme
# int(2.8) -> çıktı -> 2 olarak integer e dönüştü


# Variable Assingment
a = 2
x = a + 5  # x = 7
a = a + 3  # a = 5

# Non-Scaler
# String
# "ATATURK"
type("1")  # str

z = "Bugün Kadıköy'den Mecidiyeköy'e 40 dakikada gittim."
print(z)

# String Concatenation
"5" + "4"  #  "54"

# Succesive Concatenation
4 * "hello"  # "hellohellohellohello"
x = "1" + "0" * 5  # "100000"    => type(x) => str

# Length
len("turkiye!")  #   8

# Indexing (Alt elemanlara erişme)
name = "Dante"
name[1]  # "a"
"hello"[1]  #   "e"
employee = "Beatrice"
employee[-1]  # last index  => "e"

# Slicing
# [start:end]
model = "Tesla"
model[1:3]  #   "es"
model[:3]  #  "Tes"
model[1:]  #  "esla"
model[10:0:-1]  # "alse" (don't take index 0)
model[10::-1]  # &&
model[::-1]  #  "alseT"  (take all and reverse)

# Casting in Strings
a = "5"
int(a)  # =>   5    =>   type: integer

# Input
x = input("enter a number pls: ")
# gelen input'a 10 yazarsak x = "10" oluyor. !!! Inputtan gelen veri -String- olarak gelir.
print(type(x))  #   str
# w/casting =>   int(x) + 10  =>   20   => integer
y = int(input("enter a number pls: "))  # direct casting

# Comments
# we can use: # or """
"""
z = 1
print(z)
"""

# Comparison in Numerical Data and Operators
# i = j   =>   (=) Assignment
# i == j  =>  (==) Equality test
# i != j  =>  (!=) Inequality test (If it is not equal, "True" is returned.)
# i > j
# i < j
# i >= j
# i <= j

# Comparison in Strings
# "Orange" == "orange"   =>   false
# "Orange" != "orange"    =>   true
# "Orange" == "Orange"   =>   true
# "a" < "b"    => true
# "ahaha" < "byby"  =>   true ("b" > "a")
# "ab" < "ac"  => true ("c" > "b")

# Logical Operators
# not
# not true     =>   false
# not 5 > 3    =>   false
# not 5 == 5  =>   false
# not 1 > 20  =>   true

# and
# true and true     =>   true
# true and false    =>   false
# (5 > 1) and (20 < 40)  => true
# (3 > 2) and (11 < 7)  => false

# or
# true or false     =>   true
# false or false    =>   false
# (3 > 2) or (11 < 7)  => true
# (3 > 5) and (11 < 7)  => false

# Short circuit
# A and B => In the and operator, if A is false, result is automatically false
# A or B    => In the or operator, if A is true, result is automatically true
# (5 < 3) and print("hello")  => false
# (5 > 3) or print("hi") => True
# (5 < 3) or print("hi") => hi

# If - Else - Elif
x = int(input("enter a number pls: "))

if x % 2 == 0:
    print("num is even")
else:
    print("num is odd")


y = int(input("enter a number pls: "))

if y % 3 == 0:
    if y % 2 == 0:
        print("this number is divisible by both 2 and 3")
    else:
        print("this number is only divisible by 3.")
else:
    print("this number is only divisible by 2.")

print("end")


# Ternary Conditionals
result = input("y/n?")
if result == "y":  # yes or no
    b = 1
else:
    b = 0
    print(b)


# Let's try w ternary condinionals
result = input("y/n?")
b = 1 if result == "y" else 0
print(b)

# Loops
# while
r = int(input("enter a positive number pls: "))

while r < 0:
    print("this number is negative. Try again!")
    r = int(input("enter a positive number pls: "))
print("number positive")

e = 0
total = 0

while e <= 100:
    total += e
    e += 1
print(total)  # 5050


# for loop
# for <variable> in <object>
for c in "hey":
    print(c)  # "h", "e", "y"

for num in range(15):  # 0 to 14
    print("num: ", num)


total = 0
for x in range(101):
    total += x
print(total)  # (0+1+2+3+4...+100) = 5050


t = 1
for _ in range(5):
    t *= 5  # t = t*5
    print(t)  # 5,25,125,625,3125


word = "hello there"
n = len(word)
index = 0

while index < n:
    print(word[index])
    index += 1

# break
for i in range(10):
    if i == 4:
        break
    print(i)  # 0,1,2,3


p = 0
while p < 10:
    p += 1
    if p == 5:
        break
    print(p)

# continue
for i in range(10):
    if i == 5:
        continue
print(i)  # 1,2,3,4,6,7,8,9
