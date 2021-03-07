# This program is to check the input year, whether including a leap year or not
# if the input year divisible by 400, So that's definitely a leap year
# if the input year not divisible by 400, but divisible by 100, So that's not a leap year
# if the input year not divisble by 400 and 100, but divisible by 4, So that's a leap year
# if the input year not divisible by 400, 100 and 4, So that's definitely not a leap year

def input_year() :
    year = int(input("Enter for the year : "))
    return year

def leapYear() :
    year = input_year()
    if(year % 4 == 0):
        if(year % 100 == 0) :
            if(year % 400 == 0) :
                print("{0} is a leap year".format(year))
            else :
                print("{0} is not a leap year".format(year))
        else :
            print("{0} is a leap year".format(year))
    else :
        print("{0} is not a leap year".format(year))

if __name__ == "__main__" :
    leapYear()