# Students Courses Classes Management System

This Python-based program manages courses, students, and their grades efficiently, keeping track of the academic progress of students across various courses. It takes the name of a folder as a command-line argument, where the folder must contain data files for courses, students, and grades.

## Features

- **Comprehensive Data Handling:** Manages courses, students, and grades data stored in `.dat` files within a specified folder.
- **Flexible User Commands:** Offers a variety of commands for displaying student information, including listing all students, displaying details for a single student, and showing students by major or GPA.
- **Dynamic Data Manipulation:** Allows adding a new student to the database or changing a student's grade in a course through user input.
- **Error Handling:** Includes error handling for file operations and data processing to ensure robust program execution.

## Usage

Run the program from the command line, providing the folder name containing the `.dat` files as an argument:

```bash
python Driver.py folder_name
```


### Commands

- `p`: Displays all students in the database.
- `s <name>`: Displays attributes for a single student.
- `m <major>`: Displays students in that major and their GPA.
- `g <gpa>`: Displays all students with a GPA greater or equal to the provided GPA.
- `a <Name:Class:GPALetter>`: Allows you to add a student to the database. This student will be written to appropriate database files.
  - Example: `a John:CSC1301:C`
- `c <Name:Class:GPALetter>`: Allows you to change the grade for someone's class.
  - Example: `c Blake:CSC1302:A`
- `q`: Quits the program.

## Implementation Details

The program is structured around several key Python classes:

- `Course.py`: Defines the `Course` class with attributes for course number, title, and credits.
- `Courses.py`: Manages a collection of `Course` objects, including adding courses and querying course information.
- `Student.py`: Represents a student with attributes for name, major, and a list of course grades.
- `Students.py`: Manages a collection of `Student` objects, offering functionality to add students, search by major or GPA, and update student information.

Data from `.dat` files are loaded into these classes at program start. The user can interact with the data through a series of commands that manipulate and display student and course information.

## File Structure

- **courses.dat**: Contains data on courses offered.
- **students.dat**: Contains data on students enrolled.
- **grades.dat**: Contains grades awarded to students for each course.
