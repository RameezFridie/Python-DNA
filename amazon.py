# ================= BONUS Optional Task ==================
# Create a Python file called "amazon.py" in this folder.
# Write code to read the content of the text file input.txt.
# For each line in input.txt, write a new line in the new text file output.txt that computes the answer to some operation on a list of numbers.
# If the input.txt has the following:
#       Min: 1,2,3,5,6
#       Max: 1,2,3,5,6
#       Avg: 1,2,3,5,6
# Your program should generate output.txt as follows:
#       The min of [1, 2, 3, 5, 6] is 1.
#       The max of [1, 2, 3, 5, 6] is 6.
#       The avg of [1, 2, 3, 5, 6] is 3.4.
# Assume that the only operations given in the input file are min, max and avg, and that the operation is always followed by a list of comma separated integers.
# You should define the functions min, max and avg that take in a list of integers and return the min, max or avg of the list.
# Your program should handle any combination of operations and any length of input numbers.
# You can assume that the list of input numbers are always valid integers and that the list is never empty.

the_file = open('input.txt','r')
the_lines = the_file.readlines()
the_file.close()

temp_line_1 = the_lines[0].split(':')              
temp_line_1 = temp_line_1[1].split(',')
x = (int(i) for i in temp_line_1)
x = min(x)
temp_1 = the_lines[0].replace('min:','').split()
# Did this so that in the file it just prints ['1,2,3,4,5,6']
temp_line_2 = the_lines[1].split(':')
temp_line_2 = temp_line_2[1].split(',')
y = (int(i) for i in temp_line_2)
y = max(y)
temp_2 = the_lines[1].replace('max:','').split()
# Did this so that in the file it just prints ['1,2,3,4,5,6']
count = 0
total = 0
temp_line_3 = the_lines[2].split(':')
temp_line_3 = temp_line_3[1].split(',')
for i in temp_line_3:                    #Checks each position for a number
        count += 1                       # For each i in the loop will add the counter by 1
        total += int(i)                  # Casts the string value at i into an integer then adds it
        average = total/count
temp_3 = the_lines[2].replace('avg:','').split()
# Did this so that in the file it just prints ['1,2,3,4,5,6']
out_file = open('output.txt','w')
out_file.write('The min of ' + str(temp_1) + ' is ' + str(x) + '\n')
out_file.write('The max of ' + str(temp_2) + ' is ' + str(y) + '\n')
out_file.write('The avg of ' + str(temp_3) + ' is ' + str(average))        
out_file.close()

