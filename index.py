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


# List
price = [10, 52, 78, 32, 69]
price[0]  # 10
price[-1]  # 69
price[1:4]  # 25, 78, 32

# lists are mutable data type
price[1] += 5  # 57
price[0:3] = 20, 30, 40  # price = [20, 30, 40, 32, 69]

# len
len(price)  # 5

# append()
# adds to the end of the list (single)
brand = ["Ferrari", "Koenigsegg"]
brand.append("Mclaren")  # ["Ferrari", "Koenigsegg", "Mclaren" ]

# extend()
# adds to the end of the list (multiple)
animals = ["dog", "cat"]
animals.extend(["monkey", "elephant"])  # ["dog", "cat", "monkey", "elephant"]

# insert()
# attach to a specific place
numbers = [1, 2, 3, 4, 5]
numbers.insert(0, 100)  # [100, 1, 2, 3, 4 ,5] added 100 to index zero
numbers.insert(3, 99)  # [100, 1, 2, 99, 3, 4, 5]

# remove()
# removes the first element
aircrafts = ["Airbus", "Boeing", "Bombarder"]
aircrafts.remove("Boeing")  # ["Airbus", "Bombarder"]

# pop()
# Removes the element at the specified position

# count()
# Returns the number of elements with the specified value
watches = ["Casio", "Rolex", "Casio", "Panamera", "Richard Mille"]
print(watches.count("Casio"))  # 2

# copy()
# Returns a copy of the list

# find the index of an element
# watches.index("Panamera") # 3

# reverse
# reversing the list
# a = [1, 2, 3]
# a.reverse()   [3, 2, 1]

# in
# The in keyword is used to check if a value is present in a sequence (list, range, string etc.).
# The in keyword is also used to iterate through a sequence in a for loop
list = [1, 2, 3, 4]
3 in list  # true
15 in list  # false


# sorting
# a = ["b", "a", "c", 1, 2.5, 3]
# a.sort()  [1, 2.5, 3, "a", "b", "c"]

# Tuple
# Tuples are used to store multiple items in a single variable.
# !!! A tuple is a collection which is ordered and unchangeable.
# tuples usage  => t = (element1, element2, ...)    or  element1, element2, ...
k = 10
y = 20
location = (10, 20)
location[0] = 100  # !!! can't change

# Dictionaries
# Dictionaries are used to store data values in key:value pairs. {}
# usage: {key : value, key2: value2, key3: value3, ...}
score = {"John": 700, "Jane": 860, "Jim": 950}
score["Jane"]  # 860

players = {
    "Alp": {"id": 5, "age": 21},
    "Akın": {"id": 7, "age": 23},
    "Orhun": {"id": 8, "age": 19},
    "Selin": {"id": 11, "age": 20},
}

players["Akın"]  # "id": 7, "age": 23
players["Selin"]["id"]  # 11
players[0]  # ERROR
players["Orhun"]["age"]  # 19
players["Alp"] = players["Alp"] + 5  # 21 + 5 = 26

# Add Element to Disctionary
players["Sema"] = {"id": 10, "age": 19}  # add "Sema"
print(
    players
)  #  {'Alp': {'id': 5, 'age': 21}, 'Akın': {'id': 7, 'age': 23}, 'Orhun': {'id': 8, 'age': 19}, 'Selin': {'id': 11, 'age': 20}, 'Sema': {'id': 10, 'age': 19}}

# del user
del players[  # delete "Orhun"
    "Orhun"
]  # {'Alp': {'id': 5, 'age': 21}, 'Akın': {'id': 7, 'age': 23}, 'Selin': {'id': 11, 'age': 20}, 'Sema': {'id': 10, 'age': 19}}

# search user
"Ayşe" in players  # false
"Sema" in players  # true

# Sets
# Sets are used to store multiple items in a single variable.
# sets are not indexable, sets are mutable
# Dictionaries : score = {"John": 700, "Jane": 860, "Jim": 950, "John": 700}
# Sets : myset = {"apple", "banana", "cherry"}
g = {}  # type(g) <dict> # empty dictionaries
s = set()  # type(s) <set> # empty set

message = "hello there"
myString = set(message)
print(myString)  # {'h', ' ', 'e', 'l', 'r', 'o', 't'}

numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5, 6, 7, 8]
thisSet = set(numbers)
print(type(thisSet))  # {1, 2, 3, 4, 5, 6, 7, 8}

# tuple to set
myTuple = (1, 2, 3, 4, 5, 5)  # tuple
print(myTuple)  # (1, 2, 3, 4, 5, 5)
mySet = set(myTuple)
print(mySet)  # {1, 2, 3, 4, 5}

# add/remove element to set
s = {1, 2, 3}
s.add(6)  # {1,2,3,6}
s.remove(1)  # {2, 3, 6}
# If we try to delete a non-existent element with remove we get an error, but if we use discard instead we don't get an error
s.discard(11)  # {2, 3, 6}

# Difference
# differences between the two sets
s1 = set([1, 3, 5])
s2 = set([2, 3, 8])
print(s1.difference(s2))  # {1, 5}
s1 - s2  # {1, 5} same

# intersection (kesişim)
s1 = set([1, 3, 11, 5])
s2 = set([2, 3, 11, 8])
s1.intersection(s2)  # {3, 11}
s1 & s2  # {3,11} same

# Union
s1 = set([1, 5, 10])
s2 = set([2, 5, 11])
s1.union(s2)  # {1, 2, 5, 10, 11}

# Non-scalar for
list = [60, 70, 85, 90]
for i in range(len(list)):
    list[i] += 5
print(list)  # [65, 75, 90, 95]

# For loop to add 5 points to each grade, excluding the student at index 1
studentGrades = [55, 80, 65, 40]
for i in range(len(studentGrades)):
    if i != 1:
        studentGrades[i] += 5
    print(studentGrades)  # [60, 80, 70, 45]

# search for an element in a list
text = int(input("Which number do you want to search for? : "))
myList = [12, 46, 92, 59, 27, 38, 21]

for i in myList:
    print(i)
    if i == text:
        print("Found!")
        break  # 38 Found!

# split()
# string to list
# We write what we want to split according to split()
text = "Hello World i love python"
t.split(" ")  # space char =>    ["Hello", "World", "i", "love"," python"]

myText = "my name is yunus, what's yours?"
print(myText.split("u"))  # ['my name is y', 'n', "s, what's yo", 'rs?']

# join
# list to string
fruits = ["banana", "apple", "grape"]
print("/".join(fruits))  # banana/apple/grape
