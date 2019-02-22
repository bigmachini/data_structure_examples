'''
This is a data structure that used key value pairs
each key is separated from value by a full colon(:)
while each entry is seperated from the other by a comma(,)

to access values in a dictionary you have to know the key to see the value
myDict = {'one' : 1, 'two': 2, 'three' : 3}

if a key is not found in the dictionary a KeyError will be raised

Dictionaries can be updated if one knows the key
myDict['key'] = newValue

To remove elements from the dictionary we use:
del myDict['key']  - this removes the data with the key
To clear a whole dictionary we use:
myDict.clear() - this will removes everything from the dictionary

if you try to del an index not in the dictionary you will get a KeyError exception

'''
#creating and initializing a dictionary
myDict = {'one' : 1, 'two': 2, 'three' : 3}
print("myDict['one'] : {}".format(myDict['one']))

#updating the value of key - one
myDict['one'] = 'this is a test to see if this works'
print("myDict['one'] : {}".format(myDict['one']))

myDict['me']