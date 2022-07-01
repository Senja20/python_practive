import random
import statistics

import pytest


class Data:
    def __init__(self):
        self.even_numbers = random.sample(range(10, 1000), 10)
        self.even_numbers = [x / 10 for x in self.even_numbers]

        self.odd_numbers = random.sample(range(10, 1000), 9)
        self.odd_numbers = [x / 10 for x in self.odd_numbers]


@pytest.fixture()
def data():
    return Data()


class TestAssignment21:
    # Prints out the average
    @pytest.mark.repeat(3)
    def test_average(self, app, data):
        average = round(statistics.mean(data.even_numbers), 2)
        app.check(data.even_numbers + [0], f'Average : {average}')

    # Prints out the median
    @pytest.mark.repeat(3)
    def test_median_even(self, app, data):
        median = round(statistics.median(data.even_numbers), 2)
        app.check(data.even_numbers + [0], f'Median : {median}')

    # Prints out the median
    @pytest.mark.repeat(3)
    def test_median_odd(self, app, data):
        median = round(statistics.median(data.odd_numbers), 2)
        app.check(data.odd_numbers + [0], f'Median : {median}')

    # Prints out the numbers sorted, in descending order
    @pytest.mark.repeat(3)
    def test_sorted_descending(self, app, data):
        descending = data.even_numbers.copy()
        descending.sort(reverse=True)
        app.check(data.even_numbers + [0], 'Descending : %s' % (' '.join([str(i) for i in descending])))
