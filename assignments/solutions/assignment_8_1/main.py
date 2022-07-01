from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

students_courses_table = Table('students_courses', Base.metadata,
                               Column('student_id', Integer, ForeignKey('students.id')),
                               Column('course_id', Integer, ForeignKey('courses.id')),
                               order_by='course_id')


class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    year = Column(Integer)

    courses = relationship('Courses', back_populates='students',
                           secondary=students_courses_table)


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    max_students = Column(Integer)

    students = relationship('Students', back_populates='courses',
                            secondary=students_courses_table)
    tests = relationship('Tests', back_populates='course')


class Tests(Base):
    __tablename__ = 'tests'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date_time = Column(String)

    course_id = Column(Integer, ForeignKey('courses.id'))
    course = relationship('Courses', back_populates='tests')


def print_main():
    print(f'1.Add student\n'
          f'2.Add course\n'
          f'3.Add test\n'
          f'4.Add student to course\n'
          f'5.List courses by student\n'
          f'6.List tests by course\n'
          f'7.Exit\n')


if __name__ == '__main__':

    engine = create_engine('sqlite:///school.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    while 1:
        print_main()
        user_input = int(input('\nEnter your choice:\n'))

        if user_input == 1:
            new_name = input("Enter name:")
            new_email = input("Enter email:")
            new_year = int(input("Enter year:"))

            add_student = Students(name=new_name, email=new_email, year=new_year)
            session.add(add_student)
            session.commit()

            added_student = session.query(Students).filter(Students.name == new_name
                                                           and Students.email == new_email
                                                           and Students.year == new_year).all()
            if added_student:
                for item in added_student:
                    print(f"Added student with id {item.id}\n")
            else:
                print("Error! Failed to get the student")

        elif user_input == 2:
            new_name = input("Enter name:")
            max_number = int(input("Enter max students:"))

            add_course = Courses(name=new_name, max_students=max_number)
            session.add(add_course)
            session.commit()

            added_course = session.query(Courses).filter(Courses.name == new_name).all()
            if added_course:
                for item in added_course:
                    print(f"Added course with id {item.id}\n")
            else:
                print("Error! Failed to get the course")

        elif user_input == 3:
            new_course_id = int(input('Enter course id:'))
            new_name = input("Enter name:")
            new_data_time = input("Enter data and time:")

            add_test = Tests(name=new_name, date_time=new_data_time, course_id=new_course_id)
            session.add(add_test)
            session.commit()

            added_test = session.query(Tests).filter(Tests.name == new_name).all()
            if added_test:
                for item in added_test:
                    print(f"Added test with id {item.id}\n")
            else:
                print('Error! Failed to get the test')

        elif user_input == 4:
            id_name = int(input("user id:"))
            student = session.query(Students).filter(Students.id == id_name).all()
            if student:
                for std_item in student:
                    print(f"Found student with id {std_item.id}")

                id_course = int(input("course id:"))
                course = session.query(Courses).filter(Courses.id == id_course).all()
                if course:
                    for crs_item in course:
                        print(f"Found course with id {crs_item.id}")

                        statement = students_courses_table.insert().values(student_id=id_name, course_id=id_course)

                        session.execute(statement)
                        session.commit()
                        print(f'Added student to course id {id_course}')

                else:
                    print("Course not found\n")
            else:
                print("Student not found\n")

        elif user_input == 5:
            id_student = int(input("Id:"))

            course_list = []
            # student = session.query(Students).filter(Students.id == id_student).all()
            student = session.query(Students).get(id_student)
            if student:

                courses = list(student.courses)
                courses.sort(key=lambda c: c.id)

                for item in courses:
                    course_list.append(item.name)
                new_list = ', '.join(map(str, course_list))
                print(f'Courses for student {id_student}: {new_list}')
            else:
                print('Student not found')

        elif user_input == 6:
            """Asks the user for a course id then lists all the tests for this course.The tests must be sorted by id, 
            lowest first. Expected output: Tests for course < id >: <test name >, < test name > ... 
            Or: Course not found"""

            id_course = int(input("course id:"))
            test_list = []

            testes = session.query(Tests).filter(Tests.course_id == id_course).all()

            for item in testes:
                test_list.append(item.name)

            test_list = ', '.join(map(str, test_list))
            print(f'Tests for course {id_course}: {test_list}')

        elif user_input == 7:
            break
        else:
            print('400 Bad Request')
