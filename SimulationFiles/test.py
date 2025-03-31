from SimulationFiles.Path import Path
from SimulationFiles.Point import Point

points = [Point(0, 0, 0), Point(6, 1, 3), Point(8, 3, 4), Point(3, 5, 2), Point(1, 2, 1), Point(0, 0, 0)]
old_path = Path(points)

print("Old Path Points: " + str(old_path.decrypt_path()))
print("Old Path Distance: " + str(old_path.calculate_distance()))
print("Old Path Cost: " + str(old_path.calculate_cost(1, 1)))

distance_matrix = [
    [0, 2.24, 5.83, 6.08, 8.54],  # Distances from point 0 (origin)
    [2.24, 0, 3.61, 5.19, 7.07],  # Distances from point 1
    [5.83, 3.61, 0, 5, 5.39],  # Distances from point 2
    [6.08, 5.19, 5, 0, 2.83],  # Distances from point 3
    [8.54, 7.07, 5.39, 2.83, 0]  # Distances from point 4
]

new_path = Path(points, distance_matrix)
print("New Path Points: " + str(new_path.decrypt_path()))
print("New Path Distance: " + str(new_path.calculate_distance()))
print("New Path Cost: " + str(new_path.calculate_cost(1, 1)))
