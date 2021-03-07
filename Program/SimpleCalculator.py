# Simple Calculator

def add(x,y) : return x + y
def subtract(x,y) : return x - y
def multiply(x,y) : return x * y
def divide(x,y) : return x / y

def mainMenu():
    print("="*25)
    print("\n\tMain Menu\n")
    print("="*25)
    print("")

    # Choice of operation
    print("\t[1] Add")
    print("\t[2] Subtract")
    print("\t[3] Multiply")
    print("\t[4] Divide")
    
while(True) :
    mainMenu()
    print("")
    choiceMainMenu = int(input("Enter your choice : "))
    print("")
    
    if choiceMainMenu in (1,2,3,4) :
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))
        print(num1,num2)
        if(choiceMainMenu == 1) :
            result = add(num1,num2)
            print("So, %.2f + %.2f = %.2f" % (num1, num2, result))
        elif(choiceMainMenu == 2) :
            result = subtract(num1,num2)
            print("So, %.2f - %.2f = %.2f" % (num1, num2, result))
        elif(choiceMainMenu == 3) :
            result = multiply(num1,num2)
            print("So, %.2f * %.2f = %.2f" % (num1, num2, result))
        elif(choiceMainMenu == 4) :
            result = divide(num1,num2)
            print("So, %.2f / %.2f = %.2f" % (num1, num2, result))
        back = input("\nDo you wanna go back to main menu? [yes/no] ")
        if(back == "no") : break
    else :
        print("Invalid Input")