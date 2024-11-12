print('Subtraction')
print('')

# In the variable userinput get the char (charater) that the user inputs
userinput=input('Enter your first number> ')
# Now convert it from a char to an int (integer) so we can do math on it later
number1 = int(userinput)

userinput=input('Enter your second number> ')
number2 = int(userinput)

userinput=input('Enter your third number> ')
number3=int(userinput)

print('Total: ', number1 - number2 - number3)
