class TestAssignment11:
    # Numbers 1 to 10
    def test_1_to_10(self, app):
        app.check([], ['1 2 3 4 5 6 7 8 9 10'])

    # Numbers 1 to 20, only even numbers
    def test_1_to_20_even(self, app):
        app.check([], ['2 4 6 8 10 12 14 16 18 20'])

    # Numbers 1 to 20, only odd numbers
    def test_one_to_20_odd(self, app):
        app.check([], ['1 3 5 7 9 11 13 15 17 19'])

    # Numbers 1 to 50, every 3rd number
    def test_1_to_50_every_3rd(self, app):
        app.check([], ['1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49'])

    # Numbers 1 to 40, reverse order, every 4th number
    def test_1_to_40_reverse_every_4th(self, app):
        app.check([], ['40 36 32 28 24 20 16 12 8 4'])

    # Numbers 1 to 100, prime numbers only
    def test_1_to_100_primes(self, app):
        app.check([], ['2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97'])
