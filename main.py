print("Calculator")
print("")

while True:

    function = input("Which function would you like to carry out? Please enter addition, subtraction, multiplication or division")

    num1 = float(input("Enter number 1"))
    num2 = float(input("Enter number 2"))

    if function == "addition":
        print("The answer is " , (num1 + num2))

    if function == "subtraction":
        print("The answer is " , (num1 - num2))

    if function == "multiplication":
        print("The answer is " , (num1*num2))

    if function == "division":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            result  = num1/num2
            print("The answer is " , round(result,2))

    choice = input("Would you like to perform another calculation? Answer 'no' to end the program")
    if choice == "no":
        break




