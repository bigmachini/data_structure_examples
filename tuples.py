'''

this are immutable objects, once created they cannot be changes just read
they are created using the brackets

myTuple = (1,2,3,4)
when writing a tuple with a single value a leading comman needs to be added

tuples can be accessed via index like list or split

tuples have the same operations are list, [len, concatenation(+), repetition(*), membership(in), iteration]
'''

#empty tuple
myTuple = ()

#one element tuple
myTuple = (1,)

#multiple element tuple, leading comman is not needed
myTuple = (1,2,3)

#index 0 value
print('index 0: {}'.format(myTuple[0]))