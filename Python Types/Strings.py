# Escape Character
print('I\'m Thirsty')
print("I'm \nThirsty")

# String Type
print(type('aadasd'))

# Multiple print | Separation
print("first line", "second line", sep=" ")
test1 = 's'
test2 = 'e'
print(test1,test2,sep="")
num1 = 2
num2 = 30
print(num1,num2,sep="")

# Indexing
print('Hey you!'[2])
print('-')
name = 'Andrei Neagoie'
print(name[4])
print(name[:])
print(name[1:])
print(name[:1])
print(name[-1])
print(name[::2])
print(name[::1])
print(name[::-1])
print(name[0:10:1]) # sampe index ke 9 (10-1)
# : is Slicing [ start : end : step ]

# Concatination Strings
print("Hello" + " World")

# String Looping
print('5'*10)

# Basic Functions
print(len('turtle'))

# Basic Methods 
"""
Stripe, replace, split, startswith, index, endswith,capitalize,upper,lower,find,count
"""

print('aI am aloneas'.strip('a')) # hapus kedua ujuang awal dan akhir
print('Help me'.replace('me','you'))
print('but life is good !'.split())
print('Need to make fire'.startswith('Nee'))
print("and cook rice".endswith('k rice'))
print('hello'.index('l'))
print('still there?'.upper())
print('Still THERE'.lower())
print("ok, I am done".capitalize())
print('hello'.find('l'))
print('ohhh'.count('h'))

# String Formatting
name1 = 'Jokowi'
name2 = 'Dodo'
print(f'Hello there {name1} {name2}')
print('Hello there {} {}'.format(name1,name2))
print('Hello there %s %s' %(name1,name2))

# Palindrom Words - Kata Keterbalikan - e.g:malam,reviver
temp = 'reviver'
print(bool(temp.find(temp[::-1])) + 1)