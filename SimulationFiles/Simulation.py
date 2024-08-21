import random
import itertools
import time
from pandas import DataFrame

from SimulationFiles.Path import Path
from SimulationFiles.Points import Point

RANGE_POINT_COORDS = 10


def pick_point():
    return Point(random.randint(0, RANGE_POINT_COORDS), random.randint(0, RANGE_POINT_COORDS))


def insert_origins(path):
    path.points.insert(0, Point(0, 0))
    path.points.append(Point(0, 0))


def get_min_dist(dist_dic, w, b):
    min_dist = min(dist_dic)
    min_path = Path(list(dist_dic[min_dist]))
    insert_origins(min_path)
    min_cost = min_path.calculate_cost(w, b)

    for curr_dist in dist_dic:
        if curr_dist == min_dist:
            curr_path = Path(list(dist_dic[curr_dist]))
            insert_origins(curr_path)
            curr_cost = curr_path.calculate_cost(w, b)
            if curr_cost < min_cost:
                min_dist = curr_dist

    return min_dist


class Simulation:
    def __init__(self, num_simulations, num_points, human_weight, ball_weight, points=None):
        self.num_simulations = num_simulations
        self.human_weight = human_weight
        self.ball_weight = ball_weight
        self.num_points = num_points

        if points is not None:
            self.points = [Point(item[0], item[1]) for item in points]
            self.num_points = len(self.points)
        else:
            self.points = [pick_point() for _ in range(num_points)]

        self.simulation_data = {
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

    def run_simulation(self):
        start = time.time()
        for _ in range(self.num_simulations):
            w = self.human_weight
            b = self.ball_weight
            n = self.num_points

            points_generator = itertools.permutations(self.points)

            point_calc_dic = {}
            dist_dic = {}

            for k in list(points_generator):
                path = Path(list(k))
                insert_origins(path)
                path_cost = round(path.calculate_cost(w, b), 2)
                path_distance = round(path.calculate_distance(), 2)

                point_calc_dic[path_cost] = k
                if path_distance in dist_dic:
                    existing_path = Path(dist_dic[path_distance])
                    if path_cost < existing_path.calculate_cost(w, b):
                        dist_dic[path_distance] = k
                else:
                    dist_dic[path_distance] = k

            least_cost = min(point_calc_dic)
            min_distance = get_min_dist(dist_dic, w, b)

            min_path = Path(list(point_calc_dic[least_cost]))
            shortest_distance_path = Path(list(dist_dic[min_distance]))

            insert_origins(min_path)
            insert_origins(shortest_distance_path)

            dist_of_lowest_cost_path = round(min_path.calculate_distance(), 2)
            cost_of_shortest_path = round(shortest_distance_path.calculate_cost(w, b), 2)

            dist_difference_path = round(dist_of_lowest_cost_path - min_distance, 3)
            rw_diff_path = round(cost_of_shortest_path - least_cost, 3)

            time_to_calc = round(time.time() - start, 4)

            self.simulation_data["Human Weight"].append(w)
            self.simulation_data["Ball Weight"].append(b)
            self.simulation_data["Number of Points"].append(n)
            self.simulation_data["Minimum Cost - Our Algorithm"].append(least_cost)
            self.simulation_data["Minimum Cost - Shortest Distance"].append(cost_of_shortest_path)
            self.simulation_data["Distance of Path - Our Algorithm"].append(dist_of_lowest_cost_path)
            self.simulation_data["Shortest Distance"].append(min_distance)
            self.simulation_data["Cost Savings"].append(rw_diff_path)
            self.simulation_data["Time to Calculate (seconds)"].append(time_to_calc)
            self.simulation_data["Algorithm Path"].append(min_path.decrypt_path())
            self.simulation_data["SD Path"].append(shortest_distance_path.decrypt_path())

    def save_to_csv(self, filename):
        df = DataFrame(data=self.simulation_data)
        df.to_csv(filename)
