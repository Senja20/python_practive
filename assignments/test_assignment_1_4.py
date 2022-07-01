import random
import string

import pytest


class Data:
    def __init__(self):
        self.letters = random.sample(string.ascii_lowercase, 4)
        self.string = ''.join(random.choices(self.letters, k=10))


@pytest.fixture()
def data():
    return Data()


class TestAssignment14:
    # Tells how many times each character of the alphabet appears in the string
    @pytest.mark.repeat(5)
    def test_character_count(self, app, data):
        app.check([data.string], ["'%c' : %i" % (letter, data.string.count(letter)) for letter in data.letters])
