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
pos = 7
# set the initial velocity of particle
velocity = 0
# calculate the no of steps
steps = int(total_time / dt)
# mass of the particle
mass = 145123

# use lennard-jones potential formula to calculate the force of lj provided the distance between two particles, the epsilon and sigma
def lj_force(r, epsilon, sigma):
    # Calculate the force of lj
    return 48 * epsilon * np.power(
        sigma, 12) / np.power(
        r, 13) - 24 * epsilon * np.power(
        sigma, 6) / np.power(r, 7)


# use the force of lj to calculate the acceleration of the particle
def lj_acceleration(r, epsilon, sigma):
    # Calculate the force of lj
    force = lj_force(r, epsilon, sigma)
    # Calculate the acceleration
    acceleration = force / mass
    return acceleration

# use the acceleration to calculate the velocity of the particle
def lj_velocity(v, acceleration, dt):
    # Calculate the velocity
    velocity = v + acceleration * dt
    return velocity

# use the velocity to calculate the position of the particle
def lj_position(x, v, dt):
    # Calculate the position
    position = x + v * dt
    return position

# initialize a list to store the position of particle
position = []
# initialize a list to store the time step
time = []

# plot the position of the particle
plt.style.use('_mpl-gallery')

def plot(time, position):
    fig, ax = plt.subplots()
    ax.plot(time, position, linewidth=2.0)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Position (a.u.)')
    ax.set_title('time vs. position')
    ax.set(xlim=(0, total_time), ylim=(min(position), max(position)))
    ax.grid(True)
    plt.show()

# plot the position of the particle
for i in range(0, steps):
    # Calculate the force of lj
    force = lj_force(pos, epsilon, sigma)
    # Calculate the acceleration
    acceleration = force / mass
    # Calculate the velocity
    velocity = lj_velocity(velocity, acceleration, dt)
    # Calculate the position
    pos = lj_position(pos, velocity, dt)
    # append the position of the particle to the list
    position.append(pos)
    # append the time step to the list
    time.append(i*dt)

plot(time, position)






