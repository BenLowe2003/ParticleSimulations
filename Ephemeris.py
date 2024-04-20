import re
from Core import Particle, Vector

mass_patterns = [r"Mass,\s*10\^24\s*kg\s*=\s*~?(\d+(?:,\d{3})*)(?:\.\d+)?",
                 r"Mass\s+x10\^?23\s*\(kg\)\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)",
                 r"Mass\s+x10\^?24\s*\(kg\)\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)",
                 r"Mass\s+x\s*10\^?22\s*\(g\)\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)",
                 r"Mass\s+x10\^?26\s*\(kg\)\s*=\s*([-+]?\d*\.?\d+(?:[Ee][-+]?\d+)?)"]

scales = [10 ** 24, 10 ** 23, 19 ** 24, 10 ** 22, 10 ** 26] 

def epheperid_to_particle(ephemerid, index = 0):
    
    for i in range(len(mass_patterns)):
        match = re.search(mass_patterns[i], ephemerid)
        if match:
            scale = scales[i]
            break
    mass = float(match.group(1)) * scale
    
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

planet_names = ['Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn'
                , 'Uranus', 'Neptune']

planet_names = ['Planets/' + name + '.txt' for name in planet_names]
files = [ open(name, 'r') for name in planet_names]
planets = [file.read() for file in files]

start_planet_particles = [epheperid_to_particle(planet) for planet in  planets]
end_planet_particles = [epheperid_to_particle(planet, -1) for planet in  planets]
