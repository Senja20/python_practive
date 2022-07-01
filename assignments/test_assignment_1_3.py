import pytest


class Data:
    def __init__(self, fake):
        self.string1 = fake.sentence()
        self.string2 = fake.sentence()
        self.word = fake.word()

        while self.word in self.string1 or self.word in self.string2:
            self.word = fake.word()


@pytest.fixture()
def data(fake):
    return Data(fake)


class TestAssignment13:
    # Tells if the strings are equal or not
    def test_equal_strings(self, app, data):
        app.check([data.string1, data.string1], ['are equal'], ['are not equal'])

    # Tells if the strings are equal or not
    def test_not_equal_strings(self, app, data):
        app.check([data.string1, data.string2], ['are not equal'], ['are equal'])

    # Tells if one string is a substring of the other
    def test_substring_first(self, app, data):
        app.check([data.string1, data.string1 + ' ' + data.word], ['is a substring'], ['is not a substring'])

    # Tells if one string is a substring of the other
    def test_substring_last(self, app, data):
        app.check([data.string1 + ' ' + data.word, data.string1], ['is a substring'], ['is not a substring'])

    # Tells if one string is a substring of the other
    def test_not_substring(self, app, data):
        app.check([data.string1, data.word], ['is not a substring'], ['is a substring'])
