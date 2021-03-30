# Abstract Data Type Toy


class Toy(object):      # Class is a subclass of the object superclass
    def __init__(self):
        self.elements = []

    def add(self, new_element):
        """
        Adding new elements to a self.elements

        new_element = list of variables    
        """
        self.elements += new_element

    
    def __len__(self):
        return len(self.elements)


    def __add__(self, other):
        """
        other = instance of toy

        returns a new instance of toy
        """

        new_toy = Toy()
        new_toy.elements = self.elements + other.elements

        return new_toy


    def __eq__(self, other):
        return self.elements == other.elements


    def __str__(self):
        return str(self.elements)


    def __hash__(self):
        return id(self)


    