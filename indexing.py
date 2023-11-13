my_list = []
num = int(input("Enter number to be sort: "))
swapped = True
for i in range(num):
    val = int(input("Enter a list of element: "))
    my_list.append(val)
while swapped:
    swapped =False
    for i in range(len(my_list)-1):
        print(i)
        if my_list[i] > my_list[i+1]:
            swapped = True
            my_list[i],my_list[i+1] = my_list[i+1],my_list[i]
           
print(my_list
      ) # NOTE THAT ABSTRACTION TOOK PLACE IN THE FOLLOWING CODE..



# indecing and slicing
# from calendar import SUNDAY


my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
my_list = my_list[4:]
my_list.sort()
del my_list[1:2]

print(my_list)
# my_list.reverse()
my_list=my_list[::-1]  # In order word this also can be used to reverse a list 

    
   
print("The list with unique elements only:")
print(my_list)
    
            
i = 0
while i <= 3 :
    i +=2
    print("*")
    

def check_if_year_is_leap(year):
    if (year%4==0):
        return True
    else:
        return False

print(check_if_year_is_leap(4))
# print(check_if_year_is_leap(2023))

def days_of_the_week(day):
    
     if day == 'Sunday':
        print("Keep burning, keep praying and keep believing")
        print("He's the same today, yesterday and forever")
        print("Thank you for your sustainance and grace you've shown to me as an individual")
        print('Thank you its another', day,'!!')
        
     else:
        print('Its not sunday, go to work')
        print('oh lord, bless the new week!')
days_of_the_week('monday')


Names=[]
Names.append('Ayobami')
Names.append("Mary")
Names.append('Eriayo')
for Name in Names:
    request = input('Enter your name: ')
    if request==Name:
        break
    
   
    Tag = input('Uniqness: ')
    print(Name,'is',Tag)
    print(Name)
   


