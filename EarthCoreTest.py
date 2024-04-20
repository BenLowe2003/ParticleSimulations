from Core import *
from matplotlib import pyplot as plt
#from Render import *

integrator_explicit = Integrator()
integrator_explicit.switch('euler_forwards')
integrator_syplectic = Integrator()
integrator_syplectic.switch('midpoint')

force = Force()
force.switch('earth_core')

dt = 50
total_steps = 2000

particle_init = Particle(Vector(100, 0, 0), Vector(0, 0, 0, ), 1)
state_init = SystemState([particle_init], 0, dt)
system_explicit = System(state_init, integrator_explicit, force, dt)
system_symplectic = System(state_init, integrator_syplectic, force, dt)

system_explicit.step(total_steps)
system_symplectic.step(total_steps)

x_position_explicit = [ state.get_particle(0).get_position().get_x()
                        for state in system_explicit.get_states()]
x_position_symplectic = [ state.get_particle(0).get_position().get_x()
                        for state in system_symplectic.get_states()]
times = [dt * i for i in range(total_steps+1)]

plt.plot(times, x_position_explicit, label = 'Explicit')
plt.plot(times, x_position_symplectic, label = 'Symplectic')
plt.legend()
plt.xlabel('Time (seconds)')
plt.ylabel('Displacement (metres)')
plt.title('Simulation Of A Particle Falling Towards Earths Core')
plt.show()

energies_explicit = system_explicit.get_energies()
energies_symplectic = system_symplectic.get_energies()

plt.plot(times, energies_explicit, label = 'Explicit')
plt.plot(times, energies_symplectic, label = 'Symplectic')
plt.legend()
plt.xlabel('Time (seconds)')
plt.ylabel('Energy (kilogram metres squared per second squared)')
plt.title('Simulation Of A Particle Falling Towards Earths Core')
plt.show()

#display_system(system_explicit, scale = 1)

            
