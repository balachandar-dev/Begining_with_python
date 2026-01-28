import numpy as np

# Very easy 

""" 1 Create & Inspect
Create a NumPy array from 1 to 20 and:
find shape
find dtype
reshape it into (4, 5) """

num_array = np.arange(1,21)

num_array.shape
num_array.dtype

if num_array.size == 20:
    reshaped_array = num_array.reshape(4,5)


"""
2. Replace Values
Given:
a = np.array([1, 2, 3, 4, 5])
Replace all odd numbers with -1."""

a = np.array([1, 2, 3, 4, 5])
# for index, value in np.ndenumerate(a):
#     if value % 2 == 1:
#         a[index] = -1
a[a % 2 == 1] = -1
print(a)


""""3 Find Common Elements
Given:
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])
Find common elements without loops."""

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])

c = np.intersect1d(a, b)
print(c)

value = np.full(10, 7)

#reverse
a = [1, 2, 3, 4, 5]
a.reverse()

#even
b = np.array([3, 6, 8, 1, 9, 2])
b = b[b%2 == 0] 

# find true 
bool_array = np.array([True, False, True, False])
n = np.sum(bool_array == True) 
print(n)