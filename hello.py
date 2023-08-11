import numpy as np

a = np.array([1, 2, 3], dtype="int16")
print(a)
print("Dimensions of 'a' array:", a.ndim)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)
#Get dimensions (How many rows)
print("Dimensions of 'b' array:", b.ndim)

#Get shape
print(b.shape)

#What kind of data type is our code/variable is being store as we can use "dtype" (also when defining the variable we can set what kind of data type we want), smaller the data type less memory is being used
print(a.dtype)

#Get size
print(a.itemsize) #2 bites, if it was int32 then the size would have been 4 bites for number

#Get total size (how many element)
print(a.size)

#So total weight is going to be 6 bites if data is being store as int16
print(a.nbytes)


