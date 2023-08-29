from Course import *


class Student:

    # constructor
    def __init__(self, name, major, course_grades):
        self._name = name
        self._major = major
        self._course_grades = course_grades  # list of pairs (course object,grade)

    # getter
    def get_name(self):
        return self._name

    # getter
    def get_major(self):
        return self._major

    # getter
    def get_course_grades(self):
        return self._course_grades

    # setter
    def set_major(self, major):
        self._major = major

    # setter
    def set_course_grades(self, grades):
        self._course_grades = grades

    # return True if student takes course numbered cno; False otherwise
    def takes_course(self, cno):
        for course in self._course_grades:
            if course[0].get_cno() == cno:
                return True
        return False

    # return GPA for student (rounded to 2 decimal places)
    def gpa(self):
        total = 0
        total_credits = 0
        for courseGrade in self._course_grades:
            # CALCULATE BY MULTIPLYING BY GRADE POINTS(CREDITS)
            if courseGrade[1] == 'A':
                grade = 4.0
            elif courseGrade[1] == 'B':
                grade = 3.0
            elif courseGrade[1] == 'C':
                grade = 2.0
            elif courseGrade[1] == 'D':
                grade = 1.0
            else:
                grade = 0.0
            credit = int((courseGrade[0]).get_credits())
            grade *= credit
            total += grade
            total_credits += credit
        gpa = round(total / total_credits, 2)
        return gpa

    # add pair cg = (course,grade) to course_grades
    def add_course_grade(self, cg):
        self._course_grades.append(cg)

    # update grade for course with number cno; new grade is gr
    def update_course_grade(self, cno, gr):
        for coursegrade in self._course_grades:
            course = coursegrade[0]
            if course.get_cno() == cno:
                self._course_grades.remove(coursegrade)
                self._course_grades.append((course, gr))
                break

    # return string representation of student
    # see sample run for exact format to display student object
    def __str__(self):
        courseString = ''
        for course in self.get_course_grades():
            courseString += str(course[0]) + ' GRADE = ' + course[1] + '\n'

        returnString = '\nName: ' + self.get_name() + '\nMajor: ' + self.get_major() + '\n' \
                       + courseString + 'GPA: ' + str(self.gpa()) + '\n'

        return returnString

