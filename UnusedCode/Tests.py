import graphics as gr
import time

from core import *


print("here")

def display_state(state, window):
    for particle in state.get_particles():
        position = particle.get_position()*50 + Vector(window.getWidth(), window.getHeight(), 0) / 2
        x,y,z = position.transpose()
        point = gr.Point(int(x), int(y))
        circle = gr.Circle(point,5)
        circle.draw(window)

def display_system(system, window):
    for i in range(system.num_states()):
        state = system.get_state(i)
        display_state(state, window)
        time.sleep(system.get_dt())

integrator1 = Integrator()
integrator1.cycle(0)
integrator2 = Integrator()
integrator2.cycle(2)


force = Force()
force.cycle(2)
dt = 0.01

pos1 = Vector(1,0,0)
vel1 = Vector(0,0.4,0)
m1 = 1
p1 = Particle(pos1, vel1, m1)

pos2 = Vector(-1,0,0)
vel2 = Vector(0,-0.4,0)
m2 = 1
p2 = Particle(pos2, vel2, m2)

print("here")

init_state = SystemState([p1, p2], 0, dt)

system_ref = System(init_state, integrator1, force, dt/100)
system1 = System(init_state, integrator1, force, dt)
system2 = System(init_state, integrator2, force, dt)

system_ref.step_time(1000)
system2.step_time(10)

window = gr.GraphWin("Simulation", 1600, 1020)

display_system(system1, window)


