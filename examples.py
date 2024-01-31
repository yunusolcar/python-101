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
