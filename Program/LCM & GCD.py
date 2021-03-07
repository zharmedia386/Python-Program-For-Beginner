# This program is to find the LCM of the input number

def lcm(x,y) :
    if(x > y) :
        if(x % y == 0) :
            result = x
            return result
        temp = x
        while(x % y != 0) :
            x = temp + x
        result = x
        return result
    elif(y > x) :
        if(y % x == 0) :
            result = y
            return result
        temp = y
        while(y % x != 0) :
            y = temp + y
        result = y
        return result

def gcd(x,y) :
    if(x > y) :
        temp = y - 1
        while(x % temp != 0 or y % temp != 0) :
            temp -= 1
        return temp
    elif(y > x) :
        temp = x - 1
        while(x % temp != 0 or y % temp != 0) :
            temp -=1
        return temp
if __name__ == "__main__" :
    number_1 = int(input("Enter the first number : "))
    number_2 = int(input("Enter the second number : "))

    print("LCM of %d and %d is %d" % (number_1, number_2, lcm(number_1, number_2)))
    print("GCD of %d and %d is %d" % (number_1, number_2, gcd(number_1, number_2)))