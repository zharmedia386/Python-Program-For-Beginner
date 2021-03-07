# Finding HCF or GCD with Euclidean Algorithm

def euclidean(x, y) :
    while(y) :
        x , y = y , x % y
    return x

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

gcd = euclidean(num1, num2)

print("So, GCD of %d and %d is %d" % (num1, num2, gcd))