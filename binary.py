# ================= Compulsory Task ==================
# Create a new Python file in this folder called “Binary.py”
# Write a program that can convert a binary number to a decimal number.
# A binary number is basically a number that is made up entirely of 0s and 1s (e.g 101101)
# You can represent any amount you would like using binary.
# Ask the user to enter a binary number and convert that number to a decimal number.
# You can visit the following site to find out how to convert from binary to decimal:
#   http://www.rapidtables.com/convert/number/how-binary-to-decimal.htm
# Print out the decimal value of the number.
# Remember to make use of the built-in functions found in the math module as well as lists.

import math
# Imports math module
print('Binary is basically a number that is made up entirely of 0s and 1s (e.g 101101)')
# Give a brief disription of how binary is written
binary = input("Enter number in Binary Format:\n")
arrange = [int(i) for  i in binary]
# int() math built in function
# Arrange the numbers of the binary numbered entered in a list
arrange  = arrange[::-1]
# Read the list from right to left
result = []
# Create an open list
for i in range(len(arrange)):
    result.append(arrange[i]*(2**i))
    # Here it calculates by taking each binary number and multiplying it by 2 to the power of the position#   
    #print(i)
    # Prints each position in result lits
sum_result = sum(result)
# sum() math built in function
# Adds the result of each number in result list
print('Binary:',binary,'\nDecimal Number is :',sum_result)
