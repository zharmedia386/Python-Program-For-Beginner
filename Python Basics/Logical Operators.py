"""

1 < 2 and 4 > 1 # True
1 > 3 or 4 > 1 # True
1 is not 4 # True
not True # False
1 not in [2,3,4]# True
if <condition that evaluates to boolean>:
 # perform action1
elif <condition that evaluates to boolean>:
 # perform action2
else:
 # perform action

"""

print(1 < 2 and 4 > 1)
Tuple = (1,2,3)
print(4 not in Tuple)

char = 'exam'
print(char is not 'exam')
print(char is 'exam')

num1 =int(input("Enter the number : "))
if(num1 % 5 == 0) :
  print('Yes1')
elif(num1 % 3 == 0) :
  print('Yes2')
else : 
  print('Yes3')