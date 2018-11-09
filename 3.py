#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.


import random
SIZE = 10
arr = [random.randint(-100, 100) for _ in range (SIZE)]
print(arr)
min_n = 0
max_n = 0
for i in range (len(arr)):
	if arr[i] > max_n:
		max_n = i
	if arr[i] < min_n:
		min_n = i
print('максимальное число = ', arr[max_n], 'минимальное число = ', arr[min_n])
art = arr[max_n]
arr[max_n] = arr[min_n]
arr[min_n] = art
print(arr)