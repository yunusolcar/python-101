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
"""
# other way:
param1 = int(input("enter a range: "))


def square(param1):
    total = 0
    for i in range(1, param1 + 1):
        total += i**2
    return total


result = square(param1)
print(result)
