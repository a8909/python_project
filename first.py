import time

# Write a for loop that counts to five.
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    # Body of the loop - use: time.sleep(1)

# Write a print function with the final message.



h=[1,2,3,4,5]

print(h[0])

for i in range(5):
    print(str(h[i])+" Miississipi")
print('finally')


age = 18
if age >= 30:
    print("He has a valid age")
else:
        print("He is hacked !")
        
# phyton if case assessment

is_adult = False
if is_adult:
    print("He ia an adult")
else:
    print("He is a youth")
    
name = "ade"
name_2 = input("Enter a name: ")
if name == name_2:
    print("ade account is valid")
else:
    if name_2 == "frank":
         print("ade account is hacked and session is hijacked.")
         
# Guess the secret number game
magician_number = 77
secret_number = int(input("Enter number: "))
while magician_number != secret_number:
    #  print("Well done, muggle! You're free now")
    print('oops try again')
    secret_number = int(input("Enter number: "))
else:
     print("correct you are free") 
     
   # Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ")
for letter in user_word:
    if letter == "o":
        
            
         continue
        
        
    print(letter.upper())
#blocks and building game 
blocks = int(input("Enter the number of blocks: "))
height = blocks/2
#
# Write your code here.
if blocks != height:
    print("The height of the pyramid:", height)

