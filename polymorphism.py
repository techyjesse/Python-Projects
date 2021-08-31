from math import pi

# parent class

class Shapes:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass
    def fact(self):
        return "I am a two-dimensional shape."
        
    
# child class with it's own functions

class Circle(Shapes):
    def __init__(self, radius, color):
        super().__init__("Circle")
        self.radius = radius
        self.color = color

    def area(self):
        return pi*self.radius**2

        
# another child class with it's own functions

class Square(Shapes):
    def __init__(self, length, height):
        super().__init__("Square")
        self.length = length
        self.height = height

    def area(self):
        return self.length*self.height

    def fact(self):
        return "All angles in a square are equal."

        
        
        

if __name__ == "__main__":

    
    a = Square(5,5)
    b = Circle(9,'Red')
    print(a.fact())
    print("The area of the square is: ", a.area())
    print("The area of the circle is: ", b.area())
    


    
