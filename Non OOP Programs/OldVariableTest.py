import math
import itertools
import random
from pandas import DataFrame
import time

HUMAN_WEIGHT = 5
BALL_WEIGHT = 1
NUMBER_OF_POINTS = 5
POINTS = [[0, 0], [8, 1], [5, 4], [10, 8], [8, 10], [5, 9], [1, 6], [0, 0], [0, 0]]
# Copy and paste a set of points here (origins included)

def pick_point():
    return random.randint(0, 10)


def distance(p1, p2):
    """
    Calculates the distance between
    two points in the Cartesian Plane
    """
    diff_x = p1[0] - p2[0]
    diff_y = p1[1] - p2[1]
    return math.sqrt(diff_x ** 2 + diff_y ** 2)


def point_cost(p1, p2, balls):
    """
    Calculates the cost of a segment of a route
    after factoring in weight of tennis balls and human
    """
    return distance(p1, p2) * (balls + w)


def calc_path(list_of_points):
    """
    Calculates the cost of a route
    Factors weight of human and ball into calculations
    """
    cost = 0
    balls = 0

    for points_set in range(len(list_of_points) - 1):
        p1 = list_of_points[points_set]
        p2 = list_of_points[points_set + 1]
        cost += point_cost(p1, p2, balls)
        balls += b

    return cost


def calc_distance(list_of_points):
    """
    Calculates distance of a route
    Ignores weight of ball and humans
    """
    raw_cost = 0

    for points_set in range(len(list_of_points) - 1):
        p1 = list_of_points[points_set]
        p2 = list_of_points[points_set + 1]
        raw_cost += point_cost(p1, p2, 0)

    return raw_cost


def insert_origins(a_list):
    a_list.insert(0, [0, 0])
    a_list.append([0, 0])
    return a_list


def get_min_dist_path(dictionary):
    # Initialize with the first key and its corresponding path cost
    min_dist = next(iter(dictionary))
    min_cost = calc_path(dictionary[min_dist])

    for dist in dictionary:
        current_cost = calc_path(dictionary[dist])
        if current_cost < min_cost:
            min_cost = current_cost
            min_dist = dist

    return dictionary[min_dist]



simulation_data = {
    "Human Weight": [],
    "Ball Weight": [],
    "Number of Points": [],
    "Minimum Cost - Our Algorithm": [],
    "Minimum Cost - Shortest Distance": [],
    "Distance of Path - Our Algorithm": [],
    "Shortest Distance": [],
    "Algorithm Path": [],
    "SD Path": [],
    "Cost Savings": [],
    "Time to Calculate (seconds)": []
}

print("Starting calculations...")

for iterations in range(1):
    # Setting up variables
    points_dictionary = {}
    start = time.time()

    w = HUMAN_WEIGHT
    b = BALL_WEIGHT
    n = NUMBER_OF_POINTS

    points = POINTS
    points.remove([0, 0])
    points.remove([0, 0])

    points_generator = itertools.permutations(points)

    point_calc_dic = {}  # Dictionary with each set of points and their cost

    dist_dic = {}  # Dictionary with each set of points and their cost
    list_of_dist = []  # List of each cost from each path

    # Storing all possible paths
    for k in list(points_generator):
        ilist = list(k)
        ilist.insert(0, [0, 0])
        ilist.append([0, 0])

        # Calculate cost and distance of the given path
        path_cost = round(calc_path(ilist), 2)
        path_distance = round(calc_distance(ilist), 2)

        # Store the path in point_calc_dic
        point_calc_dic[path_cost] = k

        # Check if the distance already exists in dist_dic
        if path_distance in dist_dic:
            # Compare the costs and update if the current path has a smaller cost
            existing_path = dist_dic[path_distance]
            existing_cost = calc_path(existing_path)
            if path_cost < existing_cost:
                dist_dic[path_distance] = k
        else:
            # Add the path to dist_dic if the distance does not exist
            dist_dic[path_distance] = k

    # Finding min, max, average costs/distances in set of costs/distances
    least_cost = min(point_calc_dic)
    min_distance = min(dist_dic)
    test = dist_dic[min_distance]
    # print(min_distance)
    min_distance_path = get_min_dist_path(dist_dic)
    min_distance = round(calc_distance(insert_origins(list(min_distance_path))), 2)

    # The path which gives minimum real world cost/distance
    min_path = list(point_calc_dic[least_cost])  # Change to minimum_cost
    shortest_distance_path = list(dist_dic[min_distance])  # Change to mincost_distance

    # Preparing paths for calculation
    insert_origins(min_path)
    insert_origins(shortest_distance_path)

    # Finding distance of real-world-cost path
    dist_of_lowest_cost_path = round(calc_distance(min_path), 2)
    # Finding cost of shortest path
    cost_of_shortest_path = round(calc_path(shortest_distance_path), 2)

    # Calculating distance differences & cost differences
    dist_difference_path = round(dist_of_lowest_cost_path - min_distance, 3)
    rw_diff_path = round(cost_of_shortest_path - least_cost, 3)

    # For each case if our algorithm cost < the shortest distance cost, add to longer drive
    longer_drive = rw_diff_path > 0
    # A trigger if there is an extra cost of being conscious about weight of balls --> The percent of the time that our
    # algorithm saves time
    end = time.time()
    time_to_calc = round(end - start, 4)

    simulation_data["Human Weight"].append(w)
    simulation_data["Ball Weight"].append(b)
    simulation_data["Number of Points"].append(n)
    simulation_data["Minimum Cost - Our Algorithm"].append(least_cost)
    simulation_data["Minimum Cost - Shortest Distance"].append(cost_of_shortest_path)
    simulation_data["Distance of Path - Our Algorithm"].append(dist_of_lowest_cost_path)
    simulation_data["Shortest Distance"].append(min_distance)
    simulation_data["Cost Savings"].append(rw_diff_path)
    simulation_data["Time to Calculate (seconds)"].append(time_to_calc)
    simulation_data["Algorithm Path"].append(min_path)
    simulation_data["SD Path"].append(shortest_distance_path)
    print(f"Finished scenario {iterations}")

my_dataframe = DataFrame(data=simulation_data)
my_dataframe.to_csv('old_var_test.csv')
print("Done!")