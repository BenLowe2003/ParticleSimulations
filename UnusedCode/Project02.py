Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = vector(1,2,3)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    v = vector(1,2,3)
TypeError: vector() takes no arguments

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    v = Vector(1,2,3)
TypeError: Vector() takes no arguments
v = Vector()
v
<__main__.Vector object at 0x000002904C602740>
print(v)
<__main__.Vector object at 0x000002904C602740>
type(v)
<class '__main__.Vector'>


= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector()
v
<__main__.Vector object at 0x0000025B8B722260>
print(v)
<__main__.Vector object at 0x0000025B8B722260>

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
v
<__main__.Vector object at 0x00000218682D27A0>
print(v)
<__main__.Vector object at 0x00000218682D27A0>
v.norm()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    v.norm()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 27, in norm
    return np.sqrt( self.squarenorm())
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 24, in squarenorm
    return x*x + y*y + z*z
NameError: name 'x' is not defined

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
v.norm()
3.7416573867739413
print(v)
<__main__.Vector object at 0x0000020895AD27A0>

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
v
<__main__.Vector object at 0x000001CE26672770>
print(v)
<__main__.Vector object at 0x000001CE26672770>


= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
print(v)
Vector: 1, 2, 3
w = Vector(2,3,4)
v+w
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    v+w
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 19, in __add__
    return vector(x,y,z)
NameError: name 'vector' is not defined. Did you mean: 'Vector'?

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)
w = Vector(2,3,4)
v+w
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    v+w
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 19, in __add__
    return vector(x,y,z)
NameError: name 'vector' is not defined. Did you mean: 'Vector'?
v-w
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    v-w
TypeError: unsupported operand type(s) for -: 'Vector' and 'Vector'
print(v+w)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(v+w)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 19, in __add__
    return vector(x,y,z)
NameError: name 'vector' is not defined. Did you mean: 'Vector'?

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
v = Vector(1,2,3)

w = Vector(2,3,4)

print(v+w)
Vector: 3, 5, 7

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
KeyboardInterrupt

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
main()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    main()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 249, in main
    integrator = Integrator()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 212, in __init__
    self.integrator_type = Enum([euler_forwards, euler_back, verlet, midpoint])
NameError: name 'euler_forwards' is not defined

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
main()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    main()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 254, in main
    force = Force()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 161, in __init__
    self.force_enum = Enum([earth_gravity, n_body])
NameError: name 'earth_gravity' is not defined

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
main()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    main()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 262, in main
    system = System(init_state, integrator, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 240, in __init__
    self.states = [innit_state]
NameError: name 'innit_state' is not defined. Did you mean: 'init_state'?

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
main()
<__main__.System object at 0x000002907D209420>
system = main()
system_state = system.states[1]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    system_state = system.states[1]
IndexError: list index out of range
system_state = system.states[0]
system_state
<__main__.SystemState object at 0x000002907D209630>
print(system_state)
<class '__main__.Particle'>
type(system_state)
<class '__main__.SystemState'>

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
Traceback (most recent call last):
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 253, in <module>
    integrator.cycle(C)
NameError: name 'C' is not defined

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
p1
<__main__.Particle object at 0x00000246E79D93C0>
print(p1)
Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1
print(init_state)
<class '__main__.Particle'>
init_state.__str__()
"<class '__main__.Particle'>"

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)

Called
<class '__main__.Particle'>

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)

[<class '__main__.Particle'>]
p1
<__main__.Particle object at 0x000001157F8793C0>
str(p1)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)
<class '__main__.Particle'>
[<class '__main__.Particle'>]
str(particle)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    str(particle)
NameError: name 'particle' is not defined. Did you mean: 'Particle'?
str(p1)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)

<class '__main__.Particle'>
[<class '__main__.Particle'>]

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)

Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    print(init_state)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 89, in __str__
    string += str(particle.get_position())
TypeError: Particle.get_position() missing 1 required positional argument: 'self'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(init_state)

Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    print(init_state)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 89, in __str__
    string += str( particle.get_position() )
TypeError: Particle.get_position() missing 1 required positional argument: 'self'
p = innit_state.get_particle(0)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    p = innit_state.get_particle(0)
NameError: name 'innit_state' is not defined. Did you mean: 'init_state'?
p = init_state.get_particle(0)
p
<class '__main__.Particle'>
str(p)
"<class '__main__.Particle'>"
str(p1)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'
[p1]
[<__main__.Particle object at 0x00000122F7F793C0>]
str([p1])
'[<__main__.Particle object at 0x00000122F7F793C0>]'
str(p1)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'
str(p)
"<class '__main__.Particle'>"
p == p1
False

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
init_state
<__main__.SystemState object at 0x000001978C509420>
str(init_state)
0, 0, 0
'[<__main__.Particle object at 0x000001978C5093C0>]'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(init_state)

'0, 0, 0'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(init_state)

'0, 0, 0'
p = init_state.get_particle(0)
str(p)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(init_state)
'Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(init_state)

'  Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'
str(system)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    str(system)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 261, in __str__
    string += str(self.time)
AttributeError: 'System' object has no attribute 'time'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(system)

Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    str(system)
TypeError: __str__ returned non-string (type SystemState)

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
str(system)

' Time0  Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1'
system.step()
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    system.step()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 248, in step
    new_state = old_state.step(this.integrator, this.force, this.dt)
NameError: name 'this' is not defined

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    system.step()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 248, in step
    new_state = old_state.step(self.integrator, self.force, self.dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 96, in step
    new_particle = particle.step(self, integrator, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 67, in step
    return integrator.integrate(past_state, self, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 220, in integrate
    out = func(self, particle, state, force)
TypeError: Integrator.euler_forwards() takes 4 positional arguments but 5 were given

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    system.step()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 248, in step
    new_state = old_state.step(self.integrator, self.force, self.dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 96, in step
    new_particle = particle.step(self, integrator, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 67, in step
    return integrator.integrate(past_state, self, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 220, in integrate
    out = func(particle, state, force, dt) # Eler Forwards
TypeError: Integrator.euler_forwards() takes 4 positional arguments but 5 were given

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    system.step()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 248, in step
    new_state = old_state.step(self.integrator, self.force, self.dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 96, in step
    new_particle = particle.step(self, integrator, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 67, in step
    return integrator.integrate(past_state, self, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 220, in integrate
    out = func(self, particle, state, force, dt) # Eler Forwards
TypeError: Integrator.euler_forwards() takes 5 positional arguments but 6 were given

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    system.step()
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 248, in step
    new_state = old_state.step(self.integrator, self.force, self.dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 96, in step
    new_particle = particle.step(self, integrator, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 67, in step
    return integrator.integrate(past_state, self, force, dt)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 220, in integrate
    out = func(particle, state, force, dt) # Eler Forwards
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 178, in euler_forwards
    particle_force = force.calculate(particle, state)
  File "C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py", line 172, in calculate
    out = func(self, particle, state)
TypeError: Force.earth_gravity() takes 3 positional arguments but 4 were given

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
<__main__.SystemState object at 0x0000026D0B0227D0>
str(system)
' Time0  Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1 Time0.1  Velocity: 1.0, 1.981, 0.0 Position: 0.1, 0.1, 0.0 Mass: 1'

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(Vector.__init__.__doc__)
Returns a Vector object.
Args:
    x (float): x component of the vector.
    y (float): y component of the vector.
    z (float): z component of the vector.
Return:
    Vector object with x,y,z components.
        
v = Vector(1,2,3)
v * 2
<__main__.Vector object at 0x0000020CA07827D0>
print(v)
1, 2, 3
w = v * 2
print(w)
2, 4, 6
w = 2 * v
w = 3*v
print(w)
3, 6, 9
w = v / 2
print(w)
0.5, 1.0, 1.5
system.step()
<__main__.SystemState object at 0x0000020CA70A9630>
print(system)
 Time0  Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1 Time0.1  Velocity: 1.0, 1.981, 0.0 Position: 0.1, 0.1, 0.0 Mass: 1

= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
<__main__.SystemState object at 0x0000011B6D5127D0>
print(system)
 Time0 
 Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1
 Time0.1 
 Velocity: 1.0, 1.981, 0.0 Position: 0.1, 0.1, 0.0 Mass: 1


= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
system.step()
<__main__.SystemState object at 0x00000223D12A27D0>
print(system)
 Time: 0 
 Velocity: 1, 1, 0 Position: 0, 0, 0 Mass: 1
 
 Time: 0.1 
 Velocity: 1.0, 1.981, 0.0 Position: 0.1, 0.1, 0.0 Mass: 1
 


= RESTART: C:\Users\benst\OneDrive\Documents\University\Year2\CodingPractice\Python\Project01.py
print(Particle.__init__.__doc__)
Initialises a Particle object.
        Args:
            position (Vector): A Vector containing the x,y,z components of the particles initial position.
            velocity (Vector): A Vector containing the x,y,z components of the particles initial velocity.
            mass (float): A float to store the particles mass.
        Returns:
            Particle object.
dir(Enum)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'cycle', 'get_index', 'get_state', 'set', 'set_index']
