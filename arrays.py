from array import *
#arrayName = array(typecode, [initializers])
'''
There are different types of bytecode
b - signed integer 1 byte
B - unsigned integer 1 byte
c - character size 1 byte
i - signed integer 2 bytes
I - signed integer 2 bytes
f - floating point 4 bytes
d - floating point 8 bytes
'''
intArray = array('i',[1,2,3,4,5])

def printArray(data):
    for i in data:
        print ('{} '.format(i))
    print('===================================')
 #accessing an array one uses the index arrayName[index]
 #one cannot access indexs outside the predefined array size you will get an exception
print('index 0: {}'.format(intArray[0]))
print('index 1: {}'.format(intArray[1]))

#insertion can be done using the insert operator you specify the index of insertion
#arrayName.insert(index, value) the value has to match the value the array holds
intArray.insert(2,5)
printArray(intArray)

#deletion can be done using the remove inbuilt function, this removes the value at a given index
#arrayName.remove(index)
intArray.remove(4)
printArray(intArray)

#searching an array can be done using the index operation that returns the index of the value, it will throw a value Error if
#the value is not found in the array
#arrayName.index(value)
print(intArray.index(5))

#updating an array is done using the index, the index needs to be within the bounds of the array
#arrayName[index] = newValue
intArray[0] = intArray[0]  * 10
print('intArray[0]: {}'.format(intArray[0]))