from ..puzzles import day9
import pytest


class TestDay9:
    @pytest.mark.parametrize(('sequence', 'length'),
        zip([input for input in day9.txt_opener('/../inputs/day9_test.txt')],
        (6, 7, 9, 11, 6, 18)))
    def test_decompressor(self, sequence, length):
        assert len(day9.decompressor(sequence)) == length

    @pytest.mark.parametrize(('filename', '_type'), zip(
                             ('/../inputs/day9_test.txt', '/../inputs/day9_final.txt'),
                             ('list', 'str')))
    def test_txt_opener(self, filename, _type):
        assert type(day9.txt_opener(filename)).__name__ == _type

    def test_part1(self):
        assert day9.part1('/../inputs/day9_final.txt') == 112830

    @pytest.mark.ignored
    def test_part2(self):
        assert day9.part2() is True
