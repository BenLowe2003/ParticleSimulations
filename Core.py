from Primitives import *
from copy import deepcopy

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
        self.mass = float(mass)

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

    def get_momentum(self):
        return self.mass * self.velocity

    def get_energy(self):
        G  = 6.6743015e-11
        kinetic_energy = (1/2) * self.mass * self.velocity.square_norm()

        earth_mass = 5.97219e24
        earth_radius = 6378137
        G = 6.6743015e-11
        
        distance = self.get_position()
        numerator = G * self.get_mass() * earth_mass
        denominator = earth_radius * earth_radius * earth_radius
        potential_energy = (numerator / denominator) * distance.square_norm()

        return kinetic_energy + potential_energy
    

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
        for i in range(len(self.particles)):
            
            #new_state = deepcopy(self)
            #new_state.pop(i)
            
            new_particle = self.particles[i].step(self, integrator, force, dt)
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
        """Returns the ith (int) Particle (Particle)"""
        return self.particles[i]

    def get_particles(self):
        """Returns all the particles (list <Particle>)"""
        return self.particles

    def get_time(self):
        """Returns the simulation time of this state (float)"""
        return self.time

    def num_particles(self):
        """Returns the number of Particles stored in the state (int)"""
        return len(self.particles)

    def __mul__(self, other):
        """Compares this and some other (SystemState) returns the error (float) between them """
        error = 0
        for i in range(self.num_particles()):
            self_particle = self.get_particle(i)
            other_particle = other.get_particle(i)
            difference = self_particle.get_position() - other_particle.get_position()
            error += difference.norm()
        error /= self.num_particles()
        return error

    def total_momentum(self):
        """Returns the total momentum of the state (float)"""
        total_momentum = Vector(0,0,0)
        for particle in self.particles:
            total_momentum += particle.get_momentum()
        return total_momentum

    def centre_mass(self):
        """Returns the centre of mass of the state (Vector)"""
        centre = Vector(0,0,0)
        total_mass = 0
        for particle in self.particles:
            particle_position = particle.get_position()
            particle_mass = particle.get_mass()
            particle_contribution = particle_position * particle_mass
            total_mass += particle_mass
            centre += particle_contribution
        centre /= total_mass
        return centre

    def remove(self, particle):
        """Removes some input (Particle)"""
        self.particles.remove(particle)

    def pop(self, index):
        """Removes the ith (int) particle and returns it (Particle)"""
        particle = self.particles.pop(index)
        return particle

    def get_energy(self):
        """Finds the states energy for a earth_core system (float)"""
        total_energy = 0
        for particle in self.particles:
            total_energy = particle.get_energy()
        return total_energy
    


class Force:

    def earth_gravity(self, particle, state):
        """Returns the constant earther surface gravity (Vector) for a (Particle) and (SystemState)"""
        return Vector(0, -9.81, 0)

    def n_body(self, particle, state):
        """Returns the n-body force for a (Particle) and (SystemState)"""
        total_force = Vector(0, 0, 0)
        G =  6.6743015e-11
        for other_particle in state.get_particles():
            displacement = other_particle.get_position() - particle.get_position()
            denominator = displacement.norm() * displacement.square_norm()
            if other_particle != particle and denominator != 0:
                numerator = G * other_particle.get_mass() * particle.get_mass()
                attraction_force = (numerator / denominator) * displacement
                total_force += attraction_force
        return total_force

    def earth_core(self, particle, state):
        """Returns the earth core force for a (Particle) and (SystemState)"""
        earth_mass = 5.97219e24
        earth_radius = 6378137
        G = 6.6743015e-11
        
        distance = particle.get_position()
        numerator = G * particle.get_mass() * earth_mass
        denominator = earth_radius * earth_radius * earth_radius
        force = (-numerator / denominator) * particle.get_position()
        return force
        

    def __init__(self, G = 1):
        """Initialises a force object (Force)"""

        self.force_enum = Enum([self.earth_gravity, self.n_body, self.earth_core])
        self.G = G

    def cycle(self, n = 1):
        """Cycles through the different force calculation functions (int)"""
        self.force_enum.cycle(n)

    def set_force(self, func):
        """Sets the force function (function)"""
        self.force_enum.set(func)

    def switch(self, string):
        """switches to the force with some name (str)"""
        for method in self.force_enum.get_state_list():
            if method.__name__ == string:
                self.force_enum.set(method)

    def calculate(self, particle, state):
        """calculates the force for a (Particle) and (SystemState)"""
        func = self.force_enum.get_state()
        out = func(particle, state)
        return out

    def new_force(self, force):
        self.force_enum.add(force)

class Integrator:

    def euler_forwards(self, particle, state, force, dt):
        """Input (Particle), (SystemState), (Force), timestep (float) return next (Particle)"""
        position = particle.get_position() + particle.get_velocity() * dt
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        return Particle(position, velocity, particle.get_mass())
    
    def euler_back(self, particle, state, force, dt):
        """Input (Particle), (SystemState), (Force), timestep (float) return next (Particle)"""
        position = particle.get_position() + particle.get_velocity() * dt
        test_particle = Particle(position, particle.get_velocity(), particle.get_mass())
        particle_force = force.calculate(particle, state)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        return Particle(position, velocity, particle.get_mass())

    def semi_implicit_euler(self, particle, state, force, dt):
        """Input (Particle), (SystemState), (Force), timestep (float) return next (Particle)"""
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
        acceleration_mid = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration_mid * dt
        position = particle.get_position() + velocity * dt
        return Particle(position, velocity, particle.get_mass())

    def rk4(self, particle, state, force, dt):
        """Input (Particle), (SystemState), (Force), timestep (float) return next (Particle)"""
        k1 = force.calculate(particle, state)
        k2_particle = Particle(
            particle.get_position() + 0.5 * particle.get_velocity() * dt,
            particle.get_velocity() + 0.5 * k1 * dt,
            particle.get_mass())
        k2 = force.calculate(k2_particle, state)
        k3_particle = Particle(
            particle.get_position() + 0.5 * k2_particle.get_velocity() * dt,
            particle.get_velocity() + 0.5 * k2 * dt,
            particle.get_mass())
        k3 = force.calculate(k3_particle, state)
        k4_particle = Particle(
            particle.get_position() + k3_particle.get_velocity() * dt,
            particle.get_velocity() + k3 * dt,
            particle.get_mass())
        k4 = force.calculate(k4_particle, state)
        particle_force = (1/6) * (k1 + 2*k2 + 2*k3 + k4)
        acceleration = particle_force / particle.get_mass()
        velocity = particle.get_velocity() + acceleration * dt
        position = particle.get_position() + particle.get_velocity() * dt
        return Particle(position, velocity, particle.get_mass())
        
        
    def __init__(self):
        """Initialise a new Integrator"""

        self.integration_method = Enum([self.euler_forwards,
                                     self.euler_back,
                                     self.semi_implicit_euler,
                                     self.midpoint,
                                     self.rk4])

    def integrate(self, state, particle, force, dt):
        """Computes the integration for some (Particle), (SystemState), (Force), timestep (float) returning a Particle"""
        func = self.integration_method.get_state()
        out = func(particle, state, force, dt) 
        return out

    def switch(self, string):
        """Switch to a different integration method (str)"""
        for method in self.integration_method.get_state_list():
            if method.__name__ == string:
                self.integration_method.set(method)
                
    def cycle(self, n):
        """Cycle to a different integration method (int)"""
        self.integration_method.cycle(n)

    def __str__(self):
        return self.integration_method.get_state().__name__


class System:

    def __init__(self, init_state, integrator, force, dt):
        """initialises a System with initaial (SystemState), (Integrator), (Force) and timestep (float)"""
        
        self.states = [init_state]
        self.integrator = integrator
        self.force = force
        self.dt = dt

    def step(self, n = 1):
        """Computes n (int) integration steps returning the final (SystemState)"""
        for _ in range(n):
            old_state = self.states[-1]
            new_state = old_state.step(self.integrator, self.force, self.dt)
            self.states.append(new_state)
        return self.states[-1]

    def step_time(self, time):
        """computes steps until some time (float)"""
        state = self.states[-1]
        while state.get_time() < time:
            state = self.step(1)
        return state
    
    def get_state(self, i):
        """Returns tha (SystemState) with some index"""
        return self.states[i]

    def get_state_time(self, time):
        """Returns the (SystemState) for a certain input time (float)"""
        for state in self.states:
            if state.get_time() + self.get_dt()/2 >= time:
                return state
    
    def get_states(self):
        """Returns all (list <SystemStates>)"""
        return self.states

    def get_dt(self):
        """Returns the timestep (float)"""
        return self.dt

    def num_states(self):
        """Returns (int) the number of (SystemStates) stored"""
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
        """Returns (float) the total error between this and another (System) """
        error = 0
        for i in range(self.num_states()):
            my_state    = self.get_state(i)
            other_state = other.get_state(i)
            error_change = my_state * other_state
            error += error_change
        error /= self.num_states()
        return error

    def get_momentum(self):
        """Returns (list <float>) the momentum of all states"""
        momentum_list = []
        for state in self.states:
            momentum_list.append(state.total_momentum())
        return momentum_list
    
    def get_times(self):
        
        times_list = []
        for state in self.states:
            times_list.append(state.get_time())
        return times_list

    def get_energies(self):
        energy_list = [ state.get_energy() for state in self.states]
        return energy_list


