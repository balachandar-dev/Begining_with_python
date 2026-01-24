from matplotlib.pylab import int32
import numpy as np

numpy_array = np.array([[0, 1, 2, 3, 4, 5, 6, 7]])

two_dimension_array = np.array([[1,2,3],[4,5,6]])
two_dimension_array

two_dimension_array.dtype

two_dimension_array.shape

two_dimension_array.size

two_dimension_array.ndim 

zeros = np.zeros((2,3), dtype=int)

ones = np.ones((2,3), dtype=int)

arr_range = np.arange(10)

arr_range_float = np.linspace(1,10,5)

arrray_3_d_ones =np.ones((4,2,2), dtype='int32')

arrray_3_d_value =np.full((4,2,2),99) 
array_full = np.full_like(arrray_3_d_value.shape, 4)

array_random = np.random.rand(4,2,3)

array_random_int = np.random.randint(4, 8, size = (3,3))
# range is 4 to 8, matrix 3 * 3
# u can use negative too
 
array_id = np.identity(5)
#square matrix

repear_array = np.repeat(numpy_array, 3, axis = 0)
# to repeat, it should be enclosed in [[values]] 

a = np.ones((5,5), dtype = int32)

b = np.zeros((3,3), dtype = int32)

a [1:-1, 1:-1] = b

a[2,2] = 9