import puzzles


class TestPuzzles:
    def __init__(self):
        self.results = ''

    def puzzle_1_1(self):
        try:
            assert 5 == puzzles.day1_1('inputs/day1_1_test1.txt')
            assert 2 == puzzles.day1_1('inputs/day1_1_test2.txt')
            assert 12 == puzzles.day1_1('inputs/day1_1_test3.txt')
            assert 146 == puzzles.day1_1('inputs/day1_final.txt')

            self.results += f'\nDay 1.1  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 1.1  {10 * "."}FAILURE'

    def puzzle_1_2(self):
        try:
            assert 4 == puzzles.day1_2('inputs/day1_2_test1.txt')
            assert 131 == puzzles.day1_2('inputs/day1_final.txt')

            self.results += f'\nDay 1.2  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 1.2  {10 * "."}FAILURE'

    def puzzle_2_1(self):
        try:
            assert '1985' == puzzles.day2_1('inputs/day2_test.txt')
            assert '98575' == puzzles.day2_1('inputs/day2_final.txt')

            self.results += f'\nDay 2.1  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 2.1  {10 * "."}FAILURE'

    def puzzle_2_2(self):
        try:
            assert '5DB3' == puzzles.day2_2('inputs/day2_test.txt')
            assert 'CD8D4' == puzzles.day2_2('inputs/day2_final.txt')

            self.results += f'\nDay 2.2  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 2.2  {10 * "."}FAILURE'

    def test_all(self, print_results=False):
        self.puzzle_1_1()
        self.puzzle_1_2()
        self.puzzle_2_1()
        self.puzzle_2_2()

        if print_results:
            print(self.results)


if __name__ == '__main__':
    testing = TestPuzzles()
    testing.test_all(print_results=True)
