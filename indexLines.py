import re

# Ask user for input file
filename = input("Enter text filename: ")

# Open requested file
file = open(filename, 'r')
line = file.readline()

count = 1

while line :

    # Check if line begins with a digiti
    if line[0].isdigit() :
        print(re.sub(r"^\d+ ", "", line), end="")
    else :
        if count < 10 :
            print("0{count} {line}".format(**locals()), end="")
        else :
            print(count, line, end='')
        count += 1

    # Increment file line
    line = file.readline()
        
# Close file
file.close()
