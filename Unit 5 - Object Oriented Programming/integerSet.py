


class Int_Set(object):
    
    # Lets initialize
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)

        except:
            raise ValueError(str(e) + " not found!")

    def __str__(self):
        self.vals.sort()
        result = ""
        for e in self.vals:
            result = result + str(e) + ","
        return "{" + result[: -1] + "}"



    def intersect(self, other):
        result = Int_Set()
        for i in self.vals:
            if i in other.vals:
                result.insert(i)
        return result
            


    def __len__(self):
        return len(self.vals)