import math

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self._radius = radius
        elif diameter is not None:
            self._radius = diameter / 2
        else:
            raise ValueError("You must provide either radius or diameter")

    # 🎯 Decorators (getters)
    @property
    def radius(self):
        return self._radius

    @property
    def diameter(self):
        return self._radius * 2

    # ✅ Compute area
    def area(self):
        return math.pi * (self._radius ** 2)

    # ✅ String representation
    def __str__(self):
        return f"Circle(radius={self.radius:.2f})"

    # ✅ Add two circles
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        new_radius = self.radius + other.radius
        return Circle(radius=new_radius)

    # ✅ Greater than
    def __gt__(self, other):
        return self.radius > other.radius

    # ✅ Equal
    def __eq__(self, other):
        return self.radius == other.radius

    # ✅ Less than (needed for sorting)
    def __lt__(self, other):
        return self.radius < other.radius
    # Create circles
c1 = Circle(radius=5)
c2 = Circle(diameter=8)  # radius = 4

# Print
print(c1)
print(c2)

# Area
print("Area of c1:", c1.area())

# Add circles
c3 = c1 + c2
print("New circle after addition:", c3)

# Comparisons
print("c1 > c2:", c1 > c2)
print("c1 == c2:", c1 == c2)

# Sorting
circles = [c1, c2, c3]
circles.sort()

print("Sorted circles:")
for c in circles:
    print(c)