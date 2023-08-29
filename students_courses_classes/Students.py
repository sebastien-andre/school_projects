from Student import *


class Students:

    # constructor
    def __init__(self):
        self._data = {}

    # add student s to dictionary; if student s already present do nothing
    def add_student(self, s):
        if len(s.get_name()) < 1:
            pass
        else:
            name = s.get_name()
            self._data[name] = s

    # return True of sname is present in dictionary; False otherwise
    def is_student(self, sname):
        if sname in self._data:
            return True
        else:
            return False

    # return a list of all student names
    def get_student_names(self):
        name_list = []
        for student in self._data:
            name_list.append(self._data[student].get_name())
        return name_list

    # return Student object for sname; return None if sname not in dictionary
    def get_student(self, sname):
        if self.is_student(sname):
            return self._data[sname]
        else:
            return None

    # getter
    def get_students(self):
        student_list = []
        for student in self._data:
            student_list.append(self._data[student])
        return student_list

    # return a list of pairs (sname,gpa) of student names and their GPAs
    # who have major m
    def get_students_by_major(self, m):
        GPAList = []
        for student in self._data:
            if self._data[student].get_major() == m:
                GPAList.append((student, self._data[student].gpa()))
        return GPAList

    # return a list of pairs (sname,major,gpa) of student names, their majors,
    # and their GPAs who have GPA greater or equal to g
    def get_students_by_gpa(self, g):
        GPAList = []
        for student in self._data:
            if self._data[student].gpa() >= g:
                GPAList.append((student, self._data[student].get_major(), self._data[student].gpa()))
        return GPAList

    # return String representation of student (see sample run for exact format of string)
    def __str__(self):
        students_string = ''

        for student in self._data:
            students_string += str(self._data[student])

        return students_string

