import re
from Core import Particle, Vector

"""
I'm having to put the masses directly into code.
The masses in ephemerids use different formats and units for every planet.
So the code layed put here can't be generalised to any planet unlike Ephemerids.py
"""



def epheperid_to_particle(ephemerid, mass, index = 0):


    
    position_pattern = r"X\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)\s+Y\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)\s+Z\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)"
    match = re.findall(position_pattern, ephemerid)
    xyz = match[index]
    x = float(xyz[0])
    y = float(xyz[1])
    z = float(xyz[2])
    
    velocity_pattern = r"VX\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)\s+VY\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)\s+VZ\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)"
    match = re.findall(position_pattern, ephemerid)
    xyz = match[index]
    vx = float(xyz[0])
    vy = float(xyz[1])
    vz = float(xyz[2])
    position = Vector(x, y, z)
    velocity = Vector(vx, vy, vz)
    return Particle(position, velocity, mass)


file = open("Sun.txt", "r")
sun = file.read()
file.close()
file = open("Mercury.txt", "r")
mercury = file.read()
file.close()
file = open("Venus.txt", "r")
venus = file.read()
file.close()
file = open("Earth.txt", "r")
earth = file.read()
file.close()
file = open("Mars.txt", "r")
mars = file.read()
file.close()
file = open("Jupiter.txt", "r")
jupiter = file.read()
file.close()
file = open("Saturn.txt", "r")
saturn = file.read()
file.close()
file = open("Uranus.txt", "r")
uranus = file.read()
file.close()
file = open("Neptune.txt", "r")
neptune = file.read()
file.close()

planets = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
masses = [19885e26, 3.302e23, 48.685e23, 5.97219e24, 6.4171e23, 189818722e22,
          5.6834e26, 86.813e24, 102.409e24]

          
start_planet_particles = []
for i in range(9):
    planet = planets[i]
    mass = masses[i]
    planet_particle = epheperid_to_particle(planet, float(mass))
    start_planet_particles.append(planet_particle)

end_planet_particles = []
for i in range(9):
    planet = planets[i]
    mass = masses[i]
    planet_particle = epheperid_to_particle(planet, float(mass), 29)
    end_planet_particles.append(planet_particle) 
