# Tennis Balls
## Code Structure
The code is created using Object-Oriented Programming. It consists of classes which are used to create objects.
Each object contains methods (functions) and attributes (variables). As an example, a car factory (the class) is
producing cars (the object). Each car has specific attributes (e.g. color, trim level) and methods 
(e.g. driving, starting).

All files related to the simulation are in the SimulationFiles folder. Do not store other, unrelated files in this
folder.

The codebase uses Object-Oriented Programming due to there being multiple points and paths, and for simplicity to
modify later. Read on to explore the inner workings of the code.

A quick overview for the methods:
* For each method, there is a `self` object. You do not have to type this out. It is here in the documentation and in 
the classes, but you do not have to worry about it to understand the code.
* The __init__ method is the constructor. Every time you make a new object, you pass in values for the constructor.
For example, if I want to make a new point I will write `myPoint = Point(1, 2)`. The `1` is passed in as `x` in the
`__init__` method, and the `2` is passed in as `y`. This gives `myPoint` attributes `x=1` and `y=2`.

### Class: Points
- **Attributes:**
  - `x`: The x-coordinate of the point.
  - `y`: The y-coordinate of the point.

- **Methods:**
  - `__init__(self, x, y)`: Initializes a new instance of the `Point` class with the given x and y coordinates.
  - `distance_to(self, other_point)`: Calculates the Euclidean distance from the current point to another point.

**Example Usage**
```python
from SimulationFiles.Points import Point

pointA = Point(1, 2)
pointB = Point(3, 5)

print(pointA.x) # Returns 1
print(pointB.distance_to(pointA)) # Returns √21, ~5.38
```