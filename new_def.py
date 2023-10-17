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

  
    

# a = [55,64,75,80,65]
# Average = Average_marks(a)

# print('The average is', Average)


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
