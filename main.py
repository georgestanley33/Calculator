print("Calculator")
print("")

while True:

    function = input("Which function would you like to carry out? Please enter +, -, /, or *")

    num1 = float(input("Enter number 1"))
    num2 = float(input("Enter number 2"))

    if function == "+":
        print("The answer is " , (num1 + num2))

    if function == "-":
        print("The answer is " , (num1 - num2))

    if function == "*":
        print("The answer is " , (num1*num2))

    if function == "/":
        if num2 == 0:
            print("Cannot divide by 0")
        else:
            result  = num1/num2
            print("The answer is " , round(result,2))

    choice = input("Would you like to perform another calculation? Answer 'no' to end the program")
    if choice == "no":
        break




