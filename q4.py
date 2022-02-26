import numpy as np
import matplotlib.pyplot as plt

# Define some initial parameters
# rate of change of the time step
dt = 50 
# define total time
total_time = 10**6
# set sigma
sigma = 6.69
# set epsilon
epsilon = 8.71*10**-4
# set the initial position of particle
x = 7
# set the initial velocity of particle
v = 0
# calculate the no of steps
steps = int(total_time / dt)
# mass of the particle
mass = 145123
# initialize a list to store the position of particle
position = []
# initialize a list to store the time step
time = []

plt.style.use('_mpl-gallery')

def plot(time, position):
    # find min and max of k_list
    min_y = min(position)
    max_y = max(position)
    # find min and max of T
    min_x = min(time)
    max_x = max(time)
    fig, ax = plt.subplots()
    ax.plot(time, position, linewidth=2.0)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Position (a.u.)')
    ax.set_title('time vs. position')
    ax.set(xlim=(min_x, max_x), ylim=(min_y, max_y))
    ax.grid(True)
    plt.show()


# Define the function of ljp potential
# referenced from https://pythoninchemistry.org/sim_and_scat/molecular_dynamics/intro.html
# referenced from Martínez, L.; Andrade, R.; Birgin, E. G.; Martínez, J. M. J. Comput. Chem. 2009, 30 (13), 2157–2164. 10.1002/jcc.21224.
def lj_force(r, epsilon, sigma):
    # Calculate the force of lj
    return 48 * epsilon * np.power(
        sigma, 12) / np.power(
        r, 13) - 24 * epsilon * np.power(
        sigma, 6) / np.power(r, 7)

for i in range(0, steps):
    # Calculate the force of lj
    force = lj_force(x, epsilon, sigma)
    # Calculate the acceleration
    acceleration = force / mass
    # Calculate the velocity
    v = v + acceleration * dt
    # Calculate the position
    x = x + v * dt
    # add the position to the list
    position.append(x)
    # add the time step to the list
    time.append(i * dt)

# plot the position of particle vs time
plot(time, position)

