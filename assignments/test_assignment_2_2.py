import random
import pytest


class Data:
    def __init__(self, fake):
        count = random.randint(10, 20)

        self.unique_words = fake.words(nb=count, unique=True)
        self.words = self.unique_words.copy()

        # Repeat some of the words
        for _ in range(random.randint(5, 10)):
            self.words.append(self.words[random.randint(0, count - 1)])

        random.shuffle(self.words)


@pytest.fixture()
def data(fake):
    return Data(fake)


class TestAssignment22:
    # Prints how many unique words have been entered
    def test_unique_words(self, app, data):
        app.check(data.words + ['stop'], f'Unique : { len(data.unique_words) }')

    # Prints how many words in total have been entered
    def test_total_words(self, app, data):
        app.check(data.words + ['stop'], f'Total : { len(data.words) }')

    # Prints how many times each word has been entered
    @pytest.mark.parametrize('index', random.sample(range(10), 3))
    def test_word_count_sentence(self, app, data, index):
        word = data.unique_words[index]
        app.check(data.words + ['stop'], ['%s : %i' % (word, data.words.count(word))])
