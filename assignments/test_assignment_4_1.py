import os
import random
import pytest
import json
from pathlib import Path


class Data:
    def __init__(self):
        self.students = []
        self.youngest = None
        self.oldest = None
        self.total_ages = 0


@pytest.fixture(autouse=True)
def data(paths, fake):
    data = Data()

    for i in range(random.randint(10, 20)):
        data.students.append({
            'id': i + 1,
            'name': fake.name(),
            'age': random.randint(18, 80),
            'attendance': random.randint(0, 100)
        })

        data.total_ages += data.students[-1]['age']

        if data.youngest is None or data.students[-1]['age'] < data.youngest['age']:
            data.youngest = data.students[-1]

        if data.oldest is None or data.students[-1]['age'] > data.oldest['age']:
            data.oldest = data.students[-1]

    with open('students.json', 'w') as json_file:
        json.dump(data.students, json_file)

    return data


class TestAssignment41:
    def test_youngest(self, app, data):
        app.check([], [f'Youngest: {data.youngest["name"]}'])

    def test_oldest(self, app, data):
        app.check([], [f'Oldest: {data.oldest["name"]}'])

    def test_average_age(self, app, data):
        app.check([], [f'Average age: {int(data.total_ages / len(data.students))}'])

    def test_low_attendance(self, app, data):
        good = ['Bad student: ' + student['name'] for student in data.students if student['attendance'] >= 30]
        bad = ['Bad student: ' + student['name'] for student in data.students if student['attendance'] < 30]

        app.check([], bad, good)

    def test_module_file(self, app):
        assert os.path.isfile(os.path.join(app.path, 'school.py')), 'Failed to find a module named school.py'

    def test_student_class(self, app):
        self.test_module_file(app)
        assert 'class Student' in Path(os.path.join(app.path, 'school.py')).read_text(), 'Failed to find Student class'

    def test_class_usage(self, app):
        assert 'Student(' in Path(os.path.join(app.path, 'main.py')).read_text(),\
            'Failed to find usage of Student class'
