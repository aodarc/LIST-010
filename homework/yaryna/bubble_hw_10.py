import math
class Bubble:
    def __init__(self, radius = 0):
        self.__radius = radius

    def get_radius(self):
        return self.__radius


    def set_radius(self, radius):
        self.__radius = radius
        return self.__radius

    def volume(self):
        return (4/3)*math.pi*(self.__radius)**3

    def square(self):
        return 4*math.pi*(self.__radius)**2
        

    def __add__(self, other):
        total_volume = self.volume() + other.volume()
        return Bubble(((3*total_volume)/(4*math.pi))**(1/3))

    def __sub__(self, other):
        total_volume =abs(self.volume() - other.volume())
        return Bubble(((3*total_volume)/(4*math.pi))**(1/3))


bubble1 = Bubble()
bubble2 = Bubble()

bubble1.set_radius(5)
bubble2.set_radius(10)
print(bubble1.square())
print(bubble2.square())
bubble = bubble1 + bubble2
print(bubble.get_radius())
bubble = bubble1 - bubble2
print(bubble.get_radius())