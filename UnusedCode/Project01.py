from numpy import sqrt

## Here maybe define a sqrt(n, eps = 1e-16) function for completeness


class Vector:
    """
    Class for handling vectors.
    Attributes:
        x (float): The x component of the vector.
        y (float): The y component of the vector.
        z (float): The z component of the vector.
    """

    def __init__(self, x, y, z):
        """
        Returns a Vector object.
        Args:
            x (float): x component of the Vector.
            y (float): y component of the Vector.
            z (float): z component of the Vector.
        Return:
            Vector object with x,y,z components.
        """
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        """casts the Vector to a string"""
        return str(self.x) + ", " + str(self.y) + ", " + str(self.z)

    def __add__(self, other):
        """Operator adds two Vectors together."""
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x,y,z)
    
    def __sub__(self, other):
        """Operator subtracts two Vectors"""
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector(x,y,z)

    def __mul__(self, other):
        """Operator left multiplies a Vector by a float"""
        x = self.x * other
        y = self.y * other
        z = self.z * other
        return Vector(x,y,z)
    
    def __rmul__(self, other):
        """Operator right multiplies a Vector by a float."""
        return self.__mul__(other)
    
    def __truediv__(self, other):
        """Divides a Vector by a float. (Vector)"""
        if other != 0:
            return self.__mul__( 1 / other )
        else:
            raise ZeroDivisionError("Division of a Vector by Zero")
        
    def square_norm(self):
        """Returns the square of the norm of this Vector. (float)"""
        return self.x*self.x + self.y*self.y + self.z*self.z

    def norm(self):
        """Returns the norm of this Vector (float)"""
        return sqrt( self.square_norm())

    def transpose(self):
        return self.x, self.y, self.z


class Particle:
    """
    Object to hold all the infomation concerning a single particle in the system
    Attributes:
        position (Vector): The position of the particle.
        velocity (Vector): The velocity of the particle.
        mass (float): The mass of the particle.
    """

    def __init__(self, position, velocity,  mass):
        """
        Initialises a Particle object.
        Args:
            position (Vector): A Vector containing the x,y,z components of the particles initial position.
            velocity (Vector): A Vector containing the x,y,z components of the particles initial velocity.
            mass (float): A float to store the particles mass.
        Returns:
            Particle object.
        """
        self.velocity = velocity
        self.position = position
        self.mass = mass

    def __str__(self):
        """Returns a string to display the particles attributes"""
        return " Velocity: {} Position: {} Mass: {}".format(self.velocity, self.position, self.mass)

    def step(self, past_state, integrator, force, dt):
        """
        Completes one physics step, returning the resultant particle.
        Args:
            past_state (SystenState): The previous state of the system from which the state of the new Particle can be found.
            integrator (Integrator): The Integrator object which computes the new state of the Particle.
            force (Force): The Force object to find all the forces applied to the Particle.
            dt (float): The small timestep over which the integration is done.
        Return:
            Particle with the attributes of this particle at the next timestep.    
        """
        return integrator.integrate(past_state, self, force, dt)
    
    def get_position(self):
        """Returns this Particles position."""
        return self.position

    def get_velocity(self):
        """Returns this Particles velocity."""
        return self.velocity

    def get_mass(self):
        """Returns this Particles mass."""
        return self.mass

class SystemState:
    """
    Object for holding all the information concerning the physical system at some time.
    Attributes:
        particles (Particles[]): Array stores all the Particles in the system.
        num_particles (int): How many particles are in the system at this time.
        time (float): The time for which the object holds system information for.
    """

    def __init__(self, particles, time, dt):
        """
        Initialises a SystemState object.
        Args:
            particles (Particle[]): An array for the initial value of the particles.
            time (float): the initial time of the system.
        """
        self.particles = particles
        self.time = time

    def __str__(self):
        """Returns a string displaying the time and all the particles as a Particle.__str__. """
        string = ' '
        for particle in self.particles:
            string += "\n"
            string += str( particle )
        return string

    def step(self, integrator, force, dt):
        """"
        Computes a the next state of the system after a small time step.
        Args:
            integrator (Integrator): An Integrator to compute the numerical integration.
            force (Force): A Force object to compute the force on a particle.
            dt (float): The small timestep overwhich the the numerical integration is calculated.
        """
        new_system = SystemState([], self.time + dt, dt)
        for particle in self.particles:
            new_particle = particle.step(self, integrator, force, dt)
            new_system.add_particle(new_particle)
        return new_system

    def add_particle(self, particle):
        """
        Adds a particle to the SystemState.
        Args:
            particle (Particle): Adds this Particle to the SystemState.
        """
        self.particles.append(particle)

    def get_particle(self, i):
        return self.particles[i]

    def get_particles(self):
        return self.particles

    def get_time(self):
        return self.time

    def num_particles(self):
        return len(self.particles)

    def __mul__(self, other):
        error = 0
        for i in range(self.num_particles()):
            self_particle = self.get_particle(i)
            other_particle = other.get_particle(i)
            difference = self_particle.get_position() - other_particle.get_position()
            #print(" self_particle.get_position() = " + str(self_particle.get_position()))
            #print(" other_particle.get_position() = " + str(other_particle.get_position()))
            #print(" difference = " + str(difference))
            error += difference.norm()
        error /= self.num_particles()
        return error

class Enum:

    def __init__(self, state_list, start = None):
        self.state_list = state_list
        if start in state_list:
            self.state = start
        else:
            self.state = self.state_list[0]
        self.index = self.state_list.index(self.state)
        self.length = len(self.state_list)
        
    def cycle(self, n = 1):
        self.index = (self.index + n) % self.length
        self.state = self.state_list[self.index]

    def set(self, state):
        if state in self.state_list:
            self.state = state
            
    def set_index(self, i):
        if i < self.length:
            self.state = self.state_list[i]
            
    def get_state(self):
        return self.state

    def get_index(self):
        return self.index

    def get_state_list(self):
        return self.state_list
        

class Force:

    def earth_gravity(self, particle, state):
        return Vector(0, 9.81, 0)
    
    def n_body(self, particle, state):

        force = Vector(0,0,0)
        G = 1
        
        for i in state.get_particles():
            if i != particle:
                i_position = i.get_position()
                particle_position = particle.get_position()
                displacement = i_position - particle_position
                mass_poduct = i.get_mass() * particle.get_mass()
                factor = (G * mass_poduct) / (displacement.square_norm() * displacement.norm())
                attraction = displacement * factor
                force = force + attraction
        return force

    def earth_core(self, particle, state):
        earth_mass = 10
        earth_radius = 1
        G = 1
        distance = particle.get_position()
        numerator = G * particle.get_mass() * earth_mass
        denominator = earth_radius * earth_radius
        force = (-numerator / denominator) * particle.get_position()
        return force
        

    def __init__(self, G = 1):

        self.force_enum = Enum([self.earth_gravity, self.n_body, self.earth_core])
        self.G = G

    def cycle(self, n = 1):
        self.force_enum.cycle(n)

    def set_force(self, func):
        self.force_enum.set(func)

    def calculate(self, particle, state):
        func = self.force_enum.get_state()
        out = func(particle, state)
        return out

class Integrator:

    def euler_forwards(self, particle, state, force, dt):
        position = particle.get_position() + particle.get_velocity() * dt
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        return Particle(position, velocity, particle.get_mass())
    
    def euler_back(self, particle, state, force, dt):
        position = particle.get_position() + particle.get_velocity() * dt
        test_particle = Particle(position, particle.get_velocity(), particle.get_mass())
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        return Particle(position, velocity, particle.get_mass())

    def verlet(self, particle, state, force, dt):
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        position = particle.get_position() + velocity * dt
        return Particle(position, velocity, particle.get_mass())

    def midpoint(self, particle, state, force, dt):
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity_mid = particle.get_velocity() + acceleration * dt * 0.5
        position_mid = particle.get_position() + velocity_mid * dt * 0.5
        ref_particle = Particle(position_mid, velocity_mid, particle.get_mass())
        particle_force = force.calculate(ref_particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        position = particle.get_position() + velocity * dt
        return Particle(position, velocity, particle.get_mass())

    def rk4(self, particle, state, force, dt):
        particle_k1 = particle
        particle_k2 = verlet(partcicle_K1, state, force, dt/2)
        particle_k4 = verlet(partcicle_K1, state, force, dt)
        particle_k3 = verlet(particle_K4, state, force, -dt)
        k1 = force.calculate(partcicle_K1, state)
        k2 = force.calculate(partcicle_K2, state)
        k3 = force.calculate(partcicle_K3, state)
        k4 = force.calculate(partcicle_K4, state)
        particle_force = (1/6) * ( k1 + 2 * k2 + 2 * k3 + k4)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        position = particle.get_position() + velocity * dt
        return Particle(position, velocity, particle.get_mass())
        
        
    def __init__(self):

        self.integration_method = Enum([self.euler_forwards,
                                     self.euler_back,
                                     self.verlet,
                                     self.midpoint,
                                     self.rk4])

    def integrate(self, state, particle, force, dt):
        func = self.integration_method.get_state()
        out = func(particle, state, force, dt) 
        return out

    def switch(self, string):
        for method in self.integration_method.get_state_list():
            if method.__name__ == string:
                self.integration_method.set(method)
                
    def cycle(self, n):
        self.integration_method.cycle(n)

    def __str__(self):
        return self.integration_method.get_state().__name__


class System:

    def __init__(self, init_state, integrator, force, dt):
        
        self.states = [init_state]
        self.integrator = integrator
        self.force = force
        self.dt = dt

    def step(self, n = 1):
        for _ in range(n):
            old_state = self.states[-1]
            new_state = old_state.step(self.integrator, self.force, self.dt)
            self.states.append(new_state)
        return self.states[-1]

    def step_time(self, time):
        state = self.states[-1]
        while state.get_time() < time:
            state = self.step(1)
        return state
    
    def get_state(self, i):
        return self.states[i]

    def get_state_time(self, time):
        for state in self.states:
            if state.get_time() + self.get_dt()/2 >= time:
                return state
    
    def get_states(self):
        return self.states

    def get_dt(self):
        return dt

    def num_states(self):
        return len(self.states)

    def __str__(self):
        string = ''
        for state in self.states:
            string += " Time: "
            string += str(state.time)
            string += str(state)
            string += "\n \n"
        return string
    
    def __mul__(self, other):
        error = 0
        for i in range(self.num_states()):
            my_state    = self.get_state(i)
            other_state = other.get_state(i)
            error_change = my_state * other_state
            error += error_change
        error /= self.num_states()
        return error


class test:

    def __init__(self, integrator_name, force_name, init_condition_name, test, time):

        self.integrator = Integrator()
        self.integrator.switch(integrator_name)

        self.force = Force()
        self.force.switch(force_name)

        self.init_condition = None

        self.system = System(self.init_condition, self.integrator, self.force, self.dt)

        self.time = time

        self.ref = None

    #def set_ref(self, integrator, dt):
        #self.ref = System()
        

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


init_state = SystemState([p1, p2], 0, dt)

system_ref = System(init_state, integrator1, force, dt/100)
system1 = System(init_state, integrator1, force, dt)
system2 = System(init_state, integrator2, force, dt)

system_ref.step_time(1000)
system2.step_time(10)

import graphics as gr
import time

window = gr.GraphWin("Simulation", 1600, 1020)

def display_state(state, window):
    for particle in state.get_particles():
        position = particle.get_position()*50 + Vector(window.getWidth(), window.getHeight(), 0) / 2
        x,y,z = position.transpose()
        point = gr.Point(int(x), int(y))
        circle = gr.Circle(point,5)
        circle.draw(window)

def display_system(system):
    for i in range(system.num_states()):
        state = system.get_state(i)
        display_state(state, window)
        time.sleep(system.get_dt())
    







            




    
        
