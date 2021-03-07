# This program is to check the input number, whether including odd or even
# If input number mod 2 == 0, so that's an even number
# If input number mod 2 != 0, so that's an odd number

def input_number() :
    number = int(input("Enter your number : "))
    return number

def checking_number() :
    number = input_number()
    if(number % 2 == 0) : print("%d is an even number" % number)
    elif(number % 2 != 0) : print("%d is an odd number" % number)

if __name__ == "__main__" :
    checking_number()