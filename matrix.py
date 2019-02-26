'''
This are special 2-D arrays that have the same number of columns for each row
every matrix is a 2-D array but not all 2-D array are matrices

matrix are used for mathematical and scientific purposes

matrix are accessed the same way a arrays using row and column numbers
'''

#recording of temperature for a week measured 4 times a day(morning, mid-day,evening, mid-night)
from numpy import *
a = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
		   ['Wed',15,21,20,19],['Thu',11,20,22,21],
		   ['Fri',18,17,23,22],['Sat',12,22,20,18],
		   ['Sun',13,15,19,16]])

m = reshape(a, (7,5))
print(m)