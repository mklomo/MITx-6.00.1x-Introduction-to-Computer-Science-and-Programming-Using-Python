"""
ADT  Person which describes
name, birthday
"""
import datetime 

class Person(object):
    """
    Assumes name a string. 
    Create a person
    """

    def __init__(self, name):

        self._name = name

        try:
            # Starting from the right indicate the first blank space you see
            last_blank = name.rindex(" ")
            self._last_name = name[last_blank + 1 : ]

        except:
            self._last_name = name

        self._birthday = None 

    def get_name(self):
        """ Returns self's fullname """

        return self._name

    def get_last_name(self):
        """ Returns last name """
        return self._last_name

    def set_birthday(self, birthdate):
        """ Assumes birthdate is of type datetime.date 
            Sets self's birthday to birthdate
        """
        self._birthday = birthdate

    def get_age(self):
        """ Returns current age in days """
        if self._birthday == None:
            raise ValueError

        return (datetime.date.today() - self._birthday).days 


    def __lt__(self, other):
        """Assume other is of class Person()
        Return True if self preceded other in alphabetical order
        and False otherwise. Comparison is based on lastnames, but if these are the same 
        full names are compared
        """
        if self._last_name == other._last_name:
            return self._name < other._name
        return self._last_name < other._last_name


    def __str__(self):
        """ Returns self's name """

        return self._name


class MIT_person(Person):

    # This is a class variable
    _next_id_num = 0

    def __init__(self, name):

        # Inherit all the methods and __init__ from Person
        super().__init__(name)

        # Assign class variable to self._id_num
        self._id_num = MIT_person._next_id_num

        MIT_person._next_id_num += 1


    def get_id_num(self):
        """ Return the self._id_num """
        return self._id_num


    def __lt__(self, other):
        """ Return order of _id_num """ 
        return self._id_num < other._id_num

    # Check if MIT_person is a student or not

    def is_student(self):
        return isinstance(self, Student)

class Student(MIT_person):
    pass
    
class UG(Student):

    def __init__(self, name, class_year):
        
        super().__init__(name)

        self._year = class_year

    def get_class_year(self):
        return self._year

class Grad(Student):
    pass

class Transfer_student(Student):

    def __init__(self, name, from_school):
        super().__init__(name)
        self._from_school = from_school

    def get_old_school(self):
        return self._from_school

class Grades(object):
    """ Creates an empty GradeBook """
    def __init__(self):
        self._students = []
        self._grades = {}
        self._is_sorted = True 

    
    def add_student(self, student):
        """ Assumes: student of of type Student
            Adds student to the grade book """
        
        if student in self._students:
            raise ValueError("Duplicate student")

        self._students.append(student)
        self._grades[student.get_id_num()] = []
        self._is_sorted = False


    def add_grade(self, student, grade):
        """ Assumes grade is a float
            Add grade to the list of grades for student
        """

        try:
            self._grades[student.get_id_num()].append(grade)

        except:
            raise ValueError("student not in mapping")

    
    def get_grades(self, student):
        """ Return a list of students grades """

        try:
            return self._grades[student.get_id_num()][:]

        except:
            raise ValueError("student not in mapping")

    
    def get_students(self):
        """ Return a sorted list of the students in the grade book """
        if not self._is_sorted:
            self._students.sort()
            self._is_sorted = True

        return self._students[:]


def grade_report(course):
    """ Assumes course is of type Grades """

    report = ""

    for student in course.get_students():
        tot = 0.00
        num_grades = 0

        for grades in course.get_grades(student):
            tot += grades
            num_grades += 1
        try:
            average = tot/num_grades
            report = f"{report}\n{student}'s mean grade is {average}"
        except ZeroDivisionError:
            report = f"{report}\n{student} has no grades"

    return report










