from Core import *

integrator = Integrator()
integrator.switch('euler_forwards')

force = Force()
force.switch('n_body')

dt = 0.1
steps = 5000

P1 = Particle(Vector(1 , 0, 0), Vector(0 , 1, 0), 1e10)
P2 = Particle(Vector(-1 , 0, 0), Vector(0 , -1,0), 1e10)

state_init = SystemState([P1, P2], 0, dt)

system = System(state_init, integrator, force, dt)
system.step(steps)

from Render import *
display_system(system, scale = 50, time_scale = 0.1, color = 'red')
