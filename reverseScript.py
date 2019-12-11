# Ask user for input file
filename = input("Enter text filename: ")

# Reverse lines from file
for line in reversed(list(open(filename))) :
    print(line.rstrip())