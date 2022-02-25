# open dipole.txt and read the file
f = open("dipole.txt", "r")
# read the file
text = f.read()
# close the file
f.close()
# read the file line by line
lines = text.split("\n")
# read each line
for line in lines:
    # split the line into words
    words = line.split()
    # if the line is not empty
    if len(words) > 0:
        # if the second word has a value greater than 1 then add the line to a list
        if float(words[1]) > 1:
            # add the line into a new file called greater_than_one.txt
            f = open("greater.txt", "a")
            f.write(line + "\n")
            f.close()
        # if the second word has a value less than 1 then add the line to a list
        elif float(words[1]) < 1:
            # add the line into a new file called less_than_one.txt
            f = open("lower.txt", "a")
            f.write(line + "\n")
            f.close()
        else :
            continue
        # if the second word has a value equal to 1 or 0 less than 0  then ignore it

