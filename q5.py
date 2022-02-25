# n*lambda = 2*d*sin(theta) d = a/sqrt(h**2+k**2+l**2) take a from user
import math
def main():
    a = float(input("Enter the length of the side of the cube: "))
    # find the value of d from a using the formula d = a/sqrt(h**2+k**2+l**2)
    # as h = 1, k = 1, l = 0 the formula is d = a/sqrt(2)
    d = a/2**0.5
    # find the value of lambda from d using the formula lambda = 2*d*sin(theta) 
    # where n = 1, theta = pi/180*21 as theta = 21 degrees
    lam = 2*d*math.sin(21*math.pi/180)/1
    print("The wavelength is", lam)

if __name__ == "__main__":
    main()