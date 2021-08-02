"""
Also known as mappings or hash tables. They are key value pairs that are guaranteed 
to retain order of insertion starting from Python 3.7
"""

myDict = {'name' : 'Andre','age' : 30}
print(myDict['name'])
print(len(myDict))
print(myDict.get('age'))
print(myDict.get('ages','salah')) # jika gaada ages, maka salah

# List
print(list(myDict.keys()))
print(list(myDict.values()))
print(list(myDict.items()))

# Menambah keys dan value baru
myDict['magicPower'] = False
print(myDict)
myDict.update({'cool' : True})
print(myDict)

# Remove Key
del myDict['name']
print(myDict)
myDict.pop('magicPower')
print(myDict)

# Dictionaries | List
newDict = dict([['name','Andre'],['age',30]]) #pairs
print(newDict)
newDict = dict(zip(['name','age'],['Andre',30])) #two collocation
print(newDict)
