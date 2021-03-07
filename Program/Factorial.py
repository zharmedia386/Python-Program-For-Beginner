# This program is to find the faktorial of the input number

def factorial(x) :
    result = 1
    for i in range(x, 0, -1) :
        result *= i
    return result


number = int(input("Enter the number : "))
print("So, %d! is %d" % (number, factorial(number)))