import statistics
from operator import attrgetter
import json  # json-library
import school  # school.py file import, contains the Student Class

student_list = []
with open('students.json') as json_file:  # open students.json file
    root = json.load(json_file)  # making a root to enter the json file

    for a in root:  # looping through the file and defining attributes in the list
        id = a['id']
        name = a['name']
        age = a['age']
        attendance = a['attendance']

        # Adding object with its attributes to the list, still inside the for-loop
        # By using ".append()" adding objects to the list
        # "school.Student(*attributes*)" says that we'll find the class students in school file
        student_list.append(school.Student(id, name, age, attendance))

    # Sorting the list by age and printing the first (youngest) and the last (Oldest) values
    student_list.sort(key=attrgetter('age'))  # here only attregetter key works for sorting, for some reason...
    print(f'Youngest: {student_list[0].name}')
    print(f'Oldest: {student_list[-1].name}')  # "-1" gets us to the last value in the list

    # Using mean () function from statistics library to find the average age
    avg = statistics.mean(Student.age for Student in student_list)
    print(f'Average age: {int(avg)}')  # using int() to round avg variable cuz the local testing is dumb

    for a in range(len(student_list)):  # go through the list with objects
        if student_list[a].attendance < 30:  # if attribute "attendance" is lower than 30, print function will run
            print(f'Bad student: {student_list[a].name}')
