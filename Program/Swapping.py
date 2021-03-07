# Swapping values with temporary variable
def swap1(x, y):
    temp = x
    x = y
    y = temp
    print("Value of x : ", x)
    print("Value of y : ", y)

# Swapping values without temporary variable
def swap2(x, y):
    x,y = y,x
    print("Value of x : ", x)
    print("Value of y : ", y)

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

choice = input("Swapping with temporary variable? [y/n] : ")
if(choice == 'y') : swap1(num1,num2)
elif(choice == 'x') : swap2(num1,num2)