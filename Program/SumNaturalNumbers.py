# This program is to find the sum of the certain natural number based on input number from user

def sumNaturalNumbers(x) :
    sum = 0
    for i in range(x,0,-1) :
        sum += i
    return sum 

number = int(input("Enter the number : "))

print("So, the sum of all natural numbers from %d until 0 is %d" % (number, sumNaturalNumbers(number)))