from .puzzles import *


class TestPuzzles:
    results = ''

    def test_puzzle_1_1(self):
        assert 5 == day1_1('inputs/day1_1_test1.txt')
        assert 2 == day1_1('inputs/day1_1_test2.txt')
        assert 12 == day1_1('inputs/day1_1_test3.txt')
        assert 146 == day1_1('inputs/day1_final.txt')

    def test_puzzle_1_2(self):
        assert 4 == day1_2('inputs/day1_2_test1.txt')
        assert 131 == day1_2('inputs/day1_final.txt')

    def test_puzzle_2_1(self):
        assert '1985' == day2_1('inputs/day2_test.txt')
        assert '98575' == day2_1('inputs/day2_final.txt')

    def test_puzzle_2_2(self):
        assert '5DB3' == day2_2('inputs/day2_test.txt')
        assert 'CD8D4' == day2_2('inputs/day2_final.txt')

    def test_puzzle_3_1(self):
        assert is_triangle([5, 15, 19]) is True
        assert is_triangle([5, 15, 25]) is False
        assert 983 == day3_1('inputs/day3_final.txt')

    def test_puzzle_3_2(self):
        assert 6 == day3_2('inputs/day3_2_test.txt')
        assert 1836 == day3_2('inputs/day3_final.txt')

    def test_puzzle_4_1(self):
        assert is_room_real(open('inputs/day4_1_test1.txt').readline()) is True
        assert is_room_real(open('inputs/day4_1_test2.txt').readline()) is True
        assert is_room_real(open('inputs/day4_1_test3.txt').readline()) is True
        assert is_room_real(open('inputs/day4_1_test4.txt').readline()) is False
        assert get_room_value(open('inputs/day4_1_test1.txt').readline()) == 123
        assert day4_1('inputs/day4_final.txt') == 278221

    def test_puzzle_4_2(self):
        assert caesar_decrypter('qzmt-zixmtkozy-ivhz-343') == 'very encrypted name'
        assert day4_2('inputs/day4_final.txt') == 267

    def test_puzzle_5_1(self):
        assert 5 != 1


if __name__ == '__main__':
    pass
