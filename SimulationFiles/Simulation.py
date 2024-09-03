import random
import itertools
import time
from pandas import DataFrame

from SimulationFiles.Path import Path
from SimulationFiles.Points import Point

RANGE_POINT_COORDS = 10
MAX_NUM_POINTS = 10


def pick_point():
    return Point(random.randint(0, RANGE_POINT_COORDS), random.randint(0, RANGE_POINT_COORDS))


def insert_origins(path):
    path.points.insert(0, Point(0, 0))
    path.points.append(Point(0, 0))


class Simulation:
    def __init__(self, num_simulations, num_points=None, human_weight=None, ball_weight=None, points=None):
        self.num_simulations = num_simulations
        self.human_weight = human_weight
        self.ball_weight = ball_weight
        self.num_points = num_points

        if points is not None:
            points.remove([0, 0])
            points.remove([0, 0])
            self.points = [Point(item[0], item[1]) for item in points]
            self.num_points = len(self.points)
        else:
            self.points = None

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
        for _ in range(self.num_simulations):
            start = time.time()

            w = self.human_weight if self.human_weight is not None else random.randrange(25, 200, 5)
            b = self.ball_weight if self.ball_weight is not None else random.randrange(25, 1000, 25) / 10
            n = self.num_points if self.num_points is not None else random.randint(3, MAX_NUM_POINTS)

            if self.points is None:
                self.points = [pick_point() for _ in range(n)]

            points_generator = itertools.permutations(self.points)

            point_calc_dic = {}
            dist_dic = {}

            for k in list(points_generator):
                path = Path(list(k))
                insert_origins(path)
                path_cost = round(path.calculate_cost(w, b), 5)
                path_distance = round(path.calculate_distance(), 5)

                point_calc_dic[path_cost] = k

                if path_distance in dist_dic:
                    existing_path = Path(list(dist_dic[path_distance]))
                    insert_origins(existing_path)
                    existing_cost = round(existing_path.calculate_cost(w, b), 5)
                    if path_cost < existing_cost:
                        dist_dic[path_distance] = k
                else:
                    dist_dic[path_distance] = k

            least_cost = min(point_calc_dic)
            min_distance = min(dist_dic)

            min_path = Path(list(point_calc_dic[least_cost]))
            shortest_distance_path = Path(list(dist_dic[min_distance]))

            insert_origins(min_path)
            insert_origins(shortest_distance_path)

            dist_of_lowest_cost_path = min_path.calculate_distance()
            cost_of_shortest_path = shortest_distance_path.calculate_cost(w, b)

            dist_difference_path = dist_of_lowest_cost_path - min_distance
            rw_diff_path = cost_of_shortest_path - least_cost

            time_to_calc = time.time() - start

            self.simulation_data["Human Weight"].append(w)
            self.simulation_data["Ball Weight"].append(b)
            self.simulation_data["Number of Points"].append(n)
            self.simulation_data["Minimum Cost - Our Algorithm"].append(round(least_cost, 3))
            self.simulation_data["Minimum Cost - Shortest Distance"].append(round(cost_of_shortest_path, 3))
            self.simulation_data["Distance of Path - Our Algorithm"].append(round(dist_of_lowest_cost_path, 3))
            self.simulation_data["Shortest Distance"].append(round(min_distance, 3))
            self.simulation_data["Cost Savings"].append(round(rw_diff_path, 3))
            self.simulation_data["Time to Calculate (seconds)"].append(round(time_to_calc, 4))
            self.simulation_data["Algorithm Path"].append(min_path.decrypt_path())
            self.simulation_data["SD Path"].append(shortest_distance_path.decrypt_path())

            self.points = None
            print(f"Finished simulation {_ + 1} of {self.num_simulations}")

    def save_to_csv(self, filename):
        df = DataFrame(data=self.simulation_data)
        df.to_csv(filename)
