# Starter code

#Maru Puran
#September 28, 2023
#Modify code to analyze errors and understand how to debug them, as well as get us more familiar with working with integers, variables, arithmetic expressions, inputs and outputs.

num1 = 10
name = input("Please enter your name: ") #ask user for name store in variable name
print("Please enter a number: ") #added prompt to tell user to enter a number
num2 = int(input()) #error fixed - add int() around the input to convert default string into an integer
answer = input("Thanks, " + name + "! Do you like programming?: ")


total1 = num1 + num2
total2 = num1*num2 #add a new variable, assign the product of num1 and num2 into it 

print("\nHello, " + name + "! When asked if you liked programming, you responded with " + answer + "!") #uses name and answer variable in the same output statement, outputs the strings for the user to see

print("\n" + str(num1) + " plus " + str(num2) + " = " + str(total1) + ". " + str(num1) + " multiplied by " + str(num2) + " = " + str(total2) + ".")  #oncatenated total1 to be outputted as well as convert into string to concatenate and provides user with the product (total2) the same way




# Instructions

# Line 4 creates an error. Look carefully to see what is wrong with the code and fix it. #fixed

# Add a text prompt between lines 3 and 4 to tell the user to enter a number. #fixed, added int()

# Complete line 8 to concatenate total 1 into the output statement. #done

# Add a new variable with a sensible identifier.  Multiply num1 and num2 together and assign the result into this variable. #done

# Output num1, num2 and your new variable in a similar format to line 8. #done