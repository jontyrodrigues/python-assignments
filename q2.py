import numpy as np
# solve a cubic equation ax^3 + bx^2 + cx + d = 0 using the method of cubics roots
def find_v(a,b,P,R,T):
    coefficient = np.array([1,-(b+(R*T/P)),(a/P),-a*b/P])
    roots = np.roots(coefficient)
    for i in roots:
        if i.imag == 0:
            return i.real
# open the file real_gas.txt
f = open("real_gas.txt", "r")
# read the file
text = f.read()
# close the file
f.close()
# read the file line by line
lines = text.split("\n")
# read each line
for line in lines:
    # skip the first line
    if line == lines[0]:
        continue
    # split the line into words
    words = line.split()
    # if the line is not empty
    if len(words) > 0:
        # add the first word of the line to a variable called temperature
        temperature = words[0]
        # add the second word of the line to a variable called pressure
        pressure = words[1]
        print(find_v(3.592,4.267*10**-2,float(pressure),0.082,float(temperature)))

