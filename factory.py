'''
Challange:
Calculate areas of different shapes. Use the Factory design pattern.
We use factory pattern when the class instantiation is dynamic, and depends on an input
'''
from abc import ABC, abstractmethod

global pi
pi = 3.14

class Shape(ABC):
    
    @abstractmethod
    def calculateArea():
        '''
        Override this abstract method with the formula to calculate the area of the object
        Input: This is an abstract method
        '''
        pass

class Square(Shape):

    def __init__(self):
        print('Square object initiated successfully')
        self.length = int(input("Enter the length of the side of the square:"))
        area = self.calculateArea()
        print('The area of the square is: ',area)

    def calculateArea(self):
        '''
        Calculates the area of a circle 
        input: No inputs requires, function uses the objects length attribute.
        '''
        return self.length*self.length
    
class Circle(Shape):

    def __init__(self):
        print('Circle object initiated successfully')
        self.radius = int(input("Enter the radius of the circle:"))
        area = self.calculateArea()
        print('The area of the circle is: ',area)
        
    def calculateArea(self):
        '''
        Calculates the area of a circle 
        input: No inputs requires, function uses the objects length attribute.
        '''
        return pi * (self.radius*self.radius)

#As the method is defined as static, it will automatically be instantiated into the memory when the code is executed
class ShapeFactory:

    @staticmethod
    def buildShape(shape):
        '''
        Factory method instantiates a shape class based on the user input
        input: Shape that the user wants to calculate the area for.
        Execptions: Throws custom exception when the shape is neither a circle nor a square
        '''
        if shape.lower() == "square":
            return Square()  
        if shape.lower() == "circle":
            return Circle()
        if shape.lower() not in ['square,circle']:
            raise Exception("Only the area for Squares and Circles can be calculated currently")
        
if __name__ == "__main__":
    shape = input("Choose your shape: ")
    ShapeFactory.buildShape(shape)
