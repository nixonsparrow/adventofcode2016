from ..puzzles import day4
from os import path


class TestDay4:

    def test_part1(self):
        assert day4.is_room_real(open(path.dirname(__file__) + '/../inputs/day4_1_test1.txt').readline()) is True
        assert day4.is_room_real(open(path.dirname(__file__) + '/../inputs/day4_1_test2.txt').readline()) is True
        assert day4.is_room_real(open(path.dirname(__file__) + '/../inputs/day4_1_test3.txt').readline()) is True
        assert day4.is_room_real(open(path.dirname(__file__) + '/../inputs/day4_1_test4.txt').readline()) is False
        assert day4.get_room_value(open(path.dirname(__file__) + '/../inputs/day4_1_test1.txt').readline()) == 123
        assert day4.part1('/../inputs/day4_final.txt') == 278221

    def test_part2(self):
        assert day4.caesar_decrypter('qzmt-zixmtkozy-ivhz-343') == 'very encrypted name'
        assert day4.part2('/../inputs/day4_final.txt') == 267

