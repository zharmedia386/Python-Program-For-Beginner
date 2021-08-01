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
basket = basket.pop()
print(basket)
basket.pop('oranges')