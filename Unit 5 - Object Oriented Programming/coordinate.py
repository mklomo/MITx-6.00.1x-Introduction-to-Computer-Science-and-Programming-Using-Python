# Coordinate class 

"""
    This class takes the x and y values
    
    type(x) = float
    
    type(y) = float
"""

class Coordinate(object):

    # Lets initialize the  class and assign attributes
    def  __init__(self, x, y):

        self.x = x

        self.y = y

    #Computing the difference between a 
    # coordinate and another coordinate
    def distance(self, other):
        
        x_diff_sq = (self.x - other.x) ** 2

        y_diff_sq = (self.y - other.y) ** 2

        return (x_diff_sq + y_diff_sq) ** 0.5


    def __str__(self):

        return "<" + str(self.x) + "," + str(self.y) + ">"

    
    def getX(self):
        return self.x

    def getY(self):
        return self.y 

    def __eq__(self, other):
        return (self.getX() == other.getX()) and (self.getY() == other.getY())

    def __repr__(self):
        return "Coordinate(" + str(self.getX()) + "," + str(self.getY()) + ")"