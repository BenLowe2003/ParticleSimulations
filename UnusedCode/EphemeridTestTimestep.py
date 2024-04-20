from EphemeridsSimple import start_planet_particles, end_planet_particles
from Core import *


integrator = Integrator()
integrator.switch("semi_implicit_euler")
force = Force()
force.switch("n_body")

dt = 100
start_time = 0
test_dt = [ 2 ** i * 100 for i in range(0,21)]
month_time = 30 * 24 * 60 * 60

init_state  = SystemState(start_planet_particles, start_time, dt)
final_state = SystemState(end_planet_particles, start_time, dt)


end_state_ref = final_state

errors = []

for dt in test_dt:
    test_system = System(init_state, integrator, force, dt)
    test_system.step_time(month_time)
    print("dt = " + str(dt) + " is finished")
    end_state = test_system.get_state(-1)
    error = end_state * end_state_ref
    errors.append(error)




from math import log10, exp
from matplotlib import pyplot as plt



x = []
xticks = [ i for i in range(2,5)]
xnames = [ round(10 ** t, 1) for t in xticks]
yticks = [i for i in range(20, 25)]
ynames = [ round(10 ** t)  for t in yticks]

y = []

for i in range(11):
    x.append(log10(test_dt[i]))
    if errors[i] !=0:
        y.append(log10(errors[i]))
    else:
        y.append(0.0)



plt.plot(x, y)
#plt.xticks(xticks, xnames)
#plt.yticks(yticks, ynames)
plt.xlabel("timestep (seconds)")
plt.ylabel("average squred error (metres)")
plt.title("Error from true Ephemerids value for different timesteps")
plt.show()


"""

from Render import *

display_system(system, window, scale = 5e-14, time_scale = 4e-6)

"""


