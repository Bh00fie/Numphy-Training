import numpy as np

#### ACCESSING/CHALLENGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC...
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
# print(a)

#Get the shape (it should be 2x7)
# print(a.shape)

#Get a specific element [r,c]
# print(a[0, 1]) 
# #or
# print(a[0, -6])

#Get a specific row
# print(a[:]) #To get everything in that row

#Get a specific column
# print(a[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
# print(a[0, 1:6:2])

# How to change values [this can be done in 3D as well]
# a[1,5] = 20
# print(a)

# a[:,2] = 5 #in here we change the column value of 2 to fives
# print(a)
# #or
# a[:,2] = [1,2]
# print(a)

