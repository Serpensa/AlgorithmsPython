 # В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random
SIZE = 10
arr = [random.randint(-100, 100) for _ in range(SIZE)]
min_num  = 0
pos_num = -1
print(arr)
for i in range(SIZE):
	if arr[i] < 0 and pos_num == -1:
		min_num = arr[i]
		pos_num = i
	elif 0 > arr[i] > min_num:
		min_num = arr[i]
		pos_num = i
print('максимальный отрицательный элемент= ', min_num, 'позиция его в массиве= ', pos_num)

