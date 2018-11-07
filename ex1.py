#1. Проанализировать скорость и сложность одного - трёх любых алгоритмов, разработанных в рамках домашнего задания первых трех уроков.


 
def evenodd(k):

	import random
	n = random.randint(10**(k-1), 10**k )
	even = 0
	odd = 0
	while n > 0:
		x = n%2
		if x == 0:
			even +=1
		else:
			odd +=1
		n = n//10


#100 loops, best of 3: 24.7 usec per loop 
#100 loops, best of 3: 24.8 usec per loop
#100 loops, best of 3: 35.2 usec per loop

#cProfile.run('evenodd(100)')
#10 function calls in 0.344 seconds
#Ordered by: standard name
#ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#1    0.343    0.343    0.344    0.344 <ipython-input-10-3ba7d5da5a8b>:2(evenodd)
#1    0.000    0.000    0.344    0.344 <string>:1(<module>
#1    0.000    0.000    0.000    0.000 random.py:174(randrange)
#1    0.000    0.000    0.000    0.000 random.py:218(randint)
#1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
#1    0.000    0.000    0.344    0.344 {built-in method builtins.exec}
#1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects




def evenodd(k):
	import random
	num = str(random.randint(10**(k-1), 10**k ))
	even = odd = 0
	for i in num:
		if i in {'0', '2', '4', '6', '8'}:
			even += 1
		else:
			odd += 1

#100 loops, best of 3: 38.9 usec per loop
#100 loops, best of 3: 51.6 usec per loop
#100 loops, best of 3: 25.1 usec per loop



#9 function calls in 0.016 seconds
#Ordered by: standard name

   #ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        #1    0.016    0.016    0.016    0.016 <ipython-input-7-a34f71606983>:2(evenodd)
        #1    0.000    0.000    0.016    0.016 <string>:1(<module>)
        #1    0.000    0.000    0.000    0.000 random.py:174(randrange)
        #1    0.000    0.000    0.000    0.000 random.py:218(randint)
        #1    0.000    0.000    0.000    0.000 random.py:224(_randbelow)
        #1    0.000    0.000    0.016    0.016 {built-in method builtins.exec}
        #1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
        #1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        #1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}