def main():
    stop = ""

    while (stop != "y"):
        input_check()

        stop = input("Would you like exit (Y/y - yes, other - continue)? ").lower()

def input_check():
    try:
        num1 = int(input("Input first number: "))
        num2 = int(input("Input second number: "))
        oper = input("Input operation (+, -, *, /): ")

        count(num1, num2, oper)
    except:
        print("Invalid input. Try again")

def count(num1, num2, oper):
    if (oper == "+"):
        print (num1, oper, num2, "=", num1 + num2)
    elif (oper == "-"):
        print (num1, oper, num2, "=", num1 - num2)
    elif (oper == "*"):
        print (num1, oper, num2, "=", num1 * num2)
    elif (oper == "/"):
        print (num1, oper, num2, "=", num1 / num2)
    else:
        print("No such operation. Try again")

main()