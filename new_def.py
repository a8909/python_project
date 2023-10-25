# def  Average_marks(marks):
#     aver1 = len(marks)
#     aver2 = sum(marks)
#     Total = aver2/aver1
#     return Total    



# grade_a= str(input("Enter didgit:"))
# grade_b= str(input("Enter didgit:"))
# grade_c= str(input("Enter didgit:"))
# if Average>=80:
#         print("You have GRADE A")
# else:
#         print("You have GRADE C")
def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
        print(i)
    
    return strange_list

# print(strange_list_fun(5))
strange_list_fun(5)
print(strange_list_fun)
    



def is_year_leap(year):
    if year%4==0:  #mean it leap year
        return True
    elif year%100==0: #meas that it is not a leap year
            return False
    elif year%400==0:
                return True
    else:
        return False
          
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr,"->",end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

  
try: 
    a = [55,64,75,80,65]
    average = []
    for elem in a:
        
        average.append[elem]
        print(average)
        
except:print('The average is')
def f(x):
    if x ==0 :
        return 0
    return x + f(x-1)
print(f(3))
def fun(x):
    global y
    y = x * x
    return y
 
 
fun(2)
print(y)
def any():
    print(var + 1, end='')
 
 
var = 1
any()
print(var)
dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
v = dictionary['one']
 
for k in range(len(dictionary)):
    v = dictionary[v]
 
print(v)
tup = (1, 2, 4, 8)
tup = tup[1:-1]
tup = tup[0]
print(tup)
lst = [[x for x in range(3)] for y in range(3)]
 
for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print("#")
try:
    value = input("Enter a value: ")
    print(int(value)/len(value))
except ValueError:
    print("Bad input...")
except ZeroDivisionError:
    print("Very bad input...")
except TypeError:
    print("Very very bad input...")
except:
    print("Booo!")
foo = (1, 2, 3)
foo.index(0)
    






# def common_data(list1, list2):
    
#     for x in list1:
#         for y in list2:
#             if x == y:
#                 result = True
#                 return result
# common_data(3,4)
# print(common_data([1,2,3,4,5], [1,2,3,4,5]))
# print(common_data([1,2,3,4,5], [1,7,8,9,510]))
# print(common_data([1,2,3,4,5], [6,7,8,9,10]))
