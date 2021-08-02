myList = [1,2,3]
myTuple = (4,5,6)
myDict = {'name' : 'Andre','age' : 30}
mySet = {7,8,9}

for num in myList :
  print(num,end='')

print()

for a,b in myDict.items() :
  print(a,b)

for a in myDict.items() :
  print(a)

for num in '123' :
  print(num,end=' ')

print()

# Range(start,end,step)
for i in range(1,10,2) :
  print(i,end='')

print('\n' + str(list(range(0,10,2))))

# While Loop
print('-----')
msg = ''
while msg != 'quit':
 msg = input("What should I do?")
 print(msg)
