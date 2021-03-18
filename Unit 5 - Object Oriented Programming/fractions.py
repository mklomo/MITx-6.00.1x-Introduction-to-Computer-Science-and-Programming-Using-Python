# Defining Fractions and its methods


class Fraction(object):

    # Lets initialize this class with its instance variables

    def __init__(self, num, denom):
        
        self.num = num

        self.denom = denom


    # Printing the instance NOT the method output

    def __str__(self):
        return "< " + str(self.num) + "/" + str(self.denom) + " >"


    # Defining getters
    def getNum(self):
        return self.num

    def getDenom(self):
        return self.denom

    def __add__(self, other):

        num_New = (other.getNum() * self.getDenom()) + (self.getNum() * other.getDenom())

        denom_New = (other.getDenom() * self.getDenom())

        return Fraction(num_New, denom_New)

    def __sub__(self, other):

        num_New = (other.getNum() * self.getDenom()) - (self.getNum() * other.getDenom())

        denom_New = (other.getDenom() * self.getDenom())

        return Fraction(num_New, denom_New)


    # Conver fractions into floats

    def convert(self):
        return (self.getNum() / self.getDenom())

