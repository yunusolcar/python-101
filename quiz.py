while True:
    first_number = input("enter first number pls (q to exit) :  ")

    if first_number == "q":
        break

    second_number = input("enter second number pls (q to exit) : ")
    if second_number == "q":
        break

    first_number = int(first_number)
    second_number = int(second_number)

    first_number *= first_number
    print("first number's square:", first_number)

    if first_number % second_number == 0:
        print(f"{first_number} is completely divisible by {second_number}")
        print("result: ", first_number / second_number)
        break
    else:
        print(f"{first_number} is not completely divisible by {second_number}")
        break
        
        