while True:
    firstNumber = input("enter first number pls (q to exit) :  ")

    if firstNumber == "q":
        break

    secondNumber = input("enter second number pls (q to exit) : ")
    if firstNumber == "q":
        break

    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)

    firstNumber *= firstNumber
    print("first number's square:", firstNumber)

    if firstNumber % secondNumber == 0:
        print(f"{firstNumber} is completely divisible by {secondNumber}")
        print("result: ", firstNumber / secondNumber)
        break
    else:
        print(f"{firstNumber} is not completely divisible by {secondNumber}")
        break
