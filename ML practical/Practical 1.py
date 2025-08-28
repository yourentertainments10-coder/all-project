import numpy as np
arr=np.array([1,2,3,4,5])
# 1. Creating Arrays
# 1D array
arr1D = np.array([2,4,6,8])
print("1D Array:\n", arr1D)

# 2D array
arr2D = np.array([[1, 2, 3], [4, 5, 6]])
print("\n2D Array:\n", arr2D)

# 3D array
arr3D = np.array([[[11,12], [13, 14]],
                  [[15, 16], [17, 18]]])
print("\n3D Array:\n", arr3D)


# 2. Indexing and Slicing
# Indexing in 1D
print("\n1D Indexing: arr1D[2] =", arr1D[:3])  
print("\n1D Indexing: arr2D[0][2] =", arr2D[0][2])
print("\n1D Indexing: arr3D[1][0][2] =", arr3D[1][0][1])
# Slicing in 1D
print("1D Slicing:  arr1D[0] =", arr1D[0]) 
print("1D Slicing: arr2D[1][0:2] =", arr2D[1][0:2])
print("1D Slicing: arr3D[1][1][0:] =", arr3D[1][1][0:])

# 3. Reshaping

reshaped = arr1D.reshape((2,2))
print("\nReshaped 1D to 2D (5x1):\n", reshaped)

flattened = arr2D.flatten()
print("\nFlattened 2D to 1D:\n", flattened)

# 4. Mathematical Operations

#sum
sum=np.add(arr1D,arr[:4])
print("\nSum of arr1D and arr:\n", sum)   
# multiply
multiply = np.multiply(arr1D,arr[:4])        
print("\nmultiply of arr1D  and arr:\n", multiply)
#subtract
subtract = np.subtract(arr1D, arr[:4])
print("\nSubtract arr from arr1D:\n", subtract) 
# divide    
divide = np.divide(arr1D, arr[:4])
print("\nDivide arr1D by arr:\n", divide)       
#power
power = np.power(arr1D, 2)  
print("\nPower of arr1D raised to 2:\n", power)

#modulus
modulus = np.mod(arr1D, 2)  
print("\nModulus of arr1D with 2:\n", modulus)

