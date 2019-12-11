import re

filename = input("Enter text filename: ")

file = open(filename, 'r')
line = file.readline()

count = 1

while line :

    if line[0].isdigit() :
        print(re.sub(r"^\d+ ", "", line), end="")
    else :
        if count < 10 :
            print("0{count} {line}".format(**locals()), end="")
        else :
            print(count, line, end='')
        count += 1

    line = file.readline()
        
file.close()
