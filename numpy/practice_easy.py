import numpy as np

# Very easy - DAy 1

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

"""
[10, 25, 5, 30, 15]
Replace all values greater than 20 with 0."""

a = np.array([10, 25, 5, 30, 15])
a[a > 20] = 0
print(a)

""""[5, 3, -1, 7]
Check if any element is negative."""

a = np.array([5, 3, -1, 7])
a = np.any(a < 0)
print(a)

identity_array = np.identity(3)

add_the_array = np.array([[1, 2], [3, 4]])
sum = np.sum(add_the_array)
print(sum)

given_array = np.array([4, 7, 1, 9, 3])
print(np.argmax(given_array))

to_convert_array = np.array([1.2, 2.5, 3.8])
print(to_convert_array.astype('int32'))


# Day 2

a = np.arange(5,16)
print(a)

b = np.array([10, 20, 30, 40, 50])
print(b[0], b[-1])

c = np.array([0, 1, 0, 2, 3, 0])
c[c == 0] = -1
print(c)

d = np.array([1, 4, 6, 7, 9, 10])
even_number = np.where(d % 2 == 0)
print(d[even_number].size)

e = np.array([[3, 5, 7, -2]])
print(np.all(e > 0))

f = np.array([2, 3, 4, 5])
print(f ** 2)

g = np.array([8, 3, 10, 1, 6])
print(np.min(g))

h = np.array([True, False, True, False])
print(h.astype('int32'))

i = np.array([[10, 20, 30, 40]])
mean_value = np.mean(i)
print(i[i > mean_value])

j = [[1, 2], [3, 4]]
print(np.ravel(j))