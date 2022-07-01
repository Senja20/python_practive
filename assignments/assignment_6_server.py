from flask import *
from flask_restful import Resource, Api
from jsonschema import *
from werkzeug.exceptions import *

from assignment_helpers import *

app = Flask(__name__)
api = Api(app)

schema = {
    'type': 'object',
    'properties': {
        'id': {'type': 'number'},
        'name': {'type': 'string'},
        'email': {'type': 'string'},
        'year': {'type': 'number'}
    },
    'required': ['name', 'email', 'year'],
    'additionalProperties': False
}

nextId = 1


def generate_students():
    global nextId

    students = {}
    for i in range(random.randint(5, 10)):
        student = get_student(nextId)
        students[nextId] = student
        nextId += 1

    return students


students = generate_students()


class NextId(Resource):
    def get(self):
        global nextId
        return {'nextId': nextId}


class StudentList(Resource):
    def get(self):
        return list(students.values())

    def post(self):
        global nextId

        student = _validate_student(request)
        student['id'] = nextId
        students[nextId] = student

        nextId += 1

        return student, 201


class Student(Resource):
    def get(self, id):
        student = _get_student(id)
        return student

    def put(self, id):
        _student_exists(id)
        student = _validate_student(request)

        if 'id' not in student:
            raise BadRequest('Student is missing the id field.')

        if student['id'] != id:
            raise BadRequest('Object id differs from id in the URL.')

        students[id] = student

        return student, 200

    def delete(self, id):
        _student_exists(id)
        del students[id]

        return '', 204


api.add_resource(NextId, '/nextId')
api.add_resource(StudentList, '/students/')
api.add_resource(Student, '/students/<int:id>')


def _student_exists(id):
    if id not in students:
        raise NotFound('Student not found')


def _get_student(id):
    _student_exists(id)
    return students[id]


def _validate_student(request):
    student = request.get_json()

    try:
        validate(student, schema)
    except ValidationError as e:
        cause = e.message.split('\n')[0]
        raise BadRequest(f'POST data failed to validate. Invalid JSON? Error: {cause}')

    return student


if __name__ == '__main__':
    app.run(debug=True)
