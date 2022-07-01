import random
import pytest


class Data:
    def __init__(self, fake):
        self.palindrome = fake.word()
        self.palindrome += self.palindrome[::-1]
        self.not_palindrome = fake.word() + str(random.randint(0, 9))


@pytest.fixture()
def data(fake):
    return Data(fake)


class TestAssignment12:
    # Tells how many letters are in the word
    def test_letters(self, app, data):
        app.check([data.not_palindrome], [len(data.not_palindrome)])

    # Tells if the word is a palindrome
    def test_palindrome(self, app, data):
        app.check([data.palindrome], ['is a palindrome'], ['is not a palindrome'])

    # Tells if the word is a palindrome
    def test_not_palindrome(self, app, data):
        app.check([data.not_palindrome], ['is not a palindrome'], ['is a palindrome'])

    # Prints the word reversed
    def test_reverse(self, app, data):
        app.check([data.not_palindrome], [data.not_palindrome[::-1]])
