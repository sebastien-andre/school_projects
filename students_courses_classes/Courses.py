from Course import *


class Courses:

    # constructor
    def __init__(self):
        self._data = {}

    # add course c to dictionary; do not add if course number already exists
    def add_course(self, c):
        key = c.get_cno()
        if key not in self._data:
            self._data[key] = c

    # return True if cno is in dictionary, False otherwise
    def is_course(self, cno):
        return cno in self._data

    # return a list of all course numbers
    def get_course_numbers(self):
        return list(self._data.keys())

    # return course object for cno; return None if no course with cno
    def get_course(self, cno):
        if cno not in self._data:
            return None
        else:
            return self._data[cno]

    # return string representation of courses object
    def __str__(self):
        courses_string = 'All GSU Courses\n--------------------\n'
        for course in self._data:
            courses_string += str(self._data[course]) + '\n'
        return courses_string + '--------------------'

    __repr__ = __str__
