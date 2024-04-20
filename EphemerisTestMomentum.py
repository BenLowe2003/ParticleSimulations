from Core import *
from matplotlib import pyplot as plt
from Ephemeris import start_planet_particles



integrator_1 = Integrator()
integrator_1.switch('euler_semi_implicit')
integrator_2 = Integrator()
integrator_2.switch('midpoint')


force = Force()
force.switch('core')


steps = 50
month = 30 * 24 * 60 * 60
dt = month * 10

state_init = SystemState(start_planet_particles, 0, dt)


system_1 = System(state_init, integrator_1, force, dt)
system_2 = System(state_init, integrator_2, force, dt)

system_1.step(steps)
system_2.step(steps)

momentums_1 = system_1.get_momentum()
momentums_2 = system_2.get_momentum()
momentums_1 = [ momentum.norm() for momentum in momentums_1]
momentums_2 = [ momentum.norm() for momentum in momentums_2]

times = system_1.get_times()

plt.plot(times, momentums_1, label = str(integrator_1))
plt.plot(times, momentums_2, label = str(integrator_2))
plt.xlabel('Time (seconds)')
plt.ylabel('Total Momentum (kilogram metres per second)')
plt.title('Total Momentum Conservation For Different Integrators')
plt.legend()

plt.show()

from Render import *
display_system(system_1, scale = 50, time_scale = 1e-10, color = 'red')

