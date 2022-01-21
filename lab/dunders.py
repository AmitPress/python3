import math
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __del__(self): # does not work with pypy
        print("getting bye")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __len__(self):

        return int(math.sqrt(self.x**2 + self.y**2))
v1 = Vector(23, 56)
v2 = Vector(56, 78)

v = v1 + v2

print(v.x, v.y)
v3 = Vector(12, -5)
l = len(v3)
print(l)
