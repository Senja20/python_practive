import os
import random
import sqlite3

import pytest

from assignment_helpers import *


students = [get_student(i) for i in range(1, random.randint(5, 10))]
courses = [get_course(i) for i in range(1, random.randint(5, 10))]
tests = [get_test(i, random.randint(1, len(courses))) for i in range(1, random.randint(5, 10))]
student_course = []
# Add students to courses
for student in students:
    student_courses = random.sample(courses, random.randint(0, 4))
    for course in student_courses:
        student_course.append((student['id'], course['id']))


def insert_data(database, data, table):
    c = database.cursor()

    for item in data:
        values = ','.join(['?'] * len(item.values()))
        c.execute(f'INSERT INTO {table} VALUES ({values})', tuple(item.values()))

    database.commit()


@pytest.fixture(autouse=True)
def database(paths):
    owd, _ = paths
    conn = sqlite3.connect('school.sqlite')

    c = conn.cursor()

    with open(os.path.join(owd, 'test_assignment_8_1.sql'), 'r') as file:
        sql = file.read()

    c.executescript(sql)

    conn.commit()

    insert_data(conn, students, 'students')
    insert_data(conn, courses, 'courses')
    insert_data(conn, tests, 'tests')

    conn.commit()

    # Add students to courses
    for sc in student_course:
        c.execute(f'INSERT INTO students_courses VALUES (?,?)', sc)

    conn.commit()

    return conn


def get_data(database, table):
    c = database.cursor()
    c.execute(f'SELECT * FROM {table}')
    return c.fetchall()


class TestAssignment81:
    @pytest.mark.parametrize('choice,type,factory,data', [
        (1, 'student', get_student, students),
        (2, 'course', get_course, courses),
        (3, 'test', get_test, tests)
    ])
    def test_add(self, app, database, choice, type, factory, data):
        table = type + 's'

        item = factory(app)

        if type == 'test':
            item['course_id'] = random.choice(courses)['id']

        item_expected = item.copy()
        item_expected['id'] = len(data) + 1

        del item['id']

        app.check([choice] + list(item.values()) + ['7'], [f'Added {type} with id {item_expected["id"]}'])

        assert tuple(item_expected.values()) in get_data(database, table),\
            f'Failed to find new {type} in database. Input given: {" ".join([str(v) for v in item.values()])}'

    def test_add_student_to_course_invalid_student(self, app):
        app.check([4, len(students) + 1, 7], ['Student not found'])

    def test_add_student_to_course_invalid_course(self, app):
        app.check([4, 1, len(courses) + 1, 7], ['Course not found'])

    def test_add_student_to_course_valid(self, app, database):
        student_id = random.choice(students)['id']
        course_id = random.choice(courses)['id']

        app.check([4, student_id, course_id, 7], [f'Added student to course id {course_id}'])

        assert (student_id, course_id) in get_data(database, 'students_courses'),\
            f'Failed to find student connected to course in database. Input given: {student_id} {course_id}'

    def test_get_courses_by_student_valid(self, app, database):
        student_id = random.choice(students)['id']
        course_names = ', '.join(course['name'] for course in courses if (student_id, course['id']) in student_course)

        app.check([5, student_id, 7], [f'Courses for student {student_id}: {course_names}'])

    def test_get_tests_by_course_valid(self, app, database):
        course_id = random.choice(courses)['id']
        test_names = ', '.join(test['name'] for test in tests if test['course_id'] == course_id)

        app.check([6, course_id, 7], [f'Tests for course {course_id}: {test_names}'])

    def test_exit(self, app):
        app.check(['7'], [])
