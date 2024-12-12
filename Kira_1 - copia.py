# =============================================================================
#  LIBRARIES
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# DATA
x = np.linspace(0, 1, 10)
y = np.sin(x)

# PLOT

plt.plot(x,y)
plt.grid()
plt.xlabel('mati', fontsize=10)
plt.ylabel('cata', fontsize=20)
plt.show()
print(11//2)


dict_={'a':[11,21,31],'b':[12,22,32]}
df = pd.DataFrame(dict_)
df.head()
df.mean()

# Creating a 2D array
arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])

#Indexing and slicing
print(arr_2d[2])
print(arr_2d[1,2])
print(arr_2d[:,1])

#Array addition
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
result = array1 + array2
print(result)

#Scalar multiplication
array = np.array([1,2,3])
result = array * 2
print(result)

#Element-wise multiplication
array3 = np.array([1,2,3]) 
array4 = np.array([4,5,6])
result = array3*array4
print(result)

#Matrix multiplication
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])
result = np.dot(matrix1, matrix2)
print(result)


