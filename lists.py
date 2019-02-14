'''
this is an array in steroid. The data doesnt have to be of the same type
List are defined using the square brackets
myList = []
'''

#function to print all list values
def printListValues(data):
    for i in data:
        print(i)
    print('=====================================')

myList = []

#data is added to lists using the append functionality
myList.append(10)
myList.append('Bigmachini')
myList.append('Osama')
myList.append(['another','list'])
printListValues(myList)

#list can also be updated with multiple values using the splice operation
myList[5:7] = ['this','is','testing']
printListValues(myList)

#data can be removed from list using del if you know the index of the data or remove if you know the value for the data
#ValueError will be thrown if the data is not found in the list
#IndexError will the thrown if the index to be deleted is not found
del myList[1]
del myList[4]
printListValues(myList)
myList.remove('Osama')
printListValues(myList)


'''
List have some basic operation + and * 
+  means concatenationn
*  means repetition
len returns the length of a list
in is used to check if value in myList
iteration like the  for x in myList: print x
'''