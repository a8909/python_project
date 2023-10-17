def build_name(first_name, last_name, age=' '):
    full_name = first_name + ' ' + last_name + " " + "is" + " " + age
  
   

first_name=str(input('Enter first name:'))
last_name=str(input('Enter last name:'))
age=str(input('Enter age:'))


description = build_name(first_name, last_name, age)

# print(description
#       ) # The definition of build_name() takes a parameter first and last_name, then combine these two names, add a space between them and stores the result in full_name, then returned to the calling line.
#         # when returned is called you need to store it value in variablein order to be printed to the console. 

        
    
# def favorite_food(book_title):
#     message = ("One of his favorite books is" + " " + book_title.title() + "!")
#     print(message)
# favorite_food("alice in wonderland")




# def describe_city(city, country): # POSITIONAL ARGUEMENT 
#     message= ("He lives in " + city.title() + " " + "in" + " " + country.title())
#     print(message)
# describe_city("reykjavik", "iceland")
# describe_city("agege", "lagos")

# def get_description(first_name, last_name, status):
#     full_name=first_name + last_name + status
#     # return full_name.title()

# while True:
#     print("Please decribe yourself in a minute: ")
#     print("Enter 'q' at anytime to quit")
#     first_name= input("Enter your first name: ")
#     if first_name=='q':
#         break
#     last_name=input("Enter your last name: ")
#     if last_name=='q':
#         break
#     status=input("Enter status: "
#                  )
#     if status=='q':
#         break

# def greet_user(names):
#     print("hello" + " " + names.title())
# greet_user("tobiloba")
