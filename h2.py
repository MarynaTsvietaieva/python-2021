# -*- coding: utf-8 -*-

# fifth power of numbers from 1 to 20 inclusive
my_list = [ x**5 for x in range(1, 21)]
print(my_list)

# replace integer numbers with their decimal part in the list of integers and integers
p = [1,2.45,4,6.3,1.48,80]
my_list = [p[i]%1 if p[i]%1 != 0 else p[i] for i in range(len(p))]
print(my_list)

# all possible combinations of elements of two lists if the numbers are not the same
sp1= [1,3,4]
sp2 = [3,4,5]
my_list = [[str(x),str(y)]  for x in sp1 for y in sp2 if x!=y]
print(my_list)

# lambda expression that converts Fahrenheit to Celsius
f = lambda x:(x-32)/1.8
print(f(50))




