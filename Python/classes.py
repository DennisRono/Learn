# Simple class example
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

point = Point(3, 4)
point.move(2, 1)
print(f"Point coordinates: ({point.x}, {point.y})")  # Output: Point coordinates: (5, 5)
