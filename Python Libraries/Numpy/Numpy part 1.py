import numpy as np

# Creating arrays

# Let's create an array numpy with two rows and three columns.
A = np.array([[1,2,3],[4,5,6]])
print(A)
# gives : array([[1, 2, 3],
       #        [4, 5, 6]])


# The dimensions of the array can be displayed using the shape property
print("shape ", A.shape) # gives : (2, 3)

# np.zeros
# The zeros function creates an array containing any number of zeros:
np.zeros(5)
print("zeros ", np.zeros(5)) # gives array([0., 0., 0., 0., 0.])


# It's just as easy to create a 2D array (ie. a matrix) by providing a tuple with the desired number of rows and columns. For example, here's a 2x3 matrix:
zeros = np.zeros((2,3))
print("zeros \n", zeros)
# gives : array([[0., 0., 0.],
       #        [0., 0., 0.]])

# np.ones
# We can do the same thing with an array filled with 1
ones = np.ones((2,3))
print("ones \n", ones)
#gives : array([[1., 1., 1.],
       #        [1., 1., 1.]])


# np.arange
# We can also create an array with a range.
print('np.arange')
print(np.arange(10)) # gives : array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#Like the range() function in python, we can also indicate the start point, the end point and the step.
#np.arange(start, end, step)
print(np.arange(0, 10, 2)) # gives: array([0, 2, 4, 6, 8])


#np.linspace
# Create an array of 5 numbers, linearly spaced between 0 and 1
print("linespace ", np.linspace(0, 1, 5)) # array([0.  , 0.25, 0.5 , 0.75, 1.  ])

#np.eye
#Returns the identity matrix of size 3. An identity matrix return a 2-D array with ones on the diagonal and zeros elsewhere.
print("identity matrix w/ np.eye \n", np.eye(3))
#array([[1., 0., 0.],
 #      [0., 1., 0.],
  #     [0., 0., 1.]])
a = np.zeros((3,4))
print("zeros \n", a)
#array([[0., 0., 0., 0.],
 #      [0., 0., 0., 0.],
  #     [0., 0., 0., 0.]])
print("shape ", a.shape) # (3, 4)
#a.ndim # equal of len(a)
print("ndim ", a.ndim) #2
print("size", a.size) #12 #number of elements = n*m

# np.concatenate
# Concentrate or join arrays
print("Concatenate")
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
print(np.concatenate([x, y])) # array([1, 2, 3, 3, 2, 1])

# If the arrays are multidimensional, you can use either vstack (vertical) or hstack (horizontal).
x = np.array([1, 2, 3])
grid = np.array([[9, 8, 7], [6, 5, 4]])
print(np.vstack([x, grid]))
#array([[1, 2, 3],
 #      [9, 8, 7],
  #     [6, 5, 4]])

# N-dimensional arrays
# You can also create an N-dimensional array of arbitrary rank. For example, here's a 3D array (rank=3), with shape (2,3,4):
print("3D \n", np.zeros((2,3,4)))
#array([[[0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
  #      [0., 0., 0., 0.]],
#
 #      [[0., 0., 0., 0.],
  #      [0., 0., 0., 0.],
   #     [0., 0., 0., 0.]]])

#Array type
#NumPy arrays have the type ndarrays:
print(type(np.zeros((2,3,4)))) # <class 'numpy.ndarray'>

#np.full
#Creates an array of the given shape initialized with the given value. Here's a 3x4 matrix full of π.
print("np.full \n", np.full((3,4), np.pi))
#array([[3.14159265, 3.14159265, 3.14159265, 3.14159265],
    #   [3.14159265, 3.14159265, 3.14159265, 3.14159265],
     #  [3.14159265, 3.14159265, 3.14159265, 3.14159265]])

#np.empty
#An uninitialized 2x3 array (its content is not predictable, as it is whatever is in memory at that point):
print("np.empty \n", np.empty((2,3)))
#array([[1., 1., 1.],
 #      [1., 1., 1.]])
#
#np.random
#A number of functions are available in NumPy's random module to create ndarrays initialized with random values. For example, here is a 3x4 matrix initialized with random floats between 0 and 1 (uniform distribution):
print("random \n", np.random.random((3,4)))
#array([[0.21064871, 0.51084367, 0.04462232, 0.15474993],
 #      [0.48943545, 0.17311007, 0.6829123 , 0.48621628],
  #     [0.33423204, 0.84978756, 0.35483656, 0.56232577]])
