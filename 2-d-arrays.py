'''
This is an array of arrays where data is accessed via two indicies, one representing the row number and another representing the column number
if the column number is no provided the whole array in that row is displayed

insertion, deletion and updating of a 2-D array is similar to those of a regular array with just an extra index

del T[r] will delete all contents in row r
del T[r][c] will delete value at row r and column c

T.insert(r, value) this will insert value at index r

'''

from array import *
import sys
T = [[1,2,3,4,5], [6,7,8,9,0,11], [34,54,66]]

#accessing the first row elements
print(T[0])

#accessing the 3 element in the second row
print(T[1][3])

#printing put an array
def print_out_array(data, source_file=sys.stdout):
    for r in data:
        for c in r:
            print(c, end=" ", file=source_file)
        print(file=source_file)

source_file = open('./output.txt', 'w')
print_out_array(T)
print_out_array(T, source_file)
source_file.close()