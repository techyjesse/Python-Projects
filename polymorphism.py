import math


# parent class
class Polygons:

    def number_of_sides(self):
        return 0

    def area(self):
        return 0

    def perimeter(self):
        return 0

# child class inherits properties from parent class
class Pentagon(Polygons):
    # models properties of a pentagon

    def number_of_sides(self):
        return 5

    def area(self, a):
        # formula that returns the area of a pentagon
        return 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2

    def perimeter(self, a):
        return 5 * a

# another child class
class Triangle(Polygons):
    # models properties of triangle

    def number_of_sides(self):
        return 3
    # forumla that returns the area of a triangle
    def area(self, base, height):
        return 1 / 2 * base * height
    # formula that returns the perimiter of a triangle with an else if loop to ensure input is correct.
    def perimeter(self, a, b, c):
        if a + b > c:
            return a + b + c
        else:
            return "Invalid input: make sure a + b > c"


if __name__ == "__main__":
    pent = Pentagon()
    print("Pentagon Area:", pent.area(5))
    print("Perimeter:", pent.perimeter(7.5))
    print("-----------------")

    tri = Triangle()
    print("Triangle Area:", tri.area(10, 20))
    print("Perimeter:", tri.perimeter(20, 60, 75))
    print("-----------------")
