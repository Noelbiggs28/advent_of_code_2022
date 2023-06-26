class Tree:
    def __init__(self, height, y , x):
        self.name = f'{y}{x}'
        self.height = int(height)
        self.x_coord = x
        self.y_coord = y
        self.spotted = False
        self.scenic_score = 1