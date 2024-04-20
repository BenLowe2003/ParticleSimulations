
from Ephemeris import start_planet_particles, end_planet_particles
from Core import *
from time import time


integrator = Integrator()
integrator.switch("semi_implicit_euler")
force = Force()
force.switch("n_body")

dt = 100000
start_time = 0
integrator_names = ['euler_forwards','euler_back','semi_implicit_euler',
                                     'midpoint','rk4']
integrators = [ Integrator() for name in integrator_names]
for i in range(len(integrators)):
    integrators[i].switch(integrator_names[i])
month = 30 * 24 * 60 * 60

init_state  = SystemState(start_planet_particles, start_time, dt)
final_state_real = SystemState(end_planet_particles, start_time, dt)

refrence_system = System(init_state, integrators[2], force, 1000)
refrence_system.step_time(month)
final_state_ref = refrence_system.get_state(-1)


errors_real = []
errors_ref = []
times = []

for integrator in integrators:
    
    test_system = System(init_state, integrator, force, dt)

    start_time = time()
    test_system.step_time(month)
    end_time = time()
    time_difference = end_time - start_time
    times.append(time_difference)
    
    end_state = test_system.get_state(-1)
    error_real = end_state * final_state_real
    error_refrence = end_state * final_state_ref
    errors_real.append(error_real)
    errors_ref.append(error_refrence)
