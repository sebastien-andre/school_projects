import sys
import os
from Student import *
from Students import *
from Course import *
from Courses import *


# Open three files, courses.dat, students.dat, and grades.dat, present in directory dname
# Read the data and construct the courses and students dictionaries
# Return the two dictionaries as a pair (see main() for the order)
def load_data(dname):
    # load course data
    with open('./' + dname + '/courses.dat', 'r') as f:
        course_data = (f.read()).split('\n')
        f.close()

    # load student data
    with open('./' + dname + '/students.dat', 'r') as g:
        student_data = (g.read()).split('\n')
        g.close()

    # load grade data
    with open('./' + dname + '/grades.dat', 'r') as h:
        grade_data = (h.read()).split('\n')
        h.close()

    my_courses = Courses()
    for x in range(len(course_data)):
        split_course = course_data[x].split(':')
        cn = split_course[0]
        ct = split_course[1]
        cr = split_course[2]
        c = Course(cn, ct, cr)
        my_courses.add_course(c)

    course_grades = {}
    # for x in list of course/grades for a student
    # split at colon for entry by name, and put all with same name as values in dictionary(tuples)
    for grade_list in grade_data:
        grade_list = grade_list.split(':')
        name = grade_list[0]
        cno = grade_list[1]
        grade = grade_list[2]
        full_course = my_courses.get_course(cno)
        pair = (full_course, grade)
        if name not in course_grades:
            course_grades[name] = [pair]
            continue
        a_list = course_grades[name]
        a_list.append(pair)
        course_grades[name] = a_list



    my_students = Students()
    student_data.sort()
    for x in range(len(student_data)):
        split_student = student_data[x].split(':')
        name = split_student[0]
        major = split_student[1]
        list_courses = course_grades[name]
        c = Student(name, major, list_courses)
        my_students.add_student(c)

    return my_courses, my_students



def store_data(courses, students, dname):
    students_write = ''
    count = 0
    for student in students.get_students():
        count += 1
        students_write += str(student.get_name()) + ':' + str(student.get_major())
        if count < len(students.get_student_names()):
            students_write += '\n'

    courses_write = ''
    courses_list = courses.get_course_numbers()
    count = 0
    for cno in courses_list:
        count += 1
        course = courses.get_course(cno)
        courses_write += str(course.get_cno()) + ':' + str(course.get_ctitle()) + ':' + str(course.get_credits())
        if count < len(courses_list):
            courses_write += '\n'

    grades_write = ''
    count = 0
    for student in students.get_students():
        for coursegrade in student.get_course_grades():
            if count > 0:
                grades_write += '\n'
            count += 1
            course = coursegrade[0]
            grade = str(coursegrade[1])
            name = str(student.get_name())
            grades_write += name + ':' +  str(course.get_cno()) + ':' + grade

    # store course data
    with open('./' + dname + '/courses.dat', 'w') as f:
        f.write(courses_write)
        f.close()

    # store student data
    with open('./' + dname + '/students.dat', 'w') as g:
        g.write(students_write)
        g.close()

    # store grade data
    with open('./' + dname + '/grades.dat', 'w') as h:
        h.write(grades_write)
        h.close()


def main():
    # Load courses, students from file
    courses, students = load_data(sys.argv[1])
    # print(courses)
    # print(students)
    print("\nWelcome to Grades Database Program\n")
    while True:
        command = input("p, s sname, m major, g gpa, a sname:cno:grade, c sname:cno:grade, q: ").strip()
        if len(command) < 1:
            print("\nInvalid command!\n")
            continue
        elif command[0] == 'p':
            print(students)
        elif command[0] == 's':
            sname = command[2:].strip()
            s = students.get_student(sname)
            if s != None:
                print(s)
            else:
                print("\n" + sname + " NOT FOUND\n")
        elif command[0] == 'm':
            major = command[2:].strip()
            ss = students.get_students_by_major(major)
            print()
            if len(ss) > 0:
                for s in ss:
                    print(s[0] + "\t" + str(s[1]))
            else:
                print("NO Students FOUND!")
            print()
        elif command[0] == 'g':
            try:
                gg = float(command[2:].strip())
            except:
                print("\nInvalid GPA Search!\n")
                continue
            ss = students.get_students_by_gpa(gg)
            print()
            if len(ss) > 0:
                for s in ss:
                    print(s[0] + "\t" + s[1] + "\t" + str(s[2]))
            else:
                print("NO Students FOUND!")
            print()
        elif command[0] == 'a':
            # a sname:cno:grade
            record = command[2:].strip().split(":")
            if len(record) != 3:
                print("\nInvalid input to add course!\n")
                continue
            student = students.get_student(record[0])
            if student == None:
                print("\nInvalid Student. Cannot add course grade.\n")
                continue
            course = courses.get_course(record[1])
            if course == None:
                print("\nInvalid Course. Cannot add course grade.\n")
                continue
            if record[2].upper() not in ['A', 'B', 'C', 'D', 'F']:
                print("\nInvalid Grade. Cannot change course grade.\n")
                continue
            else:
                student.add_course_grade((course, record[2].upper()))
                print("\n", record, " ADDED\n")
        elif command[0] == 'c':
            # c sname:cno:grade
            record = command[2:].strip().split(":")
            if len(record) != 3:
                print("\nInvalid input to change course grade!\n")
                continue
            student = students.get_student(record[0])
            if student == None:
                print("\nInvalid Student. Cannot change course grade.\n")
                continue
            if student.takes_course(record[1]):
                if record[2].upper() in ['A', 'B', 'C', 'D', 'F']:
                    student.update_course_grade(record[1], record[2])
                    print("\nGRADE CHANGED\n")
                else:
                    print("\nInvalid Grade. Cannot change course grade.\n")
                    continue
            else:
                print("\nInvalid Course. Cannot change course grade.\n")
                continue
            print()
        elif command[0] == 'q':
            break
        else:
            print("\nInvalid command\n")
    store_data(courses, students, sys.argv[1])
    print("\nBye!\n")


main()
