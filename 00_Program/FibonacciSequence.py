# This program is used to make a fibonacci sequence in a certain terms

def fibonacci(term) :
    n1 = 0
    n2 = 1
    if(term <= 0) :
        print("Please, print with positive integer")
    elif(term == 1) :
        print(n1)
    else :
        print(n1)
        print(n2)

        count = 1
        while(count <= term-2) :
            n_update = n1 + n2
            # Update number
            n1 = n2
            n2 = n_update
            print(n2)
            count += 1

input_number = int(input("How many terms? "))

fibonacci(input_number)