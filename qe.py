import numpy as np

def real_gas(T,P):
    a = 3.592
    b = 4.267*10**-2
    R = 0.082
    coefficient = np.array([1,-(b+(R*T/P)),(a/P),-a*b/P])
    roots = np.roots(coefficient)
    return roots

y = real_gas(100,250)
for i in y:
    if i.imag == 0:
        print(i.real)

