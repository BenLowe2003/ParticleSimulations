
import graphics as gr
from time import sleep

from Core import *


window = gr.GraphWin("Simulation", 1000, 1000)

def display_state(state, window = window, scale = 10, color = 'white'):
    for particle in state.get_particles():
        position = particle.get_position()
        position.set_y(-position.get_y())
        position *= scale
        centre_screen = Vector(window.getWidth(), window.getHeight(), 0) / 2
        position += centre_screen
        x,y,z = position.transpose()
        point = gr.Point(int(x), int(y))
        circle = gr.Circle(point,5)
        circle.setFill(color)
        circle.draw(window)

def display_system(system, window = window, scale = 50, time_scale = 1, color = 'white'):

    states = system.get_states()
    num_states = len(states)
    
    for i in range( num_states ):
        state = states[i]
        display_state(state, window, scale = scale, color = color)
        sleep(system.get_dt() * time_scale)



