from numpy import sqrt

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
        """Returns (list <float>) the x,y,z coordinates of the Vector """
        return self.x, self.y, self.z

    def set_x(self, value):
        """Sets the x component of the Vector to a value (float)"""
        self.x = value
    def set_y(self, value):
        """Sets the y component of the Vector to a value (float)"""
        self.y = value
    def set_z(self, value):
        """Sets the z component of the Vector to a value (float)"""
        self.z = value

    def get_x(self):
        """returns the x value for this vector (float)"""
        return self.x
    def get_y(self):
        """returns the y value for this vector (float)"""
        return self.y
    def get_z(self):
        """returns the z value for this vector (float)"""
        return self.z


class Enum:

    def __init__(self, state_list, start = None):
        """Initialises a list of possitble states (list <any>) for the enum and a start value (any)"""
        self.state_list = state_list
        if start in state_list:
            self.state = start
        else:
            self.state = self.state_list[0]
        self.index = self.state_list.index(self.state)
        self.length = len(self.state_list)
        
    def cycle(self, n = 1):
        """Cycles through the nth (int) value of the enum"""
        self.index = (self.index + n) % self.length
        self.state = self.state_list[self.index]

    def set(self, state):
        """Sets the Enum to some state (any)"""
        if state in self.state_list:
            self.state = state
            
    def set_index(self, i):
        """returns the nth (int) value of teh Enum"""
        if i < self.length:
            self.state = self.state_list[i]
            
    def get_state(self):
        """Returns the current state of the Enum (any)"""
        return self.state

    def get_index(self):
        """gets the index of the current state of the Enum (int)"""
        return self.index

    def get_state_list(self):
        """Returns all possible states of the Enum (list <any>)"""
        return self.state_list
    
    def add(self, value):
        """Adds a state to the Enum (any)"""
        self.state_list.append(value)
