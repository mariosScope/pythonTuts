import sys
import numpy as np

print('exec loop')
for i in [0,2,3]:
	if i%2 == 0:
		print("even")
	elif i == 0:
		print("zero")
	else:
		print("odd")
print('done')

print('arrays')
arr1 = np.array([[1,2,7], [3,4,8]])
arr2 = np.array([[1,2], [3,9], [4,16]])
print(np.dot(arr1, arr2))
print(' dd0d0d000d ')
print('done')
