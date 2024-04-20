from Core import *
from matplotlib import pyplot as plt


integrator_names = ['euler_forwards','euler_back','semi_implicit_euler',
                                     'midpoint','rk4']
integrators = [ Integrator() for name in integrator_names]
for i in range(len(integrators)):
    integrators[i].cycle(i)

force = Force()
force.switch("earth_gravity")

dt = 1
time = 1

particle_init = Particle(Vector(0,0,0), Vector(0,5, 0), 1)
state_init = SystemState([particle_init], 0, dt)


state_ref = SystemState( [Particle(Vector(0,0.095,0), Vector(0,0, 0), 1)] , 5, 0.001)

errors = []
for integrator in integrators:
    system = System(state_init, integrator, force, dt)
    system.step(int(time / dt) + 1)
    final_state = system.get_state(-1)
    print(final_state)
    error = final_state * state_ref
    errors.append(error)
    



plt.bar(integrator_names, errors)
plt.xlabel("Integration Method")
plt.ylabel("Average Error (metres)")
plt.title("Error From Refrence Simulation Value For Different Integrators")
plt.show()

