"""
List = String yang mutable
dapat diganti nilainya
Index dimulai dari 0
"""

myList = [1,2,'3',True]

print(len(myList))
print(myList.index('3'))
print(myList[1:]) # Start,End,Step : 1,akhir(default),1
print(myList[1:2]) # Start,End,Step : mulai dari satu berhenti di (2-1)
print(myList[::2]) # Start,End,Step : 0,akhir(default),2
print(myList[0:3:2])
print(myList[::-1]) # Start,End,Step : 0,akhir(default),-1


# Add To Lists
print('-----')
print(myList * 2)
myList = myList + [10]
print(myList)
print(myList.append(10))
print(myList.extend([22]))
print(myList.insert(2,'111'))
print('ss'.join(['Hello','World']))


# Copy a List
print('---')
basket = ['apples','pears','oranges']
basket2 = basket.copy()
print(basket2)
print(basket[:])


# Remove from list
print('----')
basket.pop()
print(basket)
print([1,2,3].clear())


# Ordering
print('----')
number = [1,4,2]
print(number.sort())
print(sorted(number))
print(list(reversed([1,4,3,0])))


# Useful Functios
print('----')
print(1 in [1,2,3,4,5])
print(min([1,2,3,4,5]))
print(max([1,2,3,4,5]))
print(sum([1,2,3,4,5]))


# Get First and Last Elemnt
number = [1,2,3,4,5]
first,*x,last = number
print(first)
print(last)


# Matrix
print('----')
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix[2][0])
print(matrix[1][2])


# Looping through a matrix by rows
mx = [[1,2,3],[4,5,6]]
for row in range(len(mx)) :
  for col in range(len(mx[0])) :
    print(mx[row][col],end='')


# List Comprehensions
# new_list[<action> for <item> in <iterator> if <some condition>]
print('\n----')
print([i for i in 'hello'])
print([i*2 for i in [1,2,3]])
print([i for i in range(0,10) if i % 2 == 0])


print(list('Hello'))

new_list = [1,2,'contoh']
print(new_list)