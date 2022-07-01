import csv
import json
import os
import random
import string

import pytest

from assignment_helpers import *

sum_numbers = random.sample(range(100), 10)
generate_start = random.randrange(0, 10)
generate_stop = random.randrange(10, 50)

filename = ''.join(random.sample(string.ascii_lowercase, k=8))


@pytest.fixture()
def posts():
    return get_posts()


@pytest.fixture(autouse=True)
def jsonfile(paths, posts):
    jsonpath = os.path.join(f'{filename}.json')

    with open(jsonpath, 'w') as json_file:
        json.dump(posts, json_file)


class TestAssignment51:
    @pytest.mark.parametrize('app', [['sum'] + sum_numbers], indirect=True)
    def test_sum(self, app):
        app.check([], [f'Sum: {sum(sum_numbers)}'])

    @pytest.mark.parametrize('app',
                             [['generate', '--start', generate_start, '--stop', generate_stop, '--step', 1]],
                             indirect=True)
    def test_generate_step1(self, app):
        app.check([], [f'Generated: {" ".join([str(num) for num in range(generate_start, generate_stop, 1)])}'])

    @pytest.mark.parametrize('app',
                             [['generate', '--start', generate_start, '--stop', generate_stop, '--step', 2]],
                             indirect=True)
    def test_generate_step2(self, app):
        app.check([], [f'Generated: {" ".join([str(num) for num in range(generate_start, generate_stop, 2)])}'])

    @pytest.mark.parametrize('app',
                             [['generate', '--start', generate_start, '--stop', generate_stop, '--step', 3]],
                             indirect=True)
    def test_generate_step3(self, app):
        app.check([], [f'Generated: {" ".join([str(num) for num in range(generate_start, generate_stop, 3)])}'])

    @pytest.mark.parametrize('app',
                             [['convert', '--input', f'{filename}.json', '--output', f'{filename}.csv']],
                             indirect=True)
    def test_convert(self, app, posts):
        app.check([])

        csv_file = f'{filename}.csv'
        assert os.path.isfile(csv_file), f'Failed to find CSV output file.'

        csv_data = []
        with open(csv_file) as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                csv_data.append(row)

        assert all(post in csv_data for post in posts), 'Data from the JSON file is missing in the CSV file.'
