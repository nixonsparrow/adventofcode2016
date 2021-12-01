from ..puzzles import day9
import pytest


class TestDay9:
    @pytest.mark.parametrize(('a', 'b'),
        zip([input for input in day9.txt_opener('/../inputs/day9_test.txt')],
        (6, 7, 9, 11, 6, 18)))
    def test_decompressor(self, a, b):
        assert len(day9.decompressor(a)) == b

    @pytest.mark.ignored
    def test_part1(self):
        assert day9.part1() == 1

    @pytest.mark.ignored
    def test_part2(self):
        assert day9.part2() is True
