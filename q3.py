import math
import numpy as np
import matplotlib.pyplot as plt
# k = A*e**(-Ea/R*T)
def find_k(A, Ea, R, T):
    k = A*math.exp(-Ea/(R*T))
    return k
# find the k value for each of the following value of T
# T = 300, 400, 500, 600, 700, 800, 900, 1000
plt.style.use('_mpl-gallery')

def plot(T, k_list):
    # find min and max of k_list
    min_k = min(k_list)
    max_k = max(k_list)
    # find min and max of T
    min_T = min(T)
    max_T = max(T)
    fig, ax = plt.subplots()
    ax.plot(T, k_list, linewidth=2.0)
    ax.set_xlabel('Temperature (K)')
    ax.set_ylabel('k (cm^3/mol)')
    ax.set_title('k vs. Temperature')
    ax.set(xlim=(min_T, max_T), ylim=(min_k, max_k))
    ax.grid(True)
    plt.show()

k_list = []
T_list = []
T_inv_list = []

for T in [300, 400, 500, 600, 700, 800, 900, 1000]:
    print(find_k(10, 10000, 8.314, T))
    # add the k value to the list
    k_list.append(find_k(10, 10000, 8.314, T))
    # add the value of k to the list
    T_list.append(T)
    # add the value of 1/T to a list called T_inv_list
    T_inv_list.append(1/T)

plot(T_list, k_list)
plot(T_inv_list, k_list)



    
