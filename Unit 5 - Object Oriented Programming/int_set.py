# Abstract Data Type Int_Set
# 
# 
class Int_Set(object):
    """ An Int_Set is a set of integers """
    # Value of a set is represented a list of ints, self.vals.
    # Each int in a set occurs in self._vals exactly once.

    def __init__(self):
        """
        Create an empty set of integers
        """
        self._vals = []

    
    def insert(self, e):
        """
        Assumes e is an integer and inserts e into self
        """
        if e not in self._vals:
            self._vals.append(e)

    
    def member(self, e): 
        """
        Assumes e is an integer 
        Returns True if e is in self, and False otherwise
        """
        return e in self._vals


    def remove(self, e):
        """
        Assumes e is an integer and removes e from self
        Raises error if e is not in self
        """

        try:
            self._vals.remove(e)

        except:
            raise ValueError(str(e) + " not found")

    def get_members(self):
        """
        Returns a list containing the elements of self._vals
        nothing can be assumed about the order of elements
        """
        return self._vals[:]


    def __str__(self):
        """
        Returns a string representation of self
        """

        if self._vals == []:
            return "{}"

        # This modifies the list itself and returns None
        self._vals.sort()

        result = ""

        for e in self._vals:
            result += str(e) + ","

        return f"{{{result[ : -1 ]}}}"


    def __add__(self, other):
        """
        Other is an Int_Set
        mutates self so that it contains exactly the elements is self plus
        the elements in other

        returns an instance of this class
        """

        # Initialize the result
        result = Int_Set()


        # Insert elements of self into instance
        for i in self._vals:
            result.insert(i)

        # Now we have result._vals == self.vals

        for i in range(len(other._vals)):
            # Iterate through the other instance
            if other._vals[i] not in self._vals:
                # Check if the element is not in sel._vals list; then add to result._vals
                result._vals += [other._vals[i]]

        return result








        