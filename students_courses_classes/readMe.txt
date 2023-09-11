Program keeps track of courses, students, and their grades in courses they've taken.

Program takes name of a folder as command-lne argument. The folder must contain courses, students, and grades dat files. 

Commands:
	p displays all students in database
	s <name> displays attributes for a single student
	m <major> displays students in that major and their gpa
	g <gpa> displays all students with gpa greater than or equal to provided gpa
	a <Name:Class:gpaLetter> allows you to add a student to the database. This student will be written to appropriate database files
		example: a John:CSC1301:C
	c <Name:Class:gpaLetter> allows you to change the grade for someone's class
		example: c Blake:CSC1302:A
	q for quit
