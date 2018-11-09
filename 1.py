#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

diap= [ i for i in range (2, 100)]
denom = [0]*8
for i in range(2,100):
	for k in range(2,10):
		if i % k == 0:
			denom[k-2] += 1
i = 0
while i < len(denom):
	print(f'числу {i+2} кратны  {denom[i]} чисел')
	i += 1