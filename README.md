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

### Class: Point
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

### Class: Path

- **Attributes:**
  - `points`: A list of `Point` objects representing the path.
  - `cost`: The total cost of the path
  - `distance`: The total distance of the path

- **Methods:**
  - `__init__(self, points)`: Initializes a new instance of the `Path` class with the given list of points.
  - `calculate_cost(self, w, b)`: Calculates the cost of the path based on the given human weight `w` and ball weight 
  `b`.
  - `calculate_distance(self)`: Calculates the total distance of the path.
  - `decrypt_path(self)`: Returns a representation of the path as a list, instead of `Point` objects

**Example Usage**
```python
from SimulationFiles.Path import Path
from SimulationFiles.Points import Point

points = [Point(0, 0), Point(1, 2), Point(3, 5), Point(0, 0)]
path = Path(points)

print(path.points) # Returns the list of points as Point objects
print(path.calculate_distance()) # Returns the total distance of the path
print(path.decrypt_path()) # Returns [[0, 0], [1, 2], [3, 5], [0, 0]]
```

### Class: Simulation
- **Global Variables:**
  - `RANGE_POINT_COORDS`: Defines the range for point coordinates when generated randomly, controlling how far out the point values can get.
  - `MAX_NUM_POINTS`: Defines the maximum number of points that can be generated randomly.
- **Attributes:**
  - `num_simulations`: The number of simulations to run.
  - `human_weight`: The weight of the human. Randomly set between 25 and 200 if not provided.
  - `ball_weight`: The weight of the ball. Randomly set between 2.5 and 100 if not provided.
  - `num_points`: The number of points in the path. Randomly set between 3 and `MAX_NUM_POINTS` if not provided.
  Automatically set to the number of non-origin points in the `points` attribute if `points` is given.
  - `points`: A list within a list representing a path with points. Randomly generated with values ranging from 0 to 
  `RANGE_POINT_COORDS` if not provided.
  - `simulation_data`: A dictionary to store the results of the simulation.

- **Methods:**
  - `__init__(self, num_simulations, human_weight=None, ball_weight=None, num_points=None, points=None)`: Initializes a 
  new instance of the `Simulation` class with the given parameters.
  - `run_simulation(self)`: Runs the simulation for `num_simulation` times and stores the results in 
  `simulation_data`.
  - `save_to_csv(self, filename)`: Saves the simulation data to a CSV file with the given filename.

**Example Usage**
```python
from SimulationFiles.Simulation import Simulation

# Creating a simulation with some given attributes
simulation = Simulation(num_simulations=10, human_weight=70, ball_weight=5, num_points=5)

# Running the simulation and saving data to a file
simulation.run_simulation()
simulation.save_to_csv('simulation_results.csv')


# Leveraging the power of OOP: Running multiple simulations at the same time
# There are ways to make this more efficient, but this way is the easiest to understand
heavy_ball_sim = Simulation(num_simulations=1000, ball_weight = 300)
heavy_human_sim = Simulation(num_simulations=1000, human_weight=1000)
interesting_points_sim = Simulation(num_simulations=1000, points=[[0, 0], [1, 1], [-1, 1], [-1, -1], [1, -1]])

heavy_ball_sim.run_simulation()
heavy_human_sim.run_simulation()
interesting_points_sim.run_simulation()

heavy_ball_sim.save_to_csv('heavy_ball_sim_results.csv')
heavy_human_sim.save_to_csv('heavy_human_sim_results.csv')
interesting_points_sim.save_to_csv('interesting_points_sim.csv')
```