def main():
    stop   = ""
    choise = ""

    while (stop != "y"):
        choise = input("Input 1 to use default calculator\nInput 2 to use fractions calculator ")

        if (choise == "1"):
            input_check()
        elif (choise == "2"):
            fractions_count()
        else:
            print("No such operation. Try again")

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

def fractions_count():
    print("To make a fraction use \"/\"")

    num1 = input("Input first fraction: ")
    num2 = input("Input second fraction: ")
    oper = input("Input operation (+, -, *, /): ")
    num1_up   = ""
    num1_down = ""
    num2_up   = ""
    num2_down = ""
    separator = 0

    for i in range(len(num1) - 1):
        if (num1[i] == "/"):
            separator = i
            break

    num1_up   = int(num1[0:separator])
    num1_down = int(num1[separator + 1:len(num1)])

    for i in range(len(num2) - 1):
        if (num2[i] == "/"):
            separator = i
            break

    num2_up   = int(num2[0:separator])
    num2_down = int(num2[separator + 1:len(num2)])

    if (oper == "+"):
        if(num1_down == num2_down):
            print (num1, oper, num2, "=", str(num1_up + num2_up) + "/" + num1_down * num2_down)
        else:
            print (num1, oper, num2, "=", str(num1_up * num2_down + num2_up * num1_down) + "/" + str(num1_down * num2_down))
    elif (oper == "-"):
        if(num1_down == num2_down):
            print (num1, oper, num2, "=", str(num1_up - num2_up) + "/" + num1_down * num2_down)
        else:
            print (num1, oper, num2, "=", str(num1_up * num2_down - num2_up * num1_down) + "/" + str(num1_down * num2_down))
    elif (oper == "*"):
        print (num1, oper, num2, "=", str(num1_up * num2_up) + "/" + str(num1_down * num2_down))
    elif (oper == "/"):
        print (num1, oper, num2, "=", str(num1_up * num2_down) + "/" + str(num1_down * num2_up))
    else:
        print("No such operation. Try again")

main()