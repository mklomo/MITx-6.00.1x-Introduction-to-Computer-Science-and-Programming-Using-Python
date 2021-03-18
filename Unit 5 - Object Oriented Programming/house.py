# Building House class


"""
    This class defines a house with the attributes street,
    rooms and bathrooms
"""

class House(object):

    # Initializing the instance variable
    def __init__(self, street, rooms, bathrooms):
        self.street = street
        self.rooms = rooms
        self.bathrooms = bathrooms

        # Not provided as input so every object attains the attribute
        self.clean = True

    def cleanHouse(self):
        if not self.clean:
            print("This house is now clean")

        else:
            print("This house is already clean")

    
    def uncleanHouse(self):
        if self.clean:
            self.clean = False
            print("This house is now dirty")

        else:
            print("This house was already dirty")


    def talk(self, phrase):
        print(phrase)

        