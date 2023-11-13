# def dictionary(name, deparment):
#     print('solution')

    
name = {'seun:', 'segun:', 'bola:'}
department = {'art', 'sciene', 'managmement'}
for i in name:
    for k in department:
        print(i, k)
        solution = {i,k}
        

        

# answer = {key:value for key,value in solution.items() if i != k}
# entry = answer
# print(entry)


    
        
       
    


# dictionary 
from math import floor, ceil, trunc
x = 1.4
y = 2.6
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(trunc(x), trunc(y))
from random import random,seed, randrange, randint,choice, sample
seed(0)
for m in range(3):
    print(random())
for i in range(10):
    print(randint(1,10), end=',')
    
    
my_list =[1,2,3,4,5,6,7,8,9,10]
print(choice(my_list))
print(sample(my_list,5))
print()
from platform import platform, machine, processor, system, version,python_implementation, python_version_tuple
platform(aliased=False, terse=False)
print(platform())
print(platform(0,1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
for atr in python_version_tuple():
    print(atr)

     
