from puzzles import Puzzles


class TestPuzzles:
    def __init__(self):
        self.results = ''

    def puzzle_1_1(self):
        try:
            assert 5 == Puzzles().day1_1('inputs/day1_1_test1.txt')
            assert 2 == Puzzles().day1_1('inputs/day1_1_test2.txt')
            assert 12 == Puzzles().day1_1('inputs/day1_1_test3.txt')
            assert 146 == Puzzles().day1_1('inputs/day1_final.txt')

            self.results += f'\nDay 1.1  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 1.1  {10 * "."}FAILURE'

    def puzzle_1_2(self):
        try:
            assert 4 == Puzzles().day1_2('inputs/day1_2_test1.txt')
            assert 131 == Puzzles().day1_2('inputs/day1_final.txt')

            self.results += f'\nDay 1.2  {10*"."}SUCCESS'
        except AssertionError:
            self.results += f'\nDay 1.2  {10 * "."}FAILURE'

    def test_all(self, print_results=False):
        self.puzzle_1_1()
        self.puzzle_1_2()

        if print_results:
            print(self.results)


if __name__ == '__main__':
    testing = TestPuzzles()
    testing.test_all(print_results=True)
