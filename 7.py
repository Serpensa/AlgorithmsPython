7. Написать программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n – любое натуральное число.

n = int(input('Enter number= '))
s = 0
for i in range (1, n+1):
    s = s+i
form = (n*(n+1))/2
if form == s:
    print('Correct')
else:
	print('Uncorrect')
print(int(form))
print(s)