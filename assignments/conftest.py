import os
import time

import faker
from faker import Faker
import pytest
from pexpect import *


@pytest.fixture(autouse=True)
def paths(tmpdir):
    owd = os.getcwd()
    os.chdir(tmpdir)
    yield owd, tmpdir
    os.chdir(owd)


@pytest.fixture()
def app(request, paths):
    owd, cwd = paths
    assignment = f'assignment_{ request.cls.__name__[-2] }_{ request.cls.__name__[-1] }'
    path = os.path.join(owd, 'solutions', assignment)
    main = os.path.join(path, 'main.py')

    assert os.path.isfile(main), 'Failed to find assignment main.py. Incorrect file or directory name?'

    arguments = []

    if hasattr(request, 'param'):
        arguments.extend([str(p) for p in request.param])

    child = spawn('python3', args=['-u', main] + arguments, timeout=1, encoding='utf-8')
    time.sleep(0.5)
    yield App(child, path)
    child.terminate(force=True)


@pytest.fixture(scope='class')
def fake() -> Faker:
    return faker.Faker()


def normalize_data(data):
    if data is None:
        data = []

    if type(data) in [int, float, str]:
        data = [data]

    return [str(d).strip() for d in data]


class App:
    def __init__(self, child, path):
        self.child = child
        self.path = path

    def check(self, input, expected_output=None, unexpected_output=None):
        input = normalize_data(input)
        expected_output = normalize_data(expected_output)
        unexpected_output = normalize_data(unexpected_output)

        for i in input:
            self.child.sendline(i)
            time.sleep(0.2)

        assert self.child.expect([TIMEOUT, EOF]) == 1,\
            '''
            Timed out while waiting for your program to exit.
            The program might be waiting on input or have an endless loop.

            =============
            Program input
            =============

            ''' + '\n'.join(input)

        self.child.terminate(force=True)

        output = [line.strip() for line in self.child.before.split('\n')]
        missing = set(expected_output).difference(output)
        unexpected = set(unexpected_output).intersection(output)

        assert not missing and not unexpected, get_details(input, output, missing, unexpected)


def get_details(input, interaction, missing, unexpected):
    s = '\n\n'

    data_sets = [
        (input, 'Program input'),
        (interaction, 'Program interaction'),
        (missing, 'Missing output'),
        (unexpected, 'Unexpected output')
    ]

    for data, name in data_sets:
        if len(data) > 0:
            s += ''.center(50, '*') + '\n'
            s += name.center(50) + '\n'
            s += ''.center(50, '*') + '\n\n'

            s += '\n'.join(data)
            s += '\n\n'

    return s
