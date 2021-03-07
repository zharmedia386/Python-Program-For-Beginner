# This program is used to check the input number, whether prime or not

def prime(x) :
    counter = 0
    for i in range(x-1,1,-1) :
        if(x % i == 0) :
            counter = 1
    if(counter == 0) :
        return 5
    elif(counter == 1) :
        return 4

input_number = int(input("Enter the number : "))

if(prime(input_number) == 5) :
    print("%d is prime number" % input_number)
elif(prime(input_number) == 4) :
    print("%d is not prime number" % input_number)