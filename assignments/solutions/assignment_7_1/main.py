from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# get base class for table descriptions
Base = declarative_base()


class students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    year = Column(Integer)


def print_Main_Menu():
    print(f'1.Read all students\n'
          f'2.Get student by id\n'
          f'3.Add student\n'
          f'4.Edit student\n'
          f'5.Remove student\n'
          f'6.Search\n'
          f'7.Exit\n')


if __name__ == '__main__':

    engine = create_engine('sqlite:///school.sqlite')
    Session = sessionmaker(bind=engine)
    session = Session()

    while 1:

        print_Main_Menu()
        input_Value = int(input('\nEnter a value:'))
        print()

        if input_Value == 1:
            number_students = session.query(students).count()
            if number_students:
                student_all = session.query(students).all()
                for item in student_all:
                    print(f"id: {item.id},"
                          f" name: {item.name},"
                          f" email: {item.email},"
                          f" year: {item.year}")
            else:
                print("No students found\n")

        elif input_Value == 2:
            id_input = int(input("user id: "))
            students = session.query(students).filter(students.id == id_input).all()
            if students:
                for item in students:
                    print(f"id: {item.id},"
                          f"name: {item.name},"
                          f"email: {item.email},"
                          f"year: {item.year}")
            else:
                print("Student not found\n")

        elif input_Value == 3:
            new_name = input("Enter name:")
            new_email = input("Enter email:")
            new_year = int(input("Enter year:"))

            new_student = students(name=new_name, email=new_email, year=new_year)
            session.add(new_student)
            session.commit()

            new_student = session.query(students).\
                filter(students.name == new_name
                       and students.email == new_email
                       and students.year == new_year).all()

            for item in new_student:
                print(f"Added student: id: {item.id}, "
                      f"name: {item.name}, "
                      f"email: {item.email}, "
                      f"year: {item.year}")

        elif input_Value == 4:
            update_id = int(input("User id:"))
            update_name = input("User name:")
            update_email = input("User email:")
            update_year = int(input("User year:"))

            update_student = session.query(students).get(update_id)
            #update = update(students).where(students.id == 1).values(name = 'test')

            if update_student:
                update_student.name = update_name
                update_student.email = update_email
                update_student.year = update_year

                session.commit()

                print("Student was edited successfully")
            else:
                print("Student not found")

        elif input_Value == 5:
            delete_id = int(input("user id:"))
            print()

            delete_student = session.query(students).get(delete_id)
            if delete_student:
                session.delete(delete_student)
                session.commit()
                print("Student was removed successfully")
            else:
                print("Student not found")

        elif input_Value == 6:
            searched_name = input("\nEnter name:\n")
            print()

            search_student = session.query(students).filter(students.name.like(searched_name)).all()
            if search_student:
                for item in search_student:
                    print(f"id: {item.id},"
                          f" name: {item.name},"
                          f" email: {item.email},"
                          f" year: {item.year}")
            else:
                print("Student not found")
        elif input_Value == 7:
            break
        else:
            print('400 Bad Request')

"""
Notes, useless
from flask import Flask, request
from flask_restful import Api, Resource
from werkzeug.exceptions import *

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    return 'Я люблю тебя!'


books = {
    '123': {
        'title': 'yes'
    },
    '124': {
        'title': 'no'
    }
}


class BookList(Resource):
    def get(self):
        return list(books.values())


class Book(Resource):
    def get(self, isbn):
        if isbn not in books:
            raise NotFound('Invalid ISPN, book not found.')
        return books[isbn]

    def put(self, isbn):
        if isbn not in books:
            raise NotFound('Invalid ISPN, book not found.')

        book = request.get_json()

        books[isbn] = book

        return book


api.add_resource(BookList, '/books')
api.add_resource(Book, '/books/<isbn>')

app.run(debug=True)"""
