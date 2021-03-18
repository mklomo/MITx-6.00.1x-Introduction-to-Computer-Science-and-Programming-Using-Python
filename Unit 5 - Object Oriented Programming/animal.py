# Defining an Animal class
import random

class Animal(object):

    # Constructor or instance variable
    def __init__(self, age):
        self.age = age

        # This is set-up internally
        self.name = None


    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self, new_age):
        self.age = new_age

    def set_name(self, new_name = ""):
        self.name = new_name

    def __str__(self):
        return "animal: " + str(self.name) + ":" + str(self.age)


class Cat(Animal):
    def speak(self):
        return "meow"

    def __str___(self):
        return "cat: " + str(self.name) + ":" + str(self.age)


class Rabbit(Animal):

    # Now adding a class variable
    tag = 1
    def __init__(self, age, parent_1 = None, parent_2 = None):
        Animal.__init__(self, age)
        self.parent_1 = parent_1

        self.parent_2 = parent_2

        self.rid = Rabbit.tag

        Rabbit.tag += 1

    def get_name(self):
        return self.parent_1


    def set_parent_1_name(self, parent_1= ""):
        self.parent_1 = parent_1
        self.parent_2 = parent_2

    def set_parent_2_name(self, parent_2= ""):
        self.parent_2 = parent_2

    def get_rid(self):
        # Pad the string with three zeroes at the beginning
        return str(self.rid).zfill(3)

    def get_parent_1(self):
        return self.parent_1

    def get_parent_2(self):
        return self.parent_2


    def __add__(self, other):

        # Returning object of same type as this class

        return Rabbit(0, self, other)
    
    def __eq__(self, other):

        parents_same = self.parent_1.rid == other.parent_1.rid and self.parent_2.rid == other.parent_2.rid

        parents_opp = self.parent_2.rid == other.parent_2.rid and self.parent_1.rid == other.parent_1.rid

        return parents_same or parents_opp

    def speak(self):
        return "meep"

    def __str__(self):
        return "rabbit: " + str(self.name) + ":" + str(self.age)


class Person(Animal):

    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []

    def get_friends(self):
        return self.friends

    def add_friend(self, friend_name):
        if friend_name not in self.friends:
            self.friends.append(friend_name)

    def speak(self):
        return "hello"

    def age_diff(self, other):
        diff = self.get_age() - other.get_age()
        if self.get_age() > other.get_age():
            print(self.name, "is", diff, "years older than", other.name)

        else:
            print(self.name, "is", -diff, "years younger than", other.name)

    def __str__():
        return "person: "+ str(self.name) + ":" + str(self.age)


class Student(Person):
    def __init__(self, name, age, major= None):
        Person.__init__(self, name, age)
        self.major = major


    def change_major(self, major):
        self.major = major

    def speak(self):
        r = random.random()

        if r < 0.25:
            return "I have homework"

        elif 0.25 <= r <= 0.5:
            return "I need sleep"

        elif 0.5 <= r <= 0.75:
            return "I should eat"

        else:
            return "I am watching tv"

    def __str__(self):
        return "student: "+ str(self.name) + ":" + str(self.age)
