#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

n1=int(input('Enter number 1='))
n2=int(input('Enter number 2='))
n3=int(input('Enter number 3='))
if n2<n1<n3 or n3<n1<n2 :
	print(n1)
elif n1<n2<n3 or n3<n2<n1:
	print(n2)
else:
	print(n3)