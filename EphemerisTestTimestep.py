from Ephemeris import start_planet_particles, end_planet_particles
from Core import *


integrator = Integrator()
integrator.switch("semi_implicit_euler")
force = Force()
force.switch("n_body")

dt = 100
start_time = 0
test_dt = [ i * 2500 for i in range(1,50)]
month_time = 30 * 24 * 60 * 60

init_state  = SystemState(start_planet_particles, start_time, dt)
final_state = SystemState(end_planet_particles, start_time, dt)


end_state_ref = final_state

errors = []

for dt in test_dt:
    test_system = System(init_state, integrator, force, dt)
    test_system.step_time(month_time)
    #print("dt = " + str(dt) + " is finished")
    end_state = test_system.get_state(-1)
    error = end_state * end_state_ref
    errors.append(error)


from math import log10, exp
from matplotlib import pyplot as plt

x = test_dt
y = errors

plt.plot(x, y)

plt.ylim(0, errors[-1] + 1e15)
plt.xlabel("Timestep (seconds)")
plt.ylabel("Average Error (metres)")
plt.title("Error From True Ephemerids Values For Different Timesteps")
plt.show()
