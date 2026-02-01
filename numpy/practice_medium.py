import numpy as np

a = np.array([10, 5, 20, 8, 20])
unique_array = np.unique(a)
value = unique_array[-2]

b = np.array([4, 10, 7, 3, 20, 15])
sorted_values = np.sort(b)
value = sorted_values[-3:]

c = np.array([[2, 4],[6, 8]])
rows_sums = np.sum(c, axis = 1)
rows_sums = rows_sums.reshape(-1,1)
normalized = c / rows_sums

d = np.array([10, 20, 30, 40])
mean_value = np.mean(d)
d = np.where(d> mean_value, 1, 0) 
print(d)

e = np.array([1, 2, 2, 3, 3, 3, 4])
values, counts  = np.unique(e, return_counts = True)
print(values)
print(counts)

f = np.array([[1, -2, 3],[4,  5, 6], [-1, 7, 8]])
row_with_negative = np.any(f < 0, axis = 1)
print(np.where(row_with_negative)[0])

NaN = np.nan
g = np.array([[1, NaN, 3], [4, 5,  NaN],[7, 8, 9]])
mean_value = np.nanmean(g, axis = 1)
indexes = np.where(np.isnan(g))
g[indexes] = np.take(mean_value,indexes[0])
g

# g[g == Nan] =

h = np.array([[10, 30, 20],[5,  1,  9]])
index = np.argmax(h, axis = 1)

i = np.array(object=[1, 2, 3, 2, 4, 3, 5])
values, counts = np.unique(ar=i, return_counts = True)
print(values[counts > 1])



