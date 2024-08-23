import math
import itertools
import statistics
import random

HUMAN_WEIGHT = 5
BALL_WEIGHT = 1
NUMBER_OF_SIMULATIONS = 1000
NUMBER_OF_POINTS = 5

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


def pointCost(p2, p1, b):
    """
    Calculates the cost of a segment of a route
    after factoring in weight of tennis balls and humani
    """
    return distance(p1, p2) * (b + w)


def calcPath(list_of_points):
    """
    Calculates the cost of a path when given a list of points
    """
    cost = 0
    balls = 0

    for i in range(len(list_of_points) - 1):
        p1 = list_of_points[i]
        p2 = list_of_points[i + 1]
        cost += pointCost(p1, p2, balls)
        balls += b

    return cost


def calcDistance(list_of_points):
    """
    Calculates the cost of a path when given a list of points
    """
    raw_cost = 0

    for i in range(len(list_of_points) - 1):
        p1 = list_of_points[i]
        p2 = list_of_points[i + 1]
        raw_cost += pointCost(p1, p2, 0)

    return raw_cost


def insert_origins(list):
    list.insert(0, [0, 0])
    list.append([0, 0])
    return list


points_dictionary = {}

# Change values here
w = HUMAN_WEIGHT
b = BALL_WEIGHT

min_costs_list = []
max_costs_list = []
avg_costs_list = []

min_dist_list = []
max_dist_list = []
avg_dist_list = []

dist_diff_list = []
rw_diff_list = []
longer_drive_list = []

for j in range(NUMBER_OF_SIMULATIONS):
    for i in range(NUMBER_OF_POINTS):
        points_dictionary[i] = [pick_point(), pick_point()]

    # Finding all combinations of points from the dictionary
    points = []
    for key in points_dictionary:
        points.append(points_dictionary[key])

    points_generator = itertools.permutations(points)

    point_calc_dic = {}  # Dictionary with each set of points and their cost
    list_of_costs = []  # List of each cost from each path

    dist_dic = {}  # Dictionary with each set of points and their cost
    list_of_dist = []  # List of each cost from each path

    # Storing all possible paths
    for k in list(points_generator):
        ilist = list(k)
        ilist.insert(0, [0, 0])
        ilist.append([0, 0])

        # Calculates cost of the given path, same for raw
        list_of_costs.append(round(calcPath(ilist), 2))
        point_calc_dic[round(calcPath(ilist), 2)] = k

        list_of_dist.append(round(calcDistance(ilist), 2))
        dist_dic[round(calcDistance(ilist), 2)] = k

    # Finding min, max, average costs in this set
    minimum_cost = min(list_of_costs)
    maximum_cost = max(list_of_costs)
    average_cost = round(statistics.fmean(list_of_costs), 2)

    # The path which gives minimum real world cost (in tuple form)
    min_path = list(point_calc_dic[min(list_of_costs)])
    shortest_distance = list(dist_dic[min(list_of_dist)])

    # Preparing path for calculation
    insert_origins(min_path)
    insert_origins(shortest_distance)

    # Finding distance of real-world-cost path
    dist_of_lowest_cost_path = round(calcDistance(min_path), 2)
    # Finding cost of shortest path
    pathCalc_of_shortestPath = round(calcPath(shortest_distance), 2)

    mincost_distance = min(list_of_dist)
    maxcost_distance = max(list_of_dist)
    avgcost_distance = round(statistics.fmean(list_of_dist), 2)

    # Calculating distance differences & cost differences
    dist_difference_path = dist_of_lowest_cost_path - mincost_distance
    rw_diff_path = pathCalc_of_shortestPath - minimum_cost

    # For each case if our algorithm cost < shortest distance cost, add to longer drive
    longer_drive = 0
    if (rw_diff_path > 0):
        longer_drive = 1  # A trigger if there is an extra cost of being concious about weight of balls --> The percent of the time that our algorithm saves time

    min_costs_list.append(minimum_cost)
    max_costs_list.append(maximum_cost)
    avg_costs_list.append(average_cost)

    min_dist_list.append(mincost_distance)
    max_dist_list.append(maxcost_distance)
    avg_dist_list.append(avgcost_distance)

    dist_diff_list.append(dist_difference_path)  # Difference of distances
    rw_diff_list.append(rw_diff_path)  # Difference of Real World costs
    longer_drive_list.append(longer_drive)

print(f"Minimum Cost Avg: {round(statistics.fmean(min_costs_list), 2)}")
print(f"Maximum Cost Avg: {round(statistics.fmean(max_costs_list), 2)}")
print(f"Average Cost Avg: {round(statistics.fmean(avg_costs_list), 2)}")
print(f"Shortest Distance Avg: {round(statistics.fmean(min_dist_list), 2)}")
print(f"Longest Distance Avg: {round(statistics.fmean(max_dist_list), 2)}")
print(f"Average Distance Avg: {round(statistics.fmean(avg_dist_list), 2)}\n")

print(f"Avg Distance Difference: {round(statistics.fmean(dist_diff_list), 2)}")
print(f"Avg Real-world Cost Difference: {round(statistics.fmean(rw_diff_list), 2)}")
print(f"Longer drive percentage: {round(100 * statistics.fmean(longer_drive_list), 3)}%")
