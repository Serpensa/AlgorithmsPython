#3. По введенным пользователем координатам двух точек вывести уравнение прямой, проходящей через эти точки.


x1=int(input('Enter x1='))
y1=int(input('Enter y1='))
x2=int(input('Enter x2='))
y2=int(input('Enter y2='))
k=(y1 - y2)/(x1 - x2)
b=y2-k*x2
print("y=",k, 'x+',b)