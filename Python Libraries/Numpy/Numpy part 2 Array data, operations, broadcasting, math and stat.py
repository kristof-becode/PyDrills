import numpy as np
#/////////////////Array data/////////////////
#dtype
# NumPy's ndarrays are also efficient in part because all their elements must have the same type (usually numbers). You can check what the data type is by looking at the dtype attribute:
c = np.arange(1, 5)
print(c.dtype, c) # int32 [1 2 3 4]
c = np.arange(1.0, 5.0)
print(c.dtype, c) # float64 [1. 2. 3. 4.]

# Instead of letting NumPy guess what data type to use, you can set it explicitly when creating an array by setting the dtype parameter:
d = np.arange(1, 5, dtype=np.complex64)
print(d.dtype, d) # complex64 [1.+0.j 2.+0.j 3.+0.j 4.+0.j]

#Available data types include int8, int16, int32, int64, uint8|16|32|64, float16|32|64 and complex64|128. Check out the documentation for the full list.
 #itemsize
# The itemsize attribute returns the size (in bytes) of each item:
e = np.arange(1, 5, dtype=np.complex64)
print(e.itemsize) # 8

#data buffer
# #An array's data is actually stored in memory as a flat (one dimensional) byte buffer. It is available via the data attribute (you will rarely need it, though).
f = np.array([[1,2],[1000, 2000]], dtype=np.int32)
print(f.data) #<memory at 0x0000016531D6AF28>

#dive into arrays
np.random.seed(0)
x1 = np.random.randint(10, size=6)
print(x1) #array([5, 0, 3, 3, 7, 9])

#Print the first 5 elements of an array:
print(x1[:5]) #[5 0 3 3 7]

#Print the elements from the 6th and on of an array:
print(x1[5:]) #[9]

#Print every two elements of an array:
print(x1[::2]) #[5 3 7]


# /////////////////Arithmetic operations/////////////////
# All the usual arithmetic operators (+, -, *, /, //, **, etc.) can be used with ndarrays. They apply elementwise:
a = np.array([14, 23, 32, 41])
b = np.array([5,  4,  3,  2])
print("a + b  =", a + b)
print("a - b  =", a - b)
print("a * b  =", a * b)
print("a / b  =", a / b)
print("a // b  =", a // b)
print("a % b  =", a % b)
print("a ** b =", a ** b)
"""
a + b  = [19 27 35 43]
a - b  = [ 9 19 29 39]
a * b  = [70 92 96 82]
a / b  = [ 2.8         5.75       10.66666667 20.5       ]
a // b  = [ 2  5 10 20]
a % b  = [4 3 2 1]
a ** b = [537824 279841  32768   1681]
"""

#Matrix addition and subtraction :
#As we have seen previously, in order to perform additions and subtractions of two (or more) matrices,
# it's imperative that they have the same dimensions.

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
C = A + B
print(C)
#array([[ 8, 10, 12],
 #      [14, 16, 18]])

#Same thing about subtraction...
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8,9],[10,11,12]])
C = A - B
print(C)
#array([[-6, -6, -6],
 #      [-6, -6, -6]])

# If they do not have the same dimensions, then python will execute an error.

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[7,8],[10,11]])
"""
# C = A + B
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-34-2511e030946c> in <module>
      1 A = np.array([[1,2,3],[4,5,6]])
      2 B = np.array([[7,8],[10,11]])
----> 3 C = A + B
      4 C

ValueError: operands could not be broadcast together with shapes (2,3) (2,2) 
"""

# Matrix multiplication :
# We can multiply the values of the array by a single multiplier. In this case, as can be seen all the values are multiplied by 2
C = A * 2
print("A*2 \n",C)

#For multiplication with matrix, use function dot(). But don't forget, in the case of multiplications, the number of columns of A must correspond to the number of rows of B
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2],[3,4],[5,6]])
print(A.shape, B.shape)

#And that's the case here.
C = A.dot(B)
print("C=A.dot(B) \n", C)

#As you can see we have the same results as the multiplication example above.
#But if the column number of A does not match the line name of B then we will have an error.
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,2,3],[4,5,6]])
#print(A.dot(B))

# To solve the problem we can make a transposition
BT = B.T
print("BT.shape : \n", BT.shape)

# We can now perform the multiplication
print("A.dot(BT) : \n", A.dot(BT))

#  /////////////////Broadcasting/////////////////
# In general, when NumPy expects arrays of the same shape but finds that this is not the case, it applies the so-called broadcasting rules:
#First rule // If the arrays do not have the same rank, then a 1 will be prepended to the smaller ranking arrays until their ranks match.

h = np.arange(5).reshape(1, 1, 5)
print("h = np.arange(5).reshape(1, 1, 5) :\n",h)
#Now let's try to add a 1D array of shape (5,) to this 3D array of shape (1,1,5). Applying the first rule of broadcasting!

print("h + [10, 20, 30, 40, 50] \n:", h + [10, 20, 30, 40, 50]) # same as: h + [[[10, 20, 30, 40, 50]]]

# Second rule // Arrays with a 1 along a particular dimension act as if they had the size of the array with the largest shape along that dimension. The value of the array element is repeated along that dimension.
k = np.arange(6).reshape(2, 3)
print("k = np.arange(6).reshape(2, 3) :\n",k)
#Let's try to add a 2D array of shape (2,1) to this 2D ndarray of shape (2, 3). NumPy will apply the second rule of broadcasting:
print("k + [[100], [200]] :\n",k + [[100], [200]])  # same as: k + [[100, 100, 100], [200, 200, 200]]

# Combining rules 1 & 2, we can do this:

print("k + [100, 200, 300] :\n",k + [100, 200, 300]  )  # after rule 1: [[100, 200, 300]], and after rule 2: [[100, 200, 300], [100, 200, 300]]

#And also, very simply:

print("k + 1000 \n", k + 1000)  # same as: k + [[1000, 1000, 1000], [1000, 1000, 1000]]

# /////////////////Mathematical and statistical functions/////////////////
# Many mathematical and statistical functions are available for ndarrays.
#ndarray methods
#Some functions are simply ndarray methods, for example:
a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
print("a \n", a)
print("mean a =", a.mean())

# Note that this computes the mean of all elements in the ndarray, regardless of its shape.

# Here are a few more useful ndarray methods:
for func in (a.min, a.max, a.sum, a.prod, a.std, a.var):
    print(func.__name__, "=", func())

# These functions accept an optional argument axis which lets you ask for the operation to be performed on elements along the given axis. For example:
c=np.arange(24).reshape(2,3,4)
print("matrix c \n", c)

print("sum across matrices, c.sum(axis=0) :  \n", c.sum(axis=0), "\n")  # sum across matrices
print("sum across rows, c.sum(axis=1) : \n",c.sum(axis=1), "\n")  # sum across rows
print("sum across matrices and columns, c.sum(axis=(0,2)): \n",c.sum(axis=(0,2)), "\n")  # sum across matrices and columns
"""
0+1+2+3 + 12+13+14+15, 4+5+6+7 + 16+17+18+19, 8+9+10+11 + 20+21+22+23
"""
#/////////////////Universal functions/////////////////
#NumPy also provides fast elementwise functions called universal functions, or ufunc. They are vectorized wrappers of simple functions. For example square returns a new ndarray which is a copy of the original ndarray except that each element is squared:
a = np.array([[-2.5, 3.1, 7], [10, 11, 12]])
print("matrix a : \n", a )
print("a squared : \n", np.square(a), "\n")

#Here are a few more useful unary ufuncs:
print("Original ndarray")
print(a)
for func in (np.abs, np.square, np.exp, np.sign, np.ceil, np.modf, np.isnan, np.cos): # isnan : True where x is NaN, false otherwise.
    print("\n", func.__name__)
    print(func(a))