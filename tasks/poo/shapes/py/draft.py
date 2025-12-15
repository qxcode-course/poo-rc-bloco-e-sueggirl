from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def get_name(self):
        pass


class Point2D:
    def __init__(self, coord_x: float, coord_y: float):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"{self.coord_x:.2f}, {self.coord_y:.2f}"


class Circle(Shape):
    def __init__(self, center_point: Point2D, radius_value: float):
        self.center_point = center_point
        self.radius_value = radius_value
        self.shape_name = "Circ"

    def get_name(self):
        return self.shape_name

    def get_area(self):
        return math.pi * (self.radius_value ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius_value

    def __str__(self):
        return f"{self.get_name()}: C=({self.center_point}), R={self.radius_value:.2f}"


class Rectangle(Shape):
    def __init__(self, point_a: Point2D, point_b: Point2D):
        self.point_a = point_a
        self.point_b = point_b
        self.shape_name = "Rect"

    def get_name(self):
        return self.shape_name

    def get_area(self):
        width = abs(self.point_b.coord_x - self.point_a.coord_x)
        height = abs(self.point_b.coord_y - self.point_a.coord_y)
        return width * height

    def get_perimeter(self):
        width = abs(self.point_b.coord_x - self.point_a.coord_x)
        height = abs(self.point_b.coord_y - self.point_a.coord_y)
        return 2 * (width + height)

    def __str__(self):
        return f"{self.get_name()}: P1=({self.point_a}) P2=({self.point_b})"


def main():
    shape_list = []

    while True:
        try:
            command_line = input()
            parts = command_line.split()
            command = parts[0]

            print("$" + command_line)

            if command == "circle":
                cx = float(parts[1])
                cy = float(parts[2])
                radius = float(parts[3])
                new_circle = Circle(Point2D(cx, cy), radius)
                shape_list.append(new_circle)

            elif command == "rect":
                x1 = float(parts[1])
                y1 = float(parts[2])
                x2 = float(parts[3])
                y2 = float(parts[4])
                new_rect = Rectangle(Point2D(x1, y1), Point2D(x2, y2))
                shape_list.append(new_rect)

            elif command == "show":
                for shape in shape_list:
                    print(shape)

            elif command == "info":
                for shape in shape_list:
                    print(
                        f"{shape.get_name()}: "
                        f"A={shape.get_area():.2f} "
                        f"P={shape.get_perimeter():.2f}"
                    )

            elif command == "end":
                break

            else:
                print("fail: command invalid")

        except Exception as error:
            print("fail:", error)


main()
