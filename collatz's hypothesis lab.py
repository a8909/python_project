# for loop
for i in range(1,11):
    # for odd
    if i % 2 == 1:
        print(i)

# while loop
x =1
while x<11:
    if x % 2 ==1:
        print(x)
        x += 1
    
# Break statement
for letter in "john.smith@pythoninstitute.org":
    if letter == "@":
        
        break
    print(letter)


#listing 
number = [5,4,3,2,1]
number.sort()
print(number)


hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.
replace_number = int(input("Enter an integer number to replace the middle number:  ")) 
hat_list[2] = replace_number
hat_list.remove(4)
print(len(hat_list))
# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

# Step 2: write a line of code that removes the last element from the list.

# Step 3: write a line of code that prints the length of the existing list.

print(hat_list)