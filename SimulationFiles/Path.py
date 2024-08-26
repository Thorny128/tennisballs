class Path:
    def __init__(self, points):
        self.points = points
        self.cost = 0
        self.distance = 0

    def calculate_cost(self, w, b):
        self.cost = 0
        balls = 0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            self.cost += p1.distance_to(p2) * (balls + w)
            balls += b
        return self.cost

    def calculate_distance(self):
        self.distance = 0
        for i in range(len(self.points) - 1):
            p1 = self.points[i]
            p2 = self.points[i + 1]
            self.distance += p1.distance_to(p2)
        return self.distance

    def decrypt_path(self):
        return [[point.x, point.y] for point in self.points]