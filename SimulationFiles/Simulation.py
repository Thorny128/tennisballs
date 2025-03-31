import random
import itertools
import time
from pandas import DataFrame

from SimulationFiles.Path import Path
from SimulationFiles.Point import Point

RANGE_POINT_COORDS = 10
MAX_NUM_POINTS = 10

# Inserts [0, 0] on both sides of a path
def insert_origins(path):
    path.points.insert(0, Point(0, 0, 0))
    path.points.insert(path.get_length(), Point(0, 0, 0))

class Simulation:
    def __init__(self, num_simulations, distance_matrix, points, human_weight=None, ball_weight=None):
        self.num_simulations = num_simulations
        self.u_human_weight = human_weight
        self.u_ball_weight = ball_weight
        self.distance_matrix = distance_matrix

        points.remove([0, 0])
        points.remove([0, 0])
        self.points = [Point(item[0], item[1], index= i + 1) for i, item in enumerate(points)]
        self.u_num_points = len(self.points)


        # Initializing the simulation data
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
            "Time to Calculate (seconds)": [],
        }

        for i in range(MAX_NUM_POINTS + 2):
            self.simulation_data[f"Point {i}"] = []

    def run_simulation(self):
        for _ in range(self.num_simulations):
            start = time.time()

            # Getting values or randomly generating them
            human_weight = self.u_human_weight if self.u_human_weight is not None else random.randrange(25, 200, 5)
            ball_weight = self.u_ball_weight if self.u_ball_weight is not None else random.randrange(25, 1000, 25) / 10
            number_of_points = self.u_num_points if self.u_num_points is not None else random.randint(3, MAX_NUM_POINTS)

            points_generator = itertools.permutations(self.points)

            point_calc_dic = {}
            dist_dic = {}

            # Main logic - calculating all paths and putting their data in dictionaries
            for k in list(points_generator):
                path = Path(list(k), self.distance_matrix)
                insert_origins(path)
                path_cost = round(path.calculate_cost(human_weight, ball_weight), 5)
                path_distance = round(path.calculate_distance(), 5)

                point_calc_dic[path_cost] = path

                if path_distance in dist_dic:
                    existing_path = dist_dic[path_distance]
                    existing_cost = round(existing_path.calculate_cost(human_weight, ball_weight), 5)
                    if path_cost < existing_cost:
                        dist_dic[path_distance] = path
                else:
                    dist_dic[path_distance] = path

            # Finding useful data
            least_cost = min(point_calc_dic)
            min_distance = min(dist_dic)

            min_path = point_calc_dic[least_cost]
            shortest_distance_path = dist_dic[min_distance]

            dist_of_lowest_cost_path = min_path.calculate_distance()
            cost_of_shortest_path = shortest_distance_path.calculate_cost(human_weight, ball_weight)

            dist_difference_path = dist_of_lowest_cost_path - min_distance
            rw_diff_path = cost_of_shortest_path - least_cost

            time_to_calc = time.time() - start

            self.simulation_data["Human Weight"].append(human_weight)
            self.simulation_data["Ball Weight"].append(ball_weight)
            self.simulation_data["Number of Points"].append(number_of_points)
            self.simulation_data["Minimum Cost - Our Algorithm"].append(round(least_cost, 3))
            self.simulation_data["Minimum Cost - Shortest Distance"].append(round(cost_of_shortest_path, 3))
            self.simulation_data["Distance of Path - Our Algorithm"].append(round(dist_of_lowest_cost_path, 3))
            self.simulation_data["Shortest Distance"].append(round(min_distance, 3))
            self.simulation_data["Cost Savings"].append(round(rw_diff_path, 3))
            self.simulation_data["Time to Calculate (seconds)"].append(round(time_to_calc, 4))
            self.simulation_data["Algorithm Path"].append(min_path.decrypt_path())
            self.simulation_data["SD Path"].append(shortest_distance_path.decrypt_path())

            for i in range(MAX_NUM_POINTS + 2):
                if i <= number_of_points + 1:
                    self.simulation_data[f"Point {i}"].append(min_path.decrypt_path()[i])
                else:
                    self.simulation_data[f"Point {i}"].append(None)

            self.points = None
            print(f"Finished simulation {_ + 1} of {self.num_simulations}")

    def save_to_csv(self, filename):
        df = DataFrame(data=self.simulation_data)
        df.to_csv(filename)