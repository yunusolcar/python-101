# 1 to 100
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
