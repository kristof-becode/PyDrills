# 100 numpy exercises
# This is a collection of exercises that have been collected in the numpy mailing list, on stack overflow and in the numpy documentation. The goal of this collection is to offer a quick reference for both old and new users but also to provide a set of exercises for those who teach.

# 1. Import the numpy package under the name np (★☆☆)
import numpy as np

# 2. Print the numpy version and the configuration (★☆☆)
print("version :", np.__version__)
print(np.show_config())

# 3. Create a null vector of size 10 (★☆☆)
v = np.zeros((10))
print(v)

# 4. How to find the memory size of any array (★☆☆)
f = np.array([[1,2],[1000, 2000]], dtype=np.int32)
print(f.data)

#5. How to get the documentation of the numpy add function from the command line? (★☆☆)
        #python -c "import numpy; numpy.info(numpy.add)"

#6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)
v = np.zeros((10))
v[4] = 1
print(v)

#7. Create a vector with values ranging from 10 to 49 (★☆☆)
v = np.arange(10,50,1)
print(v)
v2 = np.arange(10,50,3)
print(v2)

#8. Reverse a vector (first element becomes last) (★☆☆)
v = np.array([1,2,3,4,5,6])
v = v[::-1]
print(v, "\n")

#9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
np.random.seed(0)
matrix = np.random.randint(0, 8, size=(3,3))
print("3x3 random matrix: \n", matrix,"\n")

#10. Find indices of non-zero elements from [1,2,0,0,4,0] (★☆☆)
ar = np.array([1,2,0,0,4,0])
print("ar : \n", ar)
b = np.where(ar != 0 )
print("indices waar !=0 \n", b)
print("array van die elem != 0 \n", ar[b], "\n") # print from ar the array with values != 0, or sub array b

#11. Create a 3x3 identity matrix (★☆☆)
id = np.eye(3)
print("unity matrix : \n", id)

#12. Create a 3x3x3 array with random values (★☆☆)
np.random.seed(0)
matrix = np.random.randint(-10000, 10000, size=(3,3,3))
print("3x3x3 random matrix: \n", matrix,"\n")

#13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)
np.random.seed(0)
matrix = np.random.randint(-10000, 10000, size=(10,10))
print("3x3x3 random matrix: \n", matrix,"\n")
print("min value: ", matrix.min())
print("max value: ",matrix.max())
print("\n")

#14. Create a random vector of size 30 and find the mean value (★☆☆)
np.random.seed(0)
matrix = np.random.randint(50, size=30)
print(matrix)
print("mean value is :" , matrix.mean())
print("\n")

#15. Create a 2d array with 1 on the border and 0 inside (★☆☆)
ar = np.array([[1,1,1,1],[1,0,0,1],[1,0,0,1],[1,1,1,1]])
print("start matrix: \n", ar)
print("\n")

#16. How to add a border (filled with 0's) around an existing array? (★☆☆)
arZero4 = np.zeros((1,4)) # make matrix(vector) to add above and below vertically, so shape(1,4)
arZero6 = np.zeros((6,1)) # make matrix(vector) to add left and right horizontally after adding vectors vertically, so shape(6,1)
vertAr = np.vstack([arZero4, ar, arZero4])
horAr = np.hstack([arZero6, vertAr, arZero6])
print("now with borders of 0's : \n", horAr, "\n")

# 17. What is the result of the following expression? (★☆☆)
# !!!!!!!!!!!!!nan is NotANumber so also not 0, inf is Infinity or greater than any other value
print("nan is NotANumber so also not 0, inf is Infinity or greater than any other value")
print("0 * np.nan :", 0 * np.nan) # nan
print("np.nan == np.nan :", np.nan == np.nan) #always False
print("np.inf > np.nan :", np.inf > np.nan) #False
print("np.nan - np.nan : ", np.nan - np.nan) # nan
print("np.nan in set([np.nan]) :", np.nan in set([np.nan])) # True
print("https://docs.python.org/3/tutorial/floatingpoint.html, 0.3 and 0,1 are binary fractions")
print("0.3 == 3 * 0.1 :" , 0.3 == 3 * 0.1) # False
print("\n")

#18. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal (★☆☆)
matrix  = np.zeros((5,5), dtype=int)
vals = [(1),(2),(3),(4)]
indices = [(1, 0), (2, 1), (3, 2), (4, 3)]
matrix[tuple(np.transpose(indices))] = vals
print("5x5 with 1,2,3,4 just below diagonal : \n", matrix)
print("\n")
# other way:
matrix = np.diag(1+np.arange(4), k = -1)
print("diff way: \n", matrix)
print("\n")

#19. Create a 8x8 matrix and fill it with a checkerboard pattern (★☆☆)
ar1 = np.array([1,0,1,0,1,0,1,0])
ar2 = np.array([0,1,0,1,0,1,0,1])
checkerBoard = np.vstack([ar1, ar2, ar1, ar2, ar1, ar2, ar1, ar2]) # easy
print("checker board via stack: \n" , checkerBoard, "\n")
# OR more clever:
checkerBoard = np.zeros((8,8), dtype=int)
checkerBoard[1::2,::2] = 1
checkerBoard[::2,1::2] = 1
print("clever checker board via run thru indices: \n" , checkerBoard, "\n")

#20. Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element?
np.random.seed(0)
matrix = np.random.randint(-10000, 10000, size=(6,7,8))
#print(matrix)
count = 0
print(len(matrix)) # geeft alleen z-as, nl. 6
print(matrix.size) # gives 336, being total elements in this 3D array, 7x8x6
for z in matrix:
    for y in z:
        for x in y:
            count += 1
            #if count == 100:
                #print(np.where(matrix(100) == True))
#print(count)
#OR:
print("index 100th element with np.unravel :", np.unravel_index(100, (6,7,8)))

#21. Create a checkerboard 8x8 matrix using the tile function (★☆☆)
matrix = np.tile(np.array([[1,0],[0,1]]),(4,4))
print("chekerboard with np.tile : \n ", matrix, "\n")

#22. Normalize a 5x5 random matrix (★☆☆)


#23. Create a custom dtype that describes a color as four unsigned bytes (RGBA) (★☆☆)


#24. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) (★☆☆)
np.random.seed(0)
mat1 = np.random.randint(-10000, 10000, size=(5,3))
mat2 = np.random.randint(-10000, 10000, size=(3,2))
mult = mat1.dot(mat2)
print("multiplication  with .dot() \n ", mult, "\n")

#25. Given a 1D array, negate all elements which are between 3 and 8, in place. (★☆☆)
matrix = np.arange(0,10)
print(matrix)
print(np.negative(matrix))
print(np.where((matrix<=8) & (matrix>=3)))# need to use & !!!!!!!!! not and
#actual code that got it done is this:
matrix[(matrix<=8)& (matrix>=3)] *= -1
print(matrix, "\n")

#26. What is the output of the following script? (★☆☆)

# Author: Jake VanderPlas
print("sum(range(5),-1), regular sum: 0+1+2+3+4 -1 =9     ", sum(range(5),-1)) # regular sum: 0+1+2+3+4 -1 =9
from numpy import *
print("np.sum     ", sum(range(5),-1)) # np.sum , see below
#sum iterates over supplied iterable, sums the values, and then adds -1 (i.e. substracts 1). numpy.sum just sums all the values
#from supplied iterable, and receives an axis parameter as 1, which in your case doesn't change the behaviour.

#27. Consider an integer vector Z, which of these expressions are legal? (★☆☆)
Z = np.arange(0,10,dtype=int)
print(Z) # [0 1 2 3 4 5 6 7 8 9]
print(Z**Z) #legal
print(2 << Z >> 2) # legal, << >> bit shift operators, x = x * 2^z, results in [  0   1   2   4   8  16  32  64 128 256] or powers of 2,
print(Z <- Z) # legal, reads Z < (-Z) ~ False
print(1j*Z) # legal, [0.+0.j 0.+1.j 0.+2.j 0.+3.j 0.+4.j 0.+5.j 0.+6.j 0.+7.j 0.+8.j 0.+9.j]
print(Z/1/1) #legal, [0. 1. 2. 3. 4. 5. 6. 7. 8. 9.]
# print(Z<Z>Z) # error

#28. What are the result of the following expressions?
#np.array(0) / np.array(0) # RuntimeWarning: invalid value encountered in true_divide
#np.array(0) // np.array(0) # RuntimeWarning: divide by zero encountered in floor_divide
print(np.array([np.nan]).astype(int).astype(float)) # [-9.22337204e+18]
print("\n")

#29. How to round away from zero a float array ? (★☆☆)
fltArr = np.arange(0, 10, 0.2, dtype=float)
print("float array :\n ", fltArr )
print("now rounded up: \n", np.ceil(fltArr))
print("\n")

#30. How to find common values between two arrays? (★☆☆)
np.random.seed(0)
m1 = np.random.randint(-20, 20, size=(5,3))
m2 = np.random.randint(-20, 20, size=(3,2))
print("m1: \n", m1,"\n","m2: \n",m2)
print("common values : \n", np.intersect1d(m1,m2))
print("\n")

#31. How to ignore all numpy warnings (not recommended)? (★☆☆)
# warnings.filterwarnings('ignore') #warnings module

#32. Is the following expressions true? (★☆☆)
#print(np.sqrt(-1) == np.emath.sqrt(-1)) # False and also RuntimeWarning: invalid value encountered in sqrt
#square root of negative numbers?

#33. How to get the dates of yesterday, today and tomorrow? (★☆☆)
print("yesterday : ", np.datetime64('today') - np.timedelta64(1,'D'))
print("today : ", np.datetime64('today'))
print("tomorrow :", np.datetime64('today') + np.timedelta64(1,'D'))
print("\n")

#34. How to get all the dates corresponding to the month of July 2016? (★★☆)
print("July 2016 : \n", np.arange('2016-07', '2016-08', dtype='datetime64[D]'))
print("\n")

#35. How to compute ((A+B)*(-A/2)) in place (without copy)? (★★☆)
np.random.seed(0)
A = np.random.randint(-10000, 10000, size=(5,3))
B = np.random.randint(-10000, 10000, size=(5,3))
#print(A+B)
#(A+B).dot(np.negative(A/2))

print("\n")


#36. Extract the integer part of a random array using 5 different methods (★★☆)
matrix = np.arange(0,5, 0.5, dtype=float64)
print(matrix)
intma = matrix[type(matrix) == int] # type does not work
print(intma)
intma = matrix[matrix == matrix.astype(int)]
print(intma)
intma = np.extract(type(matrix) == int, matrix) # type does not work
print(intma)
intma = np.extract(matrix == matrix.astype(int), matrix)
print(intma)
#intma = np.extract(matrix == ((str(matrix)).split('.'))[1] is None, matrix)
#print(intma)
print(np.where(matrix == matrix.astype(int)))
intma = np.extract(np.where(matrix == matrix.astype(int)), matrix) # weird!!!
print(intma)

#37. Create a 5x5 matrix with row values ranging from 0 to 4 (★★☆) # if row values have condition, this means that the matrix has samz condition
np.random.seed(0)
matrix = np.random.randint(1,5, size=(5,5))
print(matrix)
print("\n")

#38. Consider a generator function that generates 10 integers and use it to build an array (★☆☆)


#39. Create a vector of size 10 with values ranging from 0 to 1, both excluded (★★☆)
#matrix = np.arange()
matrix = np.linspace(0, 1, 11, endpoint=False)
matrix = matrix[1:len(matrix)]
print(matrix)
print("\n")

#40. Create a random vector of size 10 and sort it (★★☆)
np.random.seed(0)
matrix = np.random.randint(200, size=10)
print("random matrix : \n", matrix)
matrix.sort()
print("sorted matrix : \n",matrix,"\n")

#41. How to sum a small array faster than np.sum? (★★☆)
np.random.seed(0)
A = np.random.randint(200, size=4)
print("matrix to sum: ", A)
from time import perf_counter
#with np.sum
start = perf_counter()
sum1 = np.sum(A)
end = perf_counter()
print("sum with np.sum :", sum1, " ,time : ", (end-start))
# with sum
start = perf_counter()
sum2 = sum(A[::1])
end = perf_counter()
print("sum with sum :", sum2," ,time : ",(end-start))
print("\n")

#42. Consider two random array A and B, check if they are equal (★★☆)
np.random.seed(0)
A = np.random.randint(-200, 200, size=(4,4))
B = np.random.randint(-200, 200, size=(5,4))
print(A==B) # False because dimensions are not equal
A = np.random.randint(-200, 200, size=(4,4))
B = np.random.randint(-200, 200, size=(4,4))
print(A==B) # same dimensions, returns matrix full of False- so per element
A = np.random.randint(-200, 200, size=(4,4))
B = np.random.randint(-200, 200, size=(4,4))
print(np.array_equal(A,B))
print("\n")

#43. Make an array immutable (read-only) (★★☆)
B.flags.writeable = False
# B[0] = 4 # returns ValueError: assignment destination is read-only

#44. Consider a random 10x2 matrix representing cartesian coordinates, convert them to polar coordinates (★★☆)
# dus van [x y] ->
# x=r cos(θ) y=r sin(θ) en
# r=√(x2+y2) θ= arctan(y/x)
np.random.seed(0)
cart = np.random.randint(10, size=(10,2))
print("cartesian coordinates : \n", cart)
squa = np.square(cart)
print(squa)
sum1 = squa.sum(axis=1)
print(sum1)
sumT = sum1.T #need to transpose again
print(sumT)

# polar =
print("\n")

#45. Create random vector of size 10 and replace the maximum value by 0 (★★☆)
np.random.seed(0)
matrix = np.random.randint(10, size=10)
print("matrix : " , matrix)
print("maxwaarde vervangen door 0 met np.where :", np.where(matrix == matrix.max(), 0, matrix))
print("\n")

#46. Create a structured array with x and y coordinates covering the [0,1]x[0,1] area (★★☆)


print("\n")
#47. Given two arrays, X and Y, construct the Cauchy matrix C (Cij =1/(xi - yj))


print("\n")
#48. Print the minimum and maximum representable value for each numpy scalar type (★★☆)


print("\n")
#49. How to print all the values of an array? (★★☆)


print("\n")
#50. How to find the closest value (to a given scalar) in a vector? (★★☆)

