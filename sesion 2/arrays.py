import numpy as np



arr1d = np.array([1,2,3,4,5])
arr2d = np.array([[1,2,3],[4,5,6]])
#print(arr1d)
#print(arr2d)

arr = np.array([1,2,3,4,5])
#print(arr[2])
#print(arr[1:4])



x = [1,2,3]
y = [2,6,5]
#print(x + y)
sum1 = np.array([1,2,3])
sum2 = np.array([4,5,6])
#print(sum1+sum2)
#print(sum1*sum2)



resArr = np.array([1,2,4,5,6,7])
#print(resArr.reshape(2,3))

arrSize = 20
maxValue = 5

v = np.random.randint(maxValue, size= np.random.randint(arrSize, size=1))
print(v) 
mean = np.mean(v)
max_val = np.max(v)
min_val = np.min(v)
sum_val = np.sum(v)
sort = np.sort(v)
r_sort = np.random.permutation(v)
square = v * v
sqrt_v = np.sqrt(v)

print(mean,max_val,min_val,sum_val,sum_val,sort,r_sort,square,sqrt_v, sep = " _____  ")

