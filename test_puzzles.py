from .puzzles import *


class TestPuzzles:
    results = ''

    def test_puzzle_1_1(self):
        assert day1_1('inputs/day1_1_test1.txt') == 5
        assert day1_1('inputs/day1_1_test2.txt') == 2
        assert day1_1('inputs/day1_1_test3.txt') == 12
        assert day1_1('inputs/day1_final.txt') == 146

    def test_puzzle_1_2(self):
        assert day1_2('inputs/day1_2_test1.txt') == 4
        assert day1_2('inputs/day1_final.txt') == 131

    def test_puzzle_2_1(self):
        assert day2_1('inputs/day2_test.txt') == '1985'
        assert day2_1('inputs/day2_final.txt') == '98575'

    def test_puzzle_2_2(self):
        assert day2_2('inputs/day2_test.txt') == '5DB3'
        assert day2_2('inputs/day2_final.txt') == 'CD8D4'

    def test_puzzle_3_1(self):
        assert is_triangle([5, 15, 19]) is True
        assert is_triangle([5, 15, 25]) is False
        assert day3_1('inputs/day3_final.txt') == 983

    def test_puzzle_3_2(self):
        assert day3_2('inputs/day3_2_test.txt') == 6
        assert day3_2('inputs/day3_final.txt') == 1836

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

    #           IF COMMENTED OUT IT'S DUE TO LONG COMPUTING TIME
    def test_puzzle_5_1(self):
        # assert door_breaker('abc') == '18f47a30'
        # assert day5_1('cxdnnyjw') == 'f77a0e6e'
        pass

    #           IF COMMENTED OUT IT'S DUE TO LONG COMPUTING TIME
    def test_puzzle_5_2(self):
        # assert door_breaker('abc', advanced=True) == '05ace8e3'
        # assert day5_2('cxdnnyjw') == '999828ec'
        pass


if __name__ == '__main__':
    pass
