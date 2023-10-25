# print(' hello world')
# # names = ('vivian', 'bolu')
# # for name in names:
# #     print(name)
# # print('name')
    
# # vi = ('mississippi')

# my_list=[1,2,3,4,5,6]
# for i in len(my_list):
#     print(my_list)
    
    
    
# def new_day (day):
#     days = day
#     return days
# while True:
#     day = input("Enter a day: "
#                 )
    
#     print('Thank God its a new day!'
#           )
    
#     if day=='tuesday':
#         print("Forever i will be greatful"
#               )
#         break
    
def wishes(fist):
    print(fist.title(), 'Birthday')

wishes('happy')
# message = (wish, "Birthday")
# print(message)
    # outputs: Happy Birthday!

# def if_is_triangle(a,b,c):
#     return a+b > c and b+c > a and a+c > b
# a=float(input('Enter the number of the side\'s length:'))
# b=float(input('Enter the number of the side\'s length:'))
# c=float(input('Enter the number of the side\'s length:'))
# if_is_triangle(a,b,c)
# print('Yes it is a triangle')

# def factorial(n):
#     result = 1
    
#     for x in range(0,10):
#         result= result * x
#     return x
# for n in range(0,10):
#   print(n, n*factorial(n))
    
# def factorial(n):
#     return n
# n=int(input('Enter a nunmber: '))
# for i in range(n):
#     print(i)
# print(n, '=>',n*factorial(n))

def fib(n):
    if n < 1 :
        return None
    if n < 3:
        return 1
    elem_1 = elem_2 =1
    the_sum = 0
    for i in range(3, n+1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum
for n in range(1, 10):
    print(n, "=>", fib(n))

def factorial(b):
    if b == 1:
        return 1
    else:
        return b * factorial(b - 1)
print(factorial(4))


# def factorial(n):
#     return n * factorial(n - 1)

# print(factorial(4))
def fun(a):
    if a > 30:
        return 3
    else:
        return a + fun(a + 3)
print(fun(25)) 


my_tuple = (1,10,100,1000)

print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[1:])
print(my_tuple[:-2])

for elem in my_tuple:
    print(elem)
print(10 in my_tuple)  # in is accepted in tuple and it act as a  bool, same as not in 
var  = 23
t1 = (1,)
t2 = (2,)
t3 = (3,var)
t1,t2,t3 = t3,t2,t1
print(t1,t2,t3)

User = []
Humans = {'Name': 'jemmah',
          'Store': 'rellish', 
          'street': 'Booka'
          }
for items in Humans:
    User.append(items)
    print(User)
print(User)
print(Humans['Name'])
for User in Humans:
    print(User)
    if User in Humans:
     print(User,'=>', Humans[User])
    else:
        print(User, 'is not available')
        
for key in Humans.keys():
    print(key, '=>', Humans[key])
for pairs, pair in Humans.items():
    print(pairs, '=>', pair) 
for key in sorted(Humans.keys()):
    print(key, '=>', Humans[key])
for value in Humans.values(): # THE value() is used to get value pair in key
    print(value)
Humans['opay']='Bank'
print(Humans)
del Humans['opay']
print(Humans)
Humans.update({'opay':'Bank'})
print(Humans)
# popitem() is used to remove a random item  from a dictionary and also used to del last item on a dictionary
# studentNames = {}
# while True:
#     studentName = input('Enter your name: ')
#     if studentName=='':
#         break
#     studentScore = int(input('Enter your score (0 - 10): '))
#     if studentScore not in range(0,11):
#         break
   
#     if studentName in studentNames:
#         studentNames[studentName] += (studentScore,)
#     else:
#         studentNames[studentName]= (studentScore,)

    
        
        
stu_class = {}
while True:
    name = input("Enter your name: ")
    if name == "":
        break
    score = int (input("Enter your score (0 - 10): "))
    if score not in range (0,11):
        break
    if name in stu_class:
        stu_class[name]+= (score,)
    else:
        stu_class[name] = (score,)
for name in sorted(stu_class.keys()):
    adding =0
    counter =0
    for score in stu_class[name]:
        adding += score
        counter += 1
        print(name, ':', adding/counter)


        
        
        
        
        
        
blade = []       
segun = {'name':'taiwo', 'age': 18}  
for items in segun:
    blade.append[items]

      
    

    

    


        




    
    
    
    
    
