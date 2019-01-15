from math import pi

class Bubble:
    def __init__(self, radius=None, capacity=None):
        if radius is None:
            self.capacity = capacity
            self.radius = ((3*self.capacity)/(4*pi))**(1/3)
        else:
            self.radius = radius
            self.capacity = (4*pi*(self.radius**3))/3
        
    @property
    def square(self):
        square = 4*pi*(self.radius**2)
        return square

    #setting the rules for addition and subtraction of
    #two spheres and returning new sphere object as a result

    def __add__(self, other):
        return Bubble(self.radius + other.radius)

    def __sub__(self, other):
        if self.radius >= other.radius:
            return Bubble(self.radius - other.radius)
        else:
            raise ValueError("Cannot set negative value for a radius")

a = Bubble(None, 1)
b = Bubble(None, 4)

print(a.radius, b.radius)
print(a.capacity, b.capacity)
print(a.square, b.square)

c = a+b

print(c.radius)
print(c.capacity)
print(c.square)
