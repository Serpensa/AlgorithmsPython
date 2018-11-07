6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.


import random
SIZE = 10
arr = [random.randint(0, 100) for _ in range(SIZE)]
print(arr)
max_num = 0
min_num = 100
max_i = 0
min_i = 0
s = 0
for i in range(SIZE):
	if arr[i] > max_num:
		max_num = arr[i]
		max_i = i
	elif arr[i] < min_num:
		min_num = arr[i]
		min_i = i
print ('Наименьший элемент массива = ', min_num, 'в ячейке', min_i)
print ('Наибольший элемент массива = ', max_num, 'в ячейке',  max_i)
if max_i > min_i:
	for i in range(min_i+1, max_i):
		s += arr[i]
else:
	for i in range(max_i+1, min_i):
		s += arr[i]
print('Сумма элементов между минимальным и максимальным элементами = ', s)




