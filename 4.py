#4. Определить, какое число в массиве встречается чаще всего.


import random
SIZE = 100
arr = [random.randint(0, 100) for _ in range(SIZE)]
print(arr)
n = arr[0]
freq_max = 1
for i in range(SIZE):
	freq = 1
	for k in range(i+1, SIZE):
		if arr[i] == arr[k]:
			freq += 1
		if freq > freq_max:
			freq_max = freq
			n = arr[i]
if freq_max>1:
	print(f'Число {n} встречается {freq_max} раз')
else:
	print('Нет повторяющихся элементов')
