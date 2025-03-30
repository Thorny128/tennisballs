class Path:
    def __init__(self, points, distance_matrix=None):
        self.points = points
        self.cost = 0
        self.distance = 0
        self.distance_matrix = distance_matrix

    def calculate_cost(self, w, b):
        self.cost = 0
        balls = 0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            self.cost += self.get_distance(p1, p2) * (balls + w)
            balls += b
        return self.cost

    def calculate_distance(self):
        self.distance = 0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            self.distance += self.get_distance(p1, p2)
        return self.distance

    def get_distance(self, p1, p2):
        if self.distance_matrix is not None:
            print(f"P1 Index: {p1.index} P2 Index: {p2.index}")
            # print(f"Distance from Matrix: {self.distance_matrix[p1.index][p2.index]}")
            return self.distance_matrix[p1.index-1][p2.index-1]
        else:
            return p1.distance_to(p2)

    def decrypt_path(self):
        return [[point.x, point.y] for point in self.points]