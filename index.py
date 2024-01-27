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
# type(2.3) yazarak hangi type  da olduğunu öğrenebiliriz

# type casting
# float olan sayıyı integere çevirme
# int(2.8) -> çıktı -> 2 olarak integer e dönüştü


# Variable Assingment
# a = 2
# x = a + 5    => x = 7
# a = a + 3    => a = 5

# Non-Scaler
# String
# "ATATURK"
# type("1")    => str

z = "Bugün Kadıköy'den Mecidiyeköy'e 40 dakikada gittim."
print(z)

# String Concatenation
# "5" + "4"    =>   "54"

# Succesive Concatenation
# 4 * "hello"  => "hellohellohellohello"
# x = "1" + "0" * 5 => "100000"    => type(x) => str

# Length
# len("turkiye!")    =>   8

# Indexing (Alt elemanlara erişme)
# name = "Dante"
# name[1] => "a"
# "hello"[1]   =>   "e"
# employee = "Beatrice"
# employee[-1]     => last element  => "e"

# Slicing
# [start:end]
# model = "Tesla"
# model[1:3]   =>   "es"
# model[:3]    =>   "Tes"
# model[1:]    =>   "esla"
# model[10:0:-1]     => "alse" (don't take index 0)
# model[10::-1]     &&   model[::-1]    =>   "alseT"  (take all and reverse)
# model

# Casting in Strings
# a = "5"
# int(a)  =>   5    =>   type: integer

# Input
# x = input("enter a number pls: ")
# gelen input'a 10 yazarsak x = "10" oluyor. !!! Inputtan gelen veri -String- olarak gelir.
# print(type(x))    =>   str
# w/casting =>   int(x) + 10  =>   20   => integer
# y = int(input("enter a number pls: "))     => direct casting

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